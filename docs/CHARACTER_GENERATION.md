# 像素风角色生成指南

## 🎨 快速生成方案

### 方案 1：使用 AI 图像生成（推荐）

#### 步骤：
1. 选择 AI 工具（DALL-E/Midjourney/Stable Diffusion）
2. 复制下面对应角色的提示词
3. 生成图片
4. 下载图片
5. 放到 `frontend/assets/skins/characters/` 目录
6. 命名为 `初.png`, `博.png`, `昊.png`, `竹.png`, `东.png`, `千.png`

---

## 📋 角色提示词

### 初（男生，红色）
```
Pixel art character sprite sheet, 64x64 pixels per frame,
cute anime boy with red spiky hair, wearing casual t-shirt,
accessory: headphones,
idle animation (4 frames), walking (8 frames), working (4 frames), drunk (2 frames),
transparent background, 16-bit RPG style, red and white color scheme
```

### 博（男生，青色）
```
Pixel art character sprite sheet, 64x64 pixels per frame,
cute anime boy with cyan short hair, wearing hoodie and glasses,
accessory: glasses,
idle animation (4 frames), walking (8 frames), working (4 frames), drunk (2 frames),
transparent background, 16-bit RPG style, cyan and blue color scheme
```

### 昊（男生，黄色）
```
Pixel art character sprite sheet, 64x64 pixels per frame,
cute anime boy with blonde messy hair, wearing t-shirt and jeans,
accessory: watch,
idle animation (4 frames), walking (8 frames), working (4 frames), drunk (2 frames),
transparent background, 16-bit RPG style, yellow and orange color scheme
```

### 竹（女生，浅绿）
```
Pixel art character sprite sheet, 64x64 pixels per frame,
cute anime girl with light green long hair, wearing dress,
accessory: ribbon,
idle animation (4 frames), walking (8 frames), working (4 frames), drunk (2 frames),
transparent background, 16-bit RPG style, light green and white color scheme
```

### 东（女生，粉色）
```
Pixel art character sprite sheet, 64x64 pixels per frame,
cute anime girl with pink twin tails, wearing cute outfit,
accessory: hair clip,
idle animation (4 frames), walking (8 frames), working (4 frames), drunk (2 frames),
transparent background, 16-bit RPG style, pink and white color scheme
```

### 千（女生，紫色）
```
Pixel art character sprite sheet, 64x64 pixels per frame,
cute anime girl with purple long hair, wearing modern clothes,
accessory: earrings,
idle animation (4 frames), walking (8 frames), working (4 frames), drunk (2 frames),
transparent background, 16-bit RPG style, purple and blue color scheme
```

---

## 🔧 在线编辑工具

### Piskel (推荐)
1. 访问 https://www.piskelapp.com/
2. 创建新项目：64x64
3. 绘制角色
4. 创建动画帧（复制+微调）
5. 导出 PNG

### Aseprite (专业版)
- 付费 $20
- 功能强大
- 支持图层

---

## 📁 文件放置规则

生成后的文件放到：
```
frontend/assets/skins/characters/
├── 初.png   (或者 chu.png)
├── 博.png   (或者 bo.png)
├── 昊.png   (或者 hao.png)
├── 竹.png   (或者 zhu.png)
├── 东.png   (或者 dong.png)
└── 千.png   (或者 qian.png)
```

文件格式：PNG（透明背景）
尺寸：至少 64x64 像素

---

## 🎭 支持皮肤切换系统

### 配置文件结构
```json
{
  "skins": [
    {
      "id": "default",
      "name": "默认",
      "files": {
        "chu": "assets/skins/characters/初.png",
        "bo": "assets/skins/characters/博.png",
        ...
      }
    },
    {
      "id": "christmas",
      "name": "圣诞节",
      "files": {
        "chu": "assets/skins/christmas/初.png",
        ...
      }
    }
  ]
}
```

### 切换逻辑
- 用户点击"换装"
- 选择新皮肤
- 更新 `Character.skinId`
- 重新加载纹理
- 播放对应动画

---

## ⚡ 快速测试方案

如果暂时没有生成的图片，可以：
1. 使用现有占位符（已实现）
2. 使用 Emoji 作为临时头像
3. 使用免费像素画素材库

---

## 📞 需要帮助？

如果生成过程中遇到问题：
1. 检查图片格式（必须是 PNG）
2. 检查尺寸（至少 64x64）
3. 检查透明背景
4. 确保文件名正确
