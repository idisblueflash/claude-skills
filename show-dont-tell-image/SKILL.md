---
name: newsletter-cover-image
version: 1.8.0
description: Generate Nano Banana (Google Gemini) prompts for cinematic newsletter cover images in dramatic ink storyboard style — extreme high-contrast black and white, bold brushstrokes, woodcut-like rendering, used in professional film and animation pre-visualization. Use this skill whenever the user wants to create a newsletter cover image, a cover visual, a hero image for an article, or any cinematic illustration prompt. Also trigger when the user mentions "Nano Banana", "newsletter cover", "cover image", "封面图", "storyboard style", or asks to generate an AI image prompt for editorial or storytelling purposes.
---

# Newsletter Cover Image — Nano Banana Prompt Generator

This skill generates optimized prompts for **Nano Banana (Google Gemini image model)** to create cinematic newsletter cover images in **dramatic ink storyboard style** — extreme high-contrast B&W, bold brushstrokes, woodcut-like rendering, the visual language of professional film and animation pre-visualization.

---

## Core Philosophy: Show, Don't Tell

**不告訴觀眾感受什麼，而是讓他們感受到。**

好的提示詞不是描述圖，是設計一個感知觸發結構。具體動作、光線方向、構圖留白——這些才是情緒的載體，不是形容詞。

生成最終提示詞時，每一條都必須對應到具體的畫面決策：

| 原則 | 做法 |
|------|------|
| **光線承載情緒，不說情緒** | 描述具體光源位置、方向、硬度，而非「悲傷的場景」 |
| **遮蔽與剪影代替完整描繪** | 用剪影、遮擋、局部入鏡讓觀眾自行填補 |
| **構圖留白製造沉默** | 負空間傳遞情緒重量；主體佔比越小，孤獨感越強 |
| **截斷的動作，畫框外的故事** | 動作指向畫框之外，暗示未知的延續 |
| **氛圍三角（光線 × 節奏 × 色調）** | 從光線硬度、畫面動靜、冷暖對比三個維度同時設計 |

---

## Core Style DNA

All prompts must encode these visual principles derived from classic cinematic ink storyboard technique:

| Principle | What it means |
|-----------|--------------|
| **Extreme camera angles** | Bird's eye, worm's eye, extreme dutch tilt — never neutral eye-level |
| **High contrast B&W** | Near-zero gray midtones, bold ink shadows, woodcut feel |
| **Environment dominates figure** | Subject appears small, overwhelmed by surroundings |
| **Chaotic, asymmetric framing** | Foliage, architecture, or elements intrude from all sides unevenly |
| **Cinematic mood** | Every frame tells a story — tension, isolation, wonder, urgency |
| **Radial dynamic lines** | Speed lines, ripples, or radial strokes to imply motion and energy |
| **Animal as protagonist** | When the article theme connects to an animal, make the animal the primary subject — not the human. The animal carries the emotional weight of the image. |
| **Rule-of-thirds placement** | The animal (or primary subject) must be placed at one of the four rule-of-thirds intersection points — NEVER centered. Human figures, if present, retreat to the opposite corner at ≤5% of frame. |

---

## Prompt Formula

Build every prompt using this structure:

```
Generate a cinematic storyboard panel in dramatic ink illustration style — 
extreme high-contrast black and white, bold brushstrokes, woodcut-like 
rendering, the visual language of professional film pre-visualization.

[CAMERA ANGLE — be extreme and specific]
[SUBJECT + ACTION — who is doing what]
[SCALE RATIO — subject must feel small, e.g. "occupying no more than 15% of frame"]
[ENVIRONMENT — describe what surrounds and overwhelms the subject]
[ASYMMETRIC INTRUSION — elements pressing in from all sides, NOT symmetrically]
[LIGHTING — harsh, directional, cinematic source]
[DYNAMIC LINES — ripples, speed lines, radial strokes]

Render in dramatic ink storyboard style: extreme black and white ink contrast, 
almost zero gray midtones, bold heavy brushstrokes, rough expressive lines, 
woodcut-like rendering. No soft shading. No color.
No text, no letters, no handwriting, no annotations, no captions anywhere 
in the image.

Mood: [choose: trapped / hopeful / isolated / triumphant / tense / awe-struck]
Aspect ratio: 16:6 ultra-wide cinematic panel.
```

---

## Step-by-Step Workflow

---

### Step 1: 探索題材

向用戶提問：

> 這次想生成什麼主題的圖？你對什麼題材最熟悉——你第一個浮現的畫面是什麼？

**目的**：讓用戶從自己真實熟悉的世界出發，而非泛泛描述。最強的畫面往往來自用戶最具體的個人記憶或知識領域。

---

### Step 2: 第一輪場景候選（中文描述，無提示詞）

根據用戶的題材輸入，生成三個場景的**中文文字描述**。

