# Changelog — inkframe skill

## v2.2.0 — 2026-04-17

**比例回退至 8:3**

- 所有 prompt 模板、Quick Reference Card 中的比例从 `16:9` 改回 `8:3 ultra-wide`
- `generate-cover.py` SIZE_PRESETS 从 `16:9` 改回 `8:3`
- ASCII 构图预览帧从 64×18 改回 64×12（row ~4 / ~8 三分法坐标）

---

## v2.1.0 — 2026-04-17

**16:9 比例统一**

- 所有 prompt 模板、Quick Reference Card、示例 prompt 中的比例从 `16:6` 改为 `16:9`
- `generate-cover.py` SIZE_PRESETS 从 `21:9` 改为 `16:9`
- ASCII 构图预览帧从 64×12 调整为 64×18（monospace 字符高宽比约 2:1，64×18 对应 16:9）
- 三分法坐标更新：row ~6（top 1/3）、row ~12（bottom 1/3）
- ASCII 示例图重绘为 18 行版本，✦ 交点位置同步修正

---

## v2.0.0 — 2026-04-17

**三层 Prompt 框架**

- 新增 Three-Layer Prompt Framework 章节，将 prompt 构建拆解为三层：
  - Layer 1：具体名词（主体＋动作＋环境＋光线），每个维度附 few-shot 示例
  - Layer 2：有视觉锚点的风格词，替代无效的情绪评价词；附 ink storyboard 适配版情绪→视觉词对照表（6 组 few-shot）
  - Layer 3：魔法词，仅作末尾增强，不可替代前两层
- Prompt Formula 重构：模板明确标注三层分隔，填写顺序清晰
- Step 10 新增三层自检清单：输出 prompt 前逐层验证
- Common Pitfalls 新增：evaluative emotion words 训练信号太弱，应替换为 Layer 2 视觉锚点词

---

## v1.9.0 — 2026-04-17

**重命名 skill**

- Skill 名稱從 `show-dont-tell-image` 改為 `inkframe`
- 目錄從 `.claude/skills/show-dont-tell-image/` 改為 `.claude/skills/inkframe/`
- 更簡短易記：ink（風格）+ frame（構圖/分鏡）

---

## v1.8.0 — 2026-04-17

**腳本路徑遷移**

- 修正腳本路徑：`generate-cover.py` 從 `scripts/` 遷移至 `.claude/skills/show-dont-tell-image/scripts/`
- 所有 SKILL.md 中的命令行示例同步更新為新路徑
- Changelog 從 SKILL.md 移至獨立的 CHANGELOG.md 文件

---

## v1.7.0 — 2026-04-17

**移除具名版權引用**

- 移除所有對「Marcos Mateu-Mestre」及《Framed Ink》的具名引用，以規避潛在版權風險
- 改以風格特徵描述取代：「dramatic ink storyboard style — extreme high-contrast B&W, bold brushstrokes, woodcut-like rendering」
- 所有 prompt 模板、Core Style DNA、Quick Reference Card、示例 prompt 同步更新

---

## v1.6.0 — 2026-04-09

**參考圖工作流**

- 新增 Step 6：搜尋參考圖工作流（Wikimedia Commons 搜索 → 提供鏈接 → 用戶選擇 → 下載縮小）
- 新增 `scripts/fetch-references.py`：接收用戶貼回的 URL，下載、縮小至 800px、存入 `output/covers/references/`
- `scripts/generate-cover.py` 支持多張 `--input` 圖片
- Step 10 首次生圖改為「提示詞 + 參考圖」一起傳入，顯著提升解剖準確度
- 原 Step 6–9 順延為 Step 7–10

---

## v1.5.0 — 2026-04-09

**「Show, Don't Tell」感知設計層**

