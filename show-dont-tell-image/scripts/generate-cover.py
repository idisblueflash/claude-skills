#!/usr/bin/env python3
"""
Generate newsletter cover images via OpenRouter + Gemini image model.

Usage:
    ./scripts/generate-cover.py "your prompt"
    ./scripts/generate-cover.py "your prompt" --size preview
    ./scripts/generate-cover.py "your prompt" --size medium
    ./scripts/generate-cover.py "your prompt" --size full --output output/covers

Size presets (all 8:3 / ultra-wide ratio):
    preview  →  aspect 8:3, image_size 0.5K  (quick draft, cheapest)
    medium   →  aspect 8:3, image_size 1K    (review quality)
    full     →  aspect 8:3, image_size 2K    (final publish)

Aspect ratio is passed via image_config.aspect_ratio per OpenRouter spec.
Image size is passed via image_config.image_size.
"""

import argparse
import base64
import json
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: requests not installed. Run: pip install requests", file=sys.stderr)
    sys.exit(1)


def load_dotenv():
    """Load .env from project root (two levels up from scripts/)."""
    env_path = Path(__file__).parent.parent / ".env"
    if not env_path.exists():
        return
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)


load_dotenv()

DEFAULT_MODEL = "google/gemini-3.1-flash-image-preview"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# (aspect_ratio, image_size) per OpenRouter image_config spec
SIZE_PRESETS = {
    "preview": ("21:9", "1K"),   # 0.5K not supported by this model
    "medium":  ("21:9", "1K"),
    "full":    ("21:9", "2K"),
}


def build_content(prompt: str, input_images: list[Path]) -> list | str:
    """Build message content — plain text for generation, multipart for editing."""
    if not input_images:
        return prompt
    blocks = []
    for img in input_images:
        mime = "image/jpeg" if img.suffix.lower() in (".jpg", ".jpeg") else "image/png"
        b64 = base64.b64encode(img.read_bytes()).decode()
        blocks.append({"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}"}})
    blocks.append({"type": "text", "text": prompt})
    return blocks


def call_api(prompt: str, model: str, aspect_ratio: str, image_size: str,
             input_images: list[Path] | None = None) -> dict:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: OPENROUTER_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/newsletter-composing",
        "X-Title": "Newsletter Cover Image Generator",
    }

    payload = {
        "model": model,
        "modalities": ["image", "text"],
        "messages": [{"role": "user", "content": build_content(prompt, input_images or [])}],
        "image_config": {
            "aspect_ratio": aspect_ratio,
            "image_size": image_size,
        },
    }

    print(f"→ model:  {model}", flush=True)
    print(f"→ ratio:  {aspect_ratio}  size: {image_size}", flush=True)

    try:
        resp = requests.post(API_URL, headers=headers, json=payload, timeout=120)
    except requests.exceptions.Timeout:
        print("Error: request timed out (120s)", file=sys.stderr)
        sys.exit(1)

    if resp.status_code != 200:
        print(f"Error {resp.status_code}:\n{resp.text}", file=sys.stderr)
        sys.exit(1)

    return resp.json()


def extract_image(data: dict) -> tuple:
    """Extract (image_bytes, ext) from OpenRouter response.

    Actual location: choices[0]['message']['images'][0]['image_url']['url']
    Format: data:image/jpeg;base64,...
    """
    def decode_url(url: str):
        if url.startswith("data:image"):
            header, b64 = url.split(",", 1)
            ext = header.split("/")[1].split(";")[0]  # jpeg / png / webp
            return base64.b64decode(b64), ext
        if url.startswith("http"):
            r = requests.get(url, timeout=60)
            r.raise_for_status()
            ct = r.headers.get("Content-Type", "image/jpeg")
            ext = ct.split("/")[1].split(";")[0]
            return r.content, ext
        return None, None

    # Primary: choices[0].message.images (actual OpenRouter format)
    try:
        images = data["choices"][0]["message"].get("images") or []
        for img in images:
            url = img.get("image_url", {}).get("url", "")
            if url:
                b, e = decode_url(url)
                if b:
                    return b, e
    except (KeyError, IndexError):
        pass

    # Fallback: top-level images field
    for img in data.get("images") or []:
        url = img.get("image_url", {}).get("url", "")
        if url:
            b, e = decode_url(url)
            if b:
                return b, e

    # Fallback: choices[0].message.content blocks
    try:
        content = data["choices"][0]["message"]["content"]
        if isinstance(content, list):
            for block in content:
                if block.get("type") == "image_url":
                    b, e = decode_url(block["image_url"]["url"])
                    if b:
                        return b, e
        elif isinstance(content, str):
            b, e = decode_url(content)
            if b:
                return b, e
    except (KeyError, IndexError):
        pass

    print("Error: no image found in response.", file=sys.stderr)
    print("Top-level keys:", list(data.keys()), file=sys.stderr)
    sys.exit(1)


def save_image(image_bytes: bytes, ext: str, output_dir: Path, size_label: str) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = output_dir / f"cover-{size_label}-{ts}.{ext}"
    path.write_bytes(image_bytes)
    return path


def main():
    parser = argparse.ArgumentParser(
        description="Generate newsletter cover images via OpenRouter + Gemini",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("prompt", help="Image generation prompt")
    parser.add_argument(
        "--size", default="preview",
        choices=list(SIZE_PRESETS.keys()),
        help="Size preset: preview (0.5K draft) / medium (1K) / full (2K) — default: preview",
    )
    parser.add_argument(
        "--output", default="output/covers",
        help="Output directory (default: output/covers)",
    )
    parser.add_argument(
        "--model", default=DEFAULT_MODEL,
        help=f"OpenRouter model ID (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--input", nargs="+", default=None, metavar="IMAGE",
        help="Path(s) to existing image(s) for edit/reference mode (supports multiple)",
    )

    args = parser.parse_args()
    aspect_ratio, image_size = SIZE_PRESETS[args.size]

    input_images = []
    if args.input:
        for p in args.input:
            img = Path(p)
            if not img.exists():
                print(f"Error: input image not found: {img}", file=sys.stderr)
                sys.exit(1)
            input_images.append(img)
        print(f"→ edit mode: {', '.join(str(i) for i in input_images)}", flush=True)

    data = call_api(args.prompt, args.model, aspect_ratio, image_size, input_images or None)
    image_bytes, ext = extract_image(data)
    output_path = save_image(image_bytes, ext, Path(args.output), args.size)
    print(f"✓ Saved → {output_path}")


if __name__ == "__main__":
    main()