每個場景描述需包含：
- 具體動物/人物/主體
- 一個核心的**動作或關係**（而非情緒）
- 構圖的大致邏輯（視角、主體大小、遮擋方式）

**不給提示詞，不給情緒判斷。**

結尾提示：
> 請用數字選擇你想保留的場景（可選 1 個或 2 個，例如：「保留 1 3」）

---

### Step 3: 第二輪場景候選

針對**未被選中**的方向繼續探索，再生成三個新場景。

同樣只給中文描述，不給提示詞。

結尾提示：
> 請繼續用數字選擇，和上一輪保留的場景湊成最終 3 個（例如：「加上 5」）

---

### Step 4: 網絡搜索核實事實

對三個確認場景中涉及的**動物行為、自然現象、物理動作**進行網絡搜索。

調整方向：
- 糾正不符合真實行為的細節（例如動物的實際姿態、習性）
- 補充更具體、更有畫面感的真實細節
- 在修訂後，說明依據（一句話即可）

**不改變場景的核心構圖意圖，只讓細節更紮實。**

---

### Step 5: 確認情緒方向

向用戶提問：

> 這張圖你最想讓觀眾感受到什麼？（例如：安全感、孤獨、期待、壓迫、溫柔……）

根據用戶的情緒描述，從三個場景中**選出最匹配的一個**，並說明選擇理由：
- 哪個場景的核心動作天然承載這種情緒
- 哪個場景需要太多解釋才能傳遞這種情緒（排除原因）

結尾確認：
> 我選擇場景 X，因為 [一句話理由]。你確認嗎？

---

### Step 6: 搜尋參考圖

確認情緒方向和場景後，立即搜索 Wikimedia Commons 找真實相關照片作為解剖/姿態參考。

**搜索步驟：**

1. 在 Wikimedia Commons 搜索與場景主體相關的圖片（動物行為、自然場景）：
   - 搜索 URL 格式：`https://commons.wikimedia.org/w/index.php?search=KEYWORD&title=Special:MediaSearch&type=image`
   - 關鍵字聚焦在**動作和姿態**，例如：`leopard cub climbing tree`、`eagle fledgling cliff`
2. 列出 4–6 張候選圖的直接 URL（`upload.wikimedia.org` 連結），每條附一句描述

向用戶展示：
> 以下是找到的參考圖連結，請選擇你想用的（可複製 URL 貼回給我）：
> 1. [描述] → URL
> 2. [描述] → URL
> ...

**用戶貼回 URL 後，運行下載腳本：**

```bash
./scripts/fetch-references.py \
  "URL1" "URL2" "URL3" \
  --topic TOPIC-SLUG
```

腳本自動下載、縮小至 800px、存入 `output/covers/references/`，並輸出文件路徑供後續步驟使用。

**如果某張圖下載失敗（403、超時等）：**

告知用戶哪張失敗，請他：

> 請在瀏覽器打開這個 URL，把圖片保存到本地，然後**把文件拖入對話框**（不是截圖粘貼）。

拖入方式的原因：拖文件進 Claude Code 時，Claude 同時能看到圖片內容 **也能獲得本地文件路徑**，可以直接對該路徑做縮圖和保存操作：

```bash
python3 -c "
from PIL import Image
img = Image.open('USER_DRAGGED_FILE_PATH')
img.thumbnail((800, 800))
img.convert('RGB').save('output/covers/references/TOPIC-N.jpg', 'JPEG', quality=75)
print('Saved.')
"
```

流程繼續，不因單張失敗而中斷。

---

### Step 7: Choose a camera angle
Match the confirmed mood (from Step 5) to an angle:

| Mood | Camera Angle |
|------|-------------|
| Overwhelmed / threatened | Nearly 90° bird's eye, straight down |
| Hopeful / ascending | Extreme worm's eye, looking up |
| Isolated / lost | High angle, wide environment, tiny figure |
| Tense / urgent | Dutch tilt, medium-close, chaotic framing |
| Awe / discovery | Low angle, subject silhouetted against vast sky |

### Step 8: Build the environment
The environment must **visually compress or overwhelm** the subject:
- Urban: buildings, scaffolding, crowd, neon signs pressing in
- Nature: giant leaves, bamboo, waves, storm clouds
- Abstract: data streams, geometric shapes, converging lines
- Interior: corridors, shelves, machinery, shadows

### Step 9: Preview composition with ASCII art
Before writing the full prompt, generate an ASCII art sketch showing the rough composition.