- 新增 Core Philosophy 章節：「不告訴觀眾感受什麼，而是讓他們感受到」——提示詞不是描述圖，是設計感知觸發結構
- 整合五大 show-don't-tell 原則：
  - 光線承載情緒（描述具體光源，不說「悲傷場景」）
  - 遮蔽與剪影代替完整描繪
  - 構圖留白製造沉默（負空間傳遞情緒重量）
  - 截斷動作，讓故事延伸至畫框之外
  - 氛圍三角：光線硬度 × 畫面動靜 × 冷暖對比
- 前五步改為互動式場景探索工作流：
  - Step 1：從用戶真實熟悉的世界出發，探索題材
  - Step 2：生成三個場景的中文文字描述（無提示詞，無情緒判斷）
  - Step 3：針對未選中方向續探，湊成最終三個方向
  - Step 4：網絡搜索核實動物行為/自然現象，糾正不符真實的細節
  - Step 5：確認情緒方向，從三個場景選出最匹配者
- 原 Step 1–4 順延為 Step 6–9
- Step 6 新增說明：鏡頭角度選擇需基於 Step 5 確認的情緒方向

---

## v1.4.0 — 2026-04-06

**圖生圖編輯 + CMYK 漫畫上色**

- 新增 `--input` 圖像編輯模式，支持在已有圖片基礎上局部調整
- 新增 CMYK 漫畫上色流程：傳統印刷平塗風格（60–80 年代紙質漫畫感）
- 新增叢林場景 CMYK 色彩對照表（樹葉、螞蟻、光柱、陰影等各元素對應顏色）
- Step 5 CLI 說明擴充：增加編輯與上色命令示例
- Post-Generation Editing 章節獨立，記錄局部調整和上色兩類用法

---

## v1.3.0 — 2026-04-06

**CLI 命令行交付路徑**

- Step 5 新增雙路徑交付說明：
  - Option A：Nano Banana（瀏覽器粘貼）
  - Option B：`scripts/generate-cover.py`（命令行，更快、可腳本化）
- 記錄 CLI 用法：`--size preview / medium / full` 三種尺寸
- 輸出統一保存至 `output/covers/`，文件名含時間戳
- 備注：API 透過 OpenRouter `image_config` 使用 `21:9` 比例

---

## v1.2.0 — 2026-04-06

**動物主角 + 三分法構圖**

- 新增「動物為主角」原則：文章主題涉及動物時，動物作為畫面第一主體，承載情緒重量
- 新增三分法構圖規則：動物必須落在四個 ✦ 交匯點之一，禁止居中
- 有動物時人物比例縮小至 ≤5% 畫面高度（無動物時保持 10–15%）
- ASCII 預覽增加三分法網格標注：✦ 符號位置及座標說明
- Quick Reference Card 增加 `ANIMAL` 與 `PLACEMENT` 字段
- Core Style DNA 表格新增兩行：動物主角原則、三分法定位規則

---

## v1.1.0 — 2026-04-06

**ASCII 構圖預覽步驟**

- 新增 Step 4（現為 Step 8）：輸出完整 prompt 前先生成 ASCII 構圖預覽
- 預覽採用 16:6 寬屏比例框架
- 用符號標注主體位置（`○` 或 `人`）與環境質量感（`▓`、`║`、`~`、`/\` 等）
- 每個預覽下方附一行說明圖注：鏡頭角度、主體位置、氛圍
- 工作流程改為：確認構圖 → 輸出 prompt（而非直接輸出）
- 附完整示例（鳥瞰沼澤場景）

---

## v1.0.0 — 2026-04-06

**首次發布**

- 核心風格 DNA：基於 Marcos Mateu-Mestre《Framed Ink》6 大視覺原則
  - 極端鏡頭角度、高對比黑白、環境壓制人物、不對稱構圖、電影感、放射動態線條
- Prompt 公式：7 要素結構（鏡頭角度、主體動作、比例、環境、非對稱入侵、光線、動態線條）
- 分步工作流程：主題 → 鏡頭角度 → 環境 → prompt 輸出
- 三個完整示例 prompt：自然環境、城市科技、抽象概念
- 常見錯誤清單（對稱構圖、平視角度、大比例人物等）
- Quick Reference Card（速查卡）
