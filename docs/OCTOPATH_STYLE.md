# 八方旅人风格角色配置

## 角色设计参考

### 八方旅人美术特点
- **HD-2D 立绘风格**：非像素风，是精致的手绘风格
- **大头比例**：头身比 1:2 或 1:3
- **丰富细节**：复杂的发型、服装、配饰
- **阴影和高光**：立体感强
- **水彩渲染**：场景使用水彩效果

## 6 位角色设计

### 男生角色

#### 初 - 武士/战士
- **风格**：热血战士
- **配色**：
  - 头发：橙红色 (#E74C3C)
  - 皮肤：健康肤色 (#FFE4C4)
  - 盔甲：深红色 + 金色装饰 (#8B0000 + #FFD700)
  - 武器：大剑
- **特征**：
  - 红色短发，竖起
  - 坚毅的表情
  - 金边铠甲
  - 配剑在腰间

#### 博 - 学者/法师
- **风格**：冷静智者
- **配色**：
  - 头发：青蓝色 (#3498DB)
  - 皮肤：苍白 (#FFE4C4)
  - 长袍：深蓝色 + 星空图案 (#1A237E + #87CEEB)
  - 眼镜：金丝眼镜
- **特征**：
  - 蓝色长发（扎起）
  - 眼镜
  - 书卷抱在怀里
  - 魔法阵法环绕

#### 昊 - 商人/盗贼
- **风格**：开朗阳光
- **配色**：
  - 头发：金色 (#FFD700)
  - 皮肤：健康肤色 (#FFE4C4)
  - 服装：橙色 + 白色 (#FFA500 + #FFFFFF)
  - 配饰：钱袋
- **特征**：
  - 金色短发，微卷
  - 开朗的笑容
  - 商人服装
  - 背着大钱袋

### 女生角色

#### 竹 - 舞者/吟游诗人
- **风格**：优雅温柔
- **配色**：
  - 头发：浅绿色 (#90EE90)
  - 皮肤：白皙肤色 (#FFF0F5)
  - 裙子：绿色 + 白层叠 (#228B22 + #F0FFF0)
  - 乐器：竖琴
- **特征**：
  - 浅绿长发，编发
  - 温柔的表情
  - 飘动的裙子
  - 手持竖琴

#### 东 - 神官/修女
- **风格**：可爱治愈
- **配色**：
  - 头发：粉色 (#FF69B4)
  - 皮肤：白皙肤色 (#FFF0F5)
  - 神官服：白色 + 粉色边 (#FFFFFF + #FFB6C1)
  - 权杖：金色
- **特征**：
  - 粉色双马尾
  - 天真的表情
  - 白色神官服
  - 手持金色权杖

#### 千 - 魔术师/女巫
- **风格**：神秘优雅
- **配色**：
  - 头发：紫色 (#9370DB)
  - 皮肤：苍白肤色 (#FFE4E1)
  - 法袍：深紫色 + 星空图案 (#4B0082 + #E6E6FA)
  - 魔法书
- **特征**：
  - 紫色长发，直发
  - 神秘的表情
  - 深紫色法袍
  - 漂浮魔法粒子

## 场景风格

### 主房间场景
- **水彩渲染背景**
- **木质地板**：暖棕色 (#DEB887)
- **墙壁**：米黄色 (#F5F5DC)
- **窗户**：透过阳光
- **家具**：木质家具 + 织物
- **光影**：柔和的光影效果

## 颜色方案

### 整体色调
- **主色**：暖色调
- **辅助色**：木色、米色
- **点缀色**：金色、银色
- **阴影**：柔和的灰色

### 八方旅人配色参考
- **背景**：#FFF8DC（玉米丝色）
- **地面**：#DEB887（秘鲁色）
- **UI边框**：#8B4513（鞍褐色）
- **高光**：#FFE4B5（鹿皮色）

## 文件组织

```
frontend/assets/
├── characters/
│   ├── 初.png (HD-2D 立绘，256x256)
│   ├── 博.png
│   ├── 昊.png
│   ├── 竹.png
│   ├── 东.png
│   └── 千.png
├── backgrounds/
│   └── room.png (水彩渲染背景，1024x768)
└── ui/
    ├── frame.png (UI 边框)
    └── icons.png (图标)
```

## 技术实现

### 图片规格
- **角色**：256x256 或 512x512
- **格式**：PNG（透明背景）
- **风格**：HD-2D 立绘
- **背景**：1024x768 或 1920x1080

### Phaser 配置调整
```javascript
const config = {
    pixelArt: false,  // 关闭像素风
    roundPixels: false,  // 关闭像素圆角
    antialias: true,  // 开启抗锯齿
    renderer: Phaser.WEBGL  // 使用 WebGL
};
```

## AI 生成提示词（更新版）

### 通用提示词模板
```
HD-2D anime character portrait, similar to Octopath Traveler style,
[角色描述],
chibi proportion (big head, small body),
detailed hand-drawn illustration,
rich colors and shading,
watercolor rendering style,
soft lighting,
elegant pose,
transparent background,
high quality, 512x512
```

### 具体角色提示词

**初**:
```
HD-2D anime warrior character portrait, Octopath Traveler style,
red hair, spiky style, determined expression,
wearing ornate red and gold armor,
big head, small body proportion,
detailed hand-drawn illustration,
rich red and gold colors,
soft lighting, elegant pose,
transparent background, 512x512
```

**博**:
```
Hd-2D anime scholar character portrait, Octopath Traveler style,
blue hair, tied back, intelligent expression,
wearing elegant dark blue robes with star patterns,
big head, small body proportion,
wearing gold-rimmed glasses,
holding a magic book,
detailed hand-drawn illustration,
rich blue and gold colors,
soft lighting, transparent background, 512x512
```

**竹**:
```
HD-2D anime dancer character portrait, Octopath Traveler style,
light green hair, braided, gentle expression,
wearing elegant green and white layered dress,
big head, small body proportion,
holding a harp,
detailed hand-drawn illustration,
rich green and white colors,
soft lighting, transparent background, 512x512
```