**Rules for ASCII preview:**
- Use a 16:6 wide aspect ratio frame (e.g. 64 chars × 12 lines)
- Show camera angle by how the scene is framed (top-down = subject at center-bottom, worm's eye = wide top)
- Mark the figure as a tiny `○` or `人` (always small — ≤15% of frame, or ≤5% when an animal is present)
- Mark environment elements with rough symbols: `▓` (dark mass), `│` (vertical), `─` (horizontal), `~` (water/waves), `/\` (foliage), `*` (light source)
- **Rule-of-thirds grid**: always mark the 4 intersection points with `✦` in the ASCII frame (at ~1/3 and ~2/3 of both width and height). The animal/primary subject must sit on one of these `✦` points.
- No detail — just masses, angles, and placement
- Add a one-line caption below: `Camera: [angle] | Animal: [1/3 position] | Human: [corner] | Mood: [emotion]`

**Rule-of-thirds intersections** (for a 64×12 frame):
```
col ~21 = left 1/3     col ~43 = right 1/3
row ~4  = top 1/3      row ~8  = bottom 1/3

Four intersection points:
  ✦ top-left    (col 21, row 4)
  ✦ top-right   (col 43, row 4)
  ✦ bottom-left (col 21, row 8)
  ✦ bottom-right(col 43, row 8)
```

**Example (bird's eye, swamp):**
```
╔══════════════════════════════════════════════════════════════╗
║  /\/\    ▓▓▓▓▓▓▓▓▓▓▓    /\/\/\/\   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ║
║ /\/\/\   ▓▓▓▓▓▓▓▓▓▓▓   /\/\/\/\/\  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ║
║▓▓▓/\/\▓▓▓▓▓  ~~~  ▓▓▓▓▓▓ /\/\ ▓▓▓▓▓▓▓  ~~~  ▓▓▓▓▓▓▓▓▓▓  ║
║▓▓▓▓▓▓▓▓▓▓▓  ~~ ○ ~~  ▓▓▓▓▓▓▓▓▓▓▓▓▓  ~~~ ~~~  ▓▓▓▓▓▓▓▓▓  ║
║▓▓▓▓▓▓▓▓▓▓▓  ~~~~~~~  ▓▓▓▓▓▓▓▓▓▓▓▓▓  ~~~~~~~  ▓▓▓▓▓▓▓▓▓  ║
║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ║
╚══════════════════════════════════════════════════════════════╝
Camera: ~90° bird's eye | Figure: center, tiny (○) | Mood: trapped
```

Ask: **"構圖大致這樣，要調整嗎？"** — wait for confirmation or edits before proceeding.

### Step 10: Write and deliver the prompt
After the user confirms the composition, output the full prompt in a code block.

The prompt can be used in two ways:

**Option A — Nano Banana (browser)**
Paste directly into [Nano Banana](https://nano.banana.com).

**Option B — Command line (faster, scriptable)**
Use `scripts/generate-cover.py` in this repo (requires `OPENROUTER_API_KEY` in `.env`):

```bash
# First generation — include reference images downloaded in Step 6
.claude/skills/show-dont-tell-image/scripts/generate-cover.py "YOUR PROMPT" \
  --input output/covers/references/TOPIC-1.jpg \
          output/covers/references/TOPIC-2.jpg \
          output/covers/references/TOPIC-3.jpg \
  --size preview

# Subsequent edits — use the generated image as base
.claude/skills/show-dont-tell-image/scripts/generate-cover.py "YOUR PROMPT" --size preview   # draft
.claude/skills/show-dont-tell-image/scripts/generate-cover.py "YOUR PROMPT" --size medium    # review

# Edit an existing image (image-to-image)
.claude/skills/show-dont-tell-image/scripts/generate-cover.py "YOUR EDIT INSTRUCTION" \
  --input output/covers/cover-medium-xxx.png \
  --size medium
```

Images are saved to `output/covers/` with timestamp filename.
Size presets use aspect ratio `21:9` via OpenRouter `image_config`.

---

## Post-Generation Editing

All edits use `--input` mode (image-to-image). Pass the saved image path and describe only what to change.

### Local adjustments
```bash
.claude/skills/show-dont-tell-image/scripts/generate-cover.py \
  "Reduce the number of ants to one third. Keep everything else identical." \
  --input output/covers/cover-medium-xxx.png --size medium
```

### Colorization — Traditional Comic CMYK
Apply flat comic-book color to a finished B&W image:

```bash
.claude/skills/show-dont-tell-image/scripts/generate-cover.py \
  "Colorize using traditional comic book CMYK style. Limited flat palette — bold cyan, magenta, yellow, warm tan/brown. Ink-black lines stay sharp. Flat fills, no gradients. Style: 1960s–1980s printed comic page. Keep all composition and linework identical." \
  --input output/covers/cover-medium-xxx.png --size medium
```

**CMYK color guide for jungle scenes:**
| Element | Color |
|---------|-------|
| Forest floor / roots | Warm brown, dark tan |
| Leaves | Olive-green, yellowed |
| Ants | Dark brown-black |
| Light shafts | Warm yellow-white |
| Deep shadows | Pure black |
| Sky / clearings | Pale cyan |

---

## Example Prompts by Theme

### 🌿 Nature / Environment
```
Generate a cinematic storyboard panel in dramatic ink illustration style — 
extreme high-contrast black and white, bold brushstrokes, woodcut-like rendering.

The camera is positioned almost directly overhead — nearly 90 degrees 
straight down — looking down at a lone figure standing in a dark tropical 
swamp. The figure must appear very tiny, occupying no more than 15% of 
the frame height, facing upward toward the camera.

Chaotic, oversized tropical leaves and bamboo canes intrude aggressively 
from all four sides — NOT symmetrically. The water surface shows 
concentric ripple rings. Radial dynamic speed lines on the leaves suggest 
motion and danger.

Render in dramatic ink storyboard style: extreme black and white ink contrast, 
almost zero gray midtones, bold heavy brushstrokes, rough expressive lines, 
woodcut-like rendering. No soft shading. No color.
No text, no letters, no handwriting, no annotations, no captions anywhere 
in the image.

Mood: trapped, isolated, overwhelmed.
Aspect ratio: 16:6 ultra-wide cinematic panel.
```

### 🏙️ Urban / Technology
```
Generate a cinematic storyboard panel in dramatic ink illustration style — 
extreme high-contrast black and white, bold brushstrokes, woodcut-like rendering.

Extreme worm's eye view looking up from ground level at a lone figure 
standing at the base of towering skyscrapers that converge dramatically 
overhead. The figure occupies no more than 10% of the frame height, 
dwarfed by the urban canyon around them.

Glass facades, fire escapes, and signage intrude from left and right 
asymmetrically. Harsh light slices down between buildings from a single 
overhead source, casting deep ink-black shadows. Perspective lines 
radiate outward from the figure toward all four corners of the frame.

Render in dramatic ink storyboard style: extreme black and white ink contrast, 
almost zero gray midtones, bold heavy brushstrokes, rough expressive lines, 
woodcut-like rendering. No soft shading. No color.
No text, no letters, no handwriting, no annotations, no captions anywhere 
in the image.

Mood: awe-struck, insignificant, determined.
Aspect ratio: 16:6 ultra-wide cinematic panel.
```

### 💡 Abstract / Ideas
```
Generate a cinematic storyboard panel in dramatic ink illustration style — 
extreme high-contrast black and white, bold brushstrokes, woodcut-like rendering.

High angle looking down at a figure seated at a small desk, surrounded 
by an endless sea of floating paper, open books, and swirling documents 
that radiate outward in all directions. The figure occupies no more than 
10% of the frame. A single cone of harsh light illuminates the desk 
from directly above like a spotlight, while everything else fades to 
dense black shadow.

Paper edges and document corners intrude asymmetrically from all sides. 
Radial spiral lines suggest the overwhelming flow of information.

Render in dramatic ink storyboard style: extreme black and white ink contrast, 
almost zero gray midtones, bold heavy brushstrokes, rough expressive lines, 
woodcut-like rendering. No soft shading. No color.
No text, no letters, no handwriting, no annotations, no captions anywhere 
in the image.

Mood: overwhelmed, focused, searching.
Aspect ratio: 16:6 ultra-wide cinematic panel.
```

---

## Common Pitfalls to Avoid

- ❌ **Symmetric compositions** — always specify "NOT symmetrically"
- ❌ **Eye-level camera** — always push to an extreme angle
- ❌ **Large figures** — always quantify smallness ("no more than 15% of frame")
- ❌ **Soft gradients** — always include "almost zero gray midtones"
- ❌ **Generic "black and white"** — always specify "woodcut-like", "heavy ink", "bold brushstrokes"
- ❌ **Neutral mood** — always end with a specific emotional direction
- ❌ **Handwritten text / annotations** — always include "No text, no letters, no handwriting, no annotations, no captions anywhere in the image"

---

## Quick Reference Card

```
ANGLE:       bird's eye (~90°) / worm's eye / extreme dutch tilt
ANIMAL:      primary subject when present — placed at one rule-of-thirds intersection
FIGURE SIZE: human "no more than 5% of frame" when animal present; 10–15% otherwise
PLACEMENT:   animal at ✦ intersection (NOT centered); human at opposite corner/edge
DIRECTION:   "facing toward the camera" OR "back to camera"
FOLIAGE/ENV: "intrude aggressively from all sides — NOT symmetrically"
CONTRAST:    "extreme B&W ink, almost zero gray midtones"
LINES:       "radial speed lines / concentric ripples / converging perspective"
STYLE REF:   "dramatic ink storyboard, cinematic pre-viz, woodcut-like"
NO TEXT:     "No text, no letters, no handwriting, no annotations, no captions"
MOOD:        one clear emotion word
RATIO:       "16:6 ultra-wide cinematic panel"
```
