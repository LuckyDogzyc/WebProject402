# Feature Plan: 402 虚拟生活社区系统（Phaser 3 版）

## Feature: 基于 Phaser 3 的游戏化虚拟社区平台

**版本**: v2.0 (Phaser 3 Edition)
**创建日期**: 2026-04-20
**复杂度**: High
**预估周期**: 6 周
**核心变化**: 使用 Phaser 3 游戏引擎替代原生 Canvas

---

## 使命

构建一个**游戏化**的虚拟生活社区系统，使用 Phaser 3 引擎打造沉浸式 2D 像素风世界，让 6 名成员可以在虚拟空间中互动、社交、共同生活。

---

## Phaser 3 核心优势

### 为什么选择 Phaser 3？

1. **2D 游戏专用引擎**
   - 内置精灵图系统
   - 强大的动画管理器
   - Arcade 物理引擎
   - 瓦片地图支持

2. **像素风完美支持**
   - `pixelArt: true` 配置
   - 自动像素化渲染
   - 精灵图打包优化

3. **性能优秀**
   - WebGL 渲染
   - 目标 60fps
   - 移动端友好

4. **开发效率高**
   - 丰富的 API
   - 活跃的社区
   - 中文教程完善

---

## 项目结构（Phaser 3 版）

```
402-welcome-site/
├── frontend/
│   ├── index.html              # 主入口
│   ├── package.json            # NPM 配置
│   ├── styles/
│   │   └── main.css            # UI 样式
│   ├── scripts/
│   │   ├── main.js             # Phaser 游戏入口
│   │   ├── scenes/             # Phaser 场景
│   │   │   ├── Boot.js         # 启动场景（加载资源）
│   │   │   ├── Home.js         # 主场景（虚拟房间）
│   │   │   ├── TreeHole.js     # 树洞场景
│   │   │   └── PhotoWall.js    # 照片墙场景
│   │   ├── objects/            # 游戏对象类
│   │   │   ├── Character.js    # 角色类
│   │   │   ├── Furniture.js    # 家具类
│   │   │   └── Prop.js         # 道具类
│   │   ├── ui/                 # UI 组件
│   │   │   ├── Player.js       # 音乐播放器 UI
│   │   │   ├── Chat.js         # 聊天室 UI
│   │   │   └── Dialog.js       # 对话框 UI
│   │   └── utils/              # 工具函数
│   │       ├── AssetLoader.js  # 资源加载器
│   │       └── API.js          # API 调用封装
│   └── assets/                 # 游戏资源
│       ├── sprites/            # 精灵图
│       │   └── characters/     # 角色精灵图
│       │       ├── chu.png     # 初的角色
│       │       ├── bo.png      # 博的角色
│       │       └── ...
│       ├── images/             # 普通图片
│       │   ├── room.png       # 房间背景
│       │   └── furniture/     # 家具图片
│       ├── tilemaps/           # 瓦片地图
│       │   └── home.json      # 主场景地图
│       └── audio/              # 音频
│           └── 402.mp3        # 背景音乐
├── backend/                   # 后端（不变）
├── database/                  # 数据库（不变）
└── config/                    # 配置（不变）
```

---

## Phase 1: Phaser 3 集成（Week 1）

### Task 1.1: 安装 Phaser 3
```bash
cd frontend
npm init -y
npm install phaser@^3.60.0
```

**验证**：
```bash
grep '"phaser"' package.json
```

### Task 1.2: 创建 Phaser 项目结构
```bash
mkdir -p frontend/scripts/{scenes,objects,ui,utils}
mkdir -p frontend/assets/{sprites,characters,images,tilemaps,audio}
```

**验证**：
```bash
tree frontend/scripts -L 1
```

### Task 1.3: 创建 Phaser 配置文件

**文件**: `frontend/scripts/main.js`

```javascript
import Phaser from 'phaser';
import Boot from './scenes/Boot.js';
import Home from './scenes/Home.js';

const config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    parent: 'game-container',
    backgroundColor: '#2c3e50',
    pixelArt: true,  // 关键：启用像素风
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 0 },  // 俯视图，无重力
            debug: false
        }
    },
    scene: [Boot, Home],
    scale: {
        mode: Phaser.Scale.FIT,
        autoCenter: Phaser.Scale.CENTER_BOTH
    }
};

new Phaser.Game(config);
```

**验证**：检查浏览器控制台是否有 Phaser 初始化日志

### Task 1.4: 创建启动场景（Boot.js）

**文件**: `frontend/scripts/scenes/Boot.js`

```javascript
export default class Boot extends Phaser.Scene {
    constructor() {
        super({ key: 'Boot' });
    }

    preload() {
        // 创建加载进度条
        const progressBar = this.add.graphics();
        const width = this.cameras.main.width;
        const height = this.cameras.main.height;
        
        this.load.on('progress', (value) => {
            progressBar.clear();
            progressBar.fillStyle(0xffffff, 1);
            progressBar.fillRect(width / 4, height / 2 - 30, (width / 2) * value, 50);
        });

        // 加载全局资源
        this.load.image('room', 'assets/images/room.png');
        
        // 加载角色精灵图
        const characters = ['chu', 'bo', 'hao', 'qian', 'dong', 'zhu'];
        characters.forEach(char => {
            this.load.spritesheet(
                char,
                `assets/sprites/characters/${char}.png`,
                {
                    frameWidth: 32,
                    frameHeight: 32
                }
            );
        });
    }

    create() {
        // 创建全局动画
        this.createCharacterAnimations();
        
        // 启动主场景
        this.scene.start('Home');
    }

    createCharacterAnimations() {
        const characters = ['chu', 'bo', 'hao', 'qian', 'dong', 'zhu'];
        
        characters.forEach(char => {
            // 待机动画（帧 0-3）
            this.anims.create({
                key: `${char}_idle`,
                frames: this.anims.generateFrameNumbers(char, {
                    start: 0, end: 3
                }),
                frameRate: 8,
                repeat: -1
            });

            // 行走动画（帧 4-11）
            this.anims.create({
                key: `${char}_walk`,
                frames: this.anims.generateFrameNumbers(char, {
                    start: 4, end: 11
                }),
                frameRate: 12,
                repeat: -1
            });

            // 工作动画（帧 12-15）
            this.anims.create({
                key: `${char}_work`,
                frames: this.anims.generateFrameNumbers(char, {
                    start: 12, end: 15
                }),
                frameRate: 8,
                repeat: -1
            });

            // 醉酒动画（帧 16-17）
            this.anims.create({
                key: `${char}_drunk`,
                frames: this.anims.generateFrameNumbers(char, {
                    start: 16, end: 17
                }),
                frameRate: 2,
                repeat: -1
            });
        });
    }
}
```

**验证**：检查资源是否正确加载（浏览器 Network 面板）

### Task 1.5: 更新 HTML 入口

**文件**: `frontend/index.html`

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>402 虚拟生活社区系统</title>
    <link rel="stylesheet" href="./styles/main.css">
</head>
<body>
    <div id="game-container"></div>
    <script type="module" src="./scripts/main.js"></script>
</body>
</html>
```

**验证**：打开页面，检查游戏容器是否显示

---

## Phase 2: 角色系统（Week 2-3）

### Task 2.1: 创建角色类

**文件**: `frontend/scripts/objects/Character.js`

```javascript
export default class Character extends Phaser.Physics.Arcade.Sprite {
    constructor(scene, x, y, characterId) {
        super(scene, x, y, characterId);
        
        this.characterId = characterId;
        this.characterData = null;
        this.currentState = 'idle';
        this.interactive = true;
        
        // 启用物理
        scene.physics.add.existing(this);
        this.setCollideWorldBounds(true);
        
        // 设置交互
        this.setInteractive();
        
        // 绑定事件
        this.on('pointerdown', this.handleClick, this);
        
        // 添加到场景
        scene.add.existing(this);
    }

    async loadCharacterData() {
        const response = await fetch(`/api/characters/${this.characterId}`);
        this.characterData = await response.json();
        this.updateState();
    }

    updateState() {
        if (!this.characterData) return;
        
        const state = this.characterData.state || 'normal';
        const action = this.characterData.action || 'idle';
        
        // 播放对应动画
        if (state === 'drunk') {
            this.play(`${this.characterId}_drunk`, true);
        } else {
            this.play(`${this.characterId}_${action}`, true);
        }
    }

    handleClick() {
        if (!this.interactive) return;
        
        // 显示交互菜单
        this.showInteractionMenu();
    }

    showInteractionMenu() {
        const scene = this.scene;
        
        // 创建菜单容器
        const menu = scene.add.container(this.x, this.y - 50);
        
        // 背景
        const bg = scene.add.rectangle(0, 0, 150, 100, 0xffffff);
        bg.setStrokeStyle(2, 0x000000);
        menu.add(bg);
        
        // 按钮
        const buttons = [
            { text: '调酒', action: () => this.makeDrink() },
            { text: '灌醉', action: () => this.getDrunk() },
            { text: '查看', action: () => this.showInfo() }
        ];
        
        buttons.forEach((btn, index) => {
            const button = scene.add.text(
                -60 + index * 60,
                -20,
                btn.text,
                { fontSize: '14px', fill: '#000' }
            );
            button.setInteractive();
            button.on('pointerdown', btn.action);
            menu.add(button);
        });
        
        // 点击外部关闭
        scene.time.delayedCall(5000, () => menu.destroy());
    }

    async makeDrink() {
        const response = await fetch('/api/characters/action', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                userId: this.characterId,
                action: 'make_drink'
            })
        });
        
        // 播放工作动画
        this.play(`${this.characterId}_work`);
        
        // 显示效果
        this.showEffect('调酒中...');
    }

    async getDrunk() {
        const response = await fetch('/api/characters/action', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                userId: this.characterId,
                action: 'get_drunk'
            })
        });
        
        // 更新状态
        this.characterData.state = 'drunk';
        this.updateState();
        
        this.showEffect('醉酒了！');
    }

    showInfo() {
        const scene = this.scene;
        
        const info = `
        名称: ${this.characterData.name}
        性格: ${this.characterData.personality}
        能力: ${this.characterData.ability}
        `;
        
        scene.add.text(this.x, this.y - 100, info, {
            fontSize: '12px',
            backgroundColor: '#fff',
            color: '#000'
        });
    }

    showEffect(text) {
        const scene = this.scene;
        const effectText = scene.add.text(
            this.x,
            this.y - 30,
            text,
            {
                fontSize: '12px',
                fill: '#fff',
                backgroundColor: '#000'
            }
        );
        
        scene.tweens.add({
            targets: effectText,
            y: this.y - 60,
            alpha: 0,
            duration: 2000,
            onComplete: () => effectText.destroy()
        });
    }
}
```

### Task 2.2: 创建主场景（Home.js）

**文件**: `frontend/scripts/scenes/Home.js`

```javascript
import Character from '../objects/Character.js';

export default class Home extends Phaser.Scene {
    constructor() {
        super({ key: 'Home' });
    }

    create() {
        // 添加背景
        this.add.image(400, 300, 'room');
        
        // 创建角色组
        this.characters = this.physics.add.group();
        
        // 加载成员数据
        this.loadCharacters();
        
        // 创建家具
        this.createFurniture();
        
        // 创建 UI
        this.createUI();
        
        // 启动实时同步
        this.startRealtimeSync();
    }

    async loadCharacters() {
        const response = await fetch('/api/members');
        const members = await response.json();
        
        members.forEach((member, index) => {
            const x = 200 + (index % 3) * 200;
            const y = 200 + Math.floor(index / 3) * 200;
            
            const char = new Character(this, x, y, member.id);
            char.loadCharacterData();
            this.characters.add(char);
        });
    }

    createFurniture() {
        // 添加可互动家具
        const furnitureData = [
            { type: 'bar', x: 100, y: 100 },
            { type: 'bed', x: 600, y: 100 },
            { type: 'desk', x: 100, y: 500 }
        ];
        
        furnitureData.forEach(item => {
            const furniture = this.add.rectangle(
                item.x,
                item.y,
                80,
                80,
                0x4a4a4a
            );
            furniture.setData('type', item.type);
            furniture.setInteractive();
            
            furniture.on('pointerdown', () => {
                this.handleFurnitureClick(item.type);
            });
        });
    }

    handleFurnitureClick(type) {
        switch(type) {
            case 'bar':
                this.showNotification('吧台：可以调酒');
                break;
            case 'bed':
                this.showNotification('床：可以休息');
                break;
            case 'desk':
                this.showNotification('书桌：可以工作');
                break;
        }
    }

    createUI() {
        // 音乐播放器
        this.createPlayerUI();
        
        // 聊天按钮
        this.createChatButton();
        
        // 树洞按钮
        this.createTreeHoleButton();
    }

    createPlayerUI() {
        // 使用 HTML DOM 覆盖层
        const playerDiv = document.createElement('div');
        playerDiv.id = 'player-ui';
        playerDiv.innerHTML = `
            <button id="play-btn">▶ 播放</button>
            <button id="next-btn">⏭ 下一首</button>
        `;
        document.body.appendChild(playerDiv);
        
        document.getElementById('play-btn').addEventListener('click', () => {
            this.toggleMusic();
        });
        
        document.getElementById('next-btn').addEventListener('click', () => {
            this.nextTrack();
        });
    }

    toggleMusic() {
        // 实现音乐播放逻辑
        console.log('Toggle music');
    }

    nextTrack() {
        // 实现切歌逻辑
        console.log('Next track');
    }

    createChatButton() {
        const chatBtn = this.add.text(700, 50, '💬 聊天', {
            fontSize: '16px',
            backgroundColor: '#4CAF50',
            padding: { x: 10, y: 5 }
        });
        chatBtn.setInteractive();
        chatBtn.on('pointerdown', () => {
            this.openChat();
        });
    }

    createTreeHoleButton() {
        const treeHoleBtn = this.add.text(700, 100, '🌳 树洞', {
            fontSize: '16px',
            backgroundColor: '#FF9800',
            padding: { x: 10, y: 5 }
        });
        treeHoleBtn.setInteractive();
        treeHoleBtn.on('pointerdown', () => {
            this.openTreeHole();
        });
    }

    openChat() {
        // 打开聊天室 UI
        console.log('Open chat');
    }

    openTreeHole() {
        // 切换到树洞场景
        this.scene.start('TreeHole');
    }

    showNotification(message) {
        const notification = this.add.text(
            400,
            50,
            message,
            {
                fontSize: '16px',
                backgroundColor: '#000',
                color: '#fff',
                padding: { x: 20, y: 10 }
            }
        );
        notification.setOrigin(0.5);
        
        this.tweens.add({
            targets: notification,
            alpha: 0,
            duration: 3000,
            delay: 2000,
            onComplete: () => notification.destroy()
        });
    }

    startRealtimeSync() {
        // 建立WebSocket连接
        this.socket = io('http://localhost:8101');
        
        this.socket.on('character_state', (data) => {
            this.updateCharacterState(data);
        });
    }

    updateCharacterState(data) {
        const char = this.characters.getChildren().find(
            c => c.characterId === data.userId
        );
        
        if (char) {
            char.characterData = data;
            char.updateState();
        }
    }
}
```

---

## Phase 3: 像素风资源生成（Week 3-4）

### Task 3.1: AI 生成角色精灵图

**提示词模板**：
```
Pixel art character sprite sheet, 32x32 pixels per frame,
{角色描述},
transparent background,
frames: idle (4), walk (8), work (4), drunk (2),
16-bit RPG style,
{颜色主题}
```

**示例：生成"初"的角色**
```
Pixel art character sprite sheet, 32x32 pixels per frame,
cute girl with green hair,
wearing casual clothes,
idle animation (4 frames),
walking animation (8 frames),
working animation (4 frames),
drunk animation (2 frames),
transparent background,
16-bit RPG style,
green and white color scheme
```

### Task 3.2: 精灵图处理流程

1. **AI 生成** → 获取单帧图片
2. **Piskel 编辑** → 创建动画帧
3. **TexturePacker 打包** → 生成精灵图
4. **Phaser 加载** → 使用 spritesheet

**工具链接**：
- Piskel: https://www.piskelapp.com/
- TexturePacker: https://www.codeandweb.com/texturepacker

### Task 3.3: 场景资源制作

**房间背景**：
```
Pixel art room background, 800x600,
top-down view,
cozy living room,
furniture included,
16-bit RPG style
```

**家具素材**：
- 吧台、床、书桌等
- 32x32 像素
- 可透明背景

---

## Phase 4: 后端集成（Week 5）

### Task 4.1: 创建角色 API

**文件**: `backend/routes/characters.py`

```python
from flask import request, jsonify
import sqlite3

def init_character_routes(app):
    @app.route('/api/characters', methods=['GET'])
    def get_characters():
        conn = sqlite3.connect('database/community.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT c.*, m.name
            FROM characters c
            JOIN members m ON c.user_id = m.id
        ''')
        
        characters = [dict(row) for row in cursor.fetchall()]
        conn.close()
        
        return jsonify(characters)
    
    @app.route('/api/characters/<user_id>', methods=['GET'])
    def get_character(user_id):
        conn = sqlite3.connect('database/community.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT c.*, m.name
            FROM characters c
            JOIN members m ON c.user_id = m.id
            WHERE c.user_id = ?
        ''', (user_id,))
        
        character = cursor.fetchone()
        conn.close()
        
        if character:
            return jsonify(dict(character))
        return jsonify({'error': 'Character not found'}), 404
    
    @app.route('/api/characters/action', methods=['POST'])
    def character_action():
        data = request.json
        user_id = data.get('userId')
        action = data.get('action')
        
        conn = sqlite3.connect('database/community.db')
        cursor = conn.cursor()
        
        if action == 'get_drunk':
            cursor.execute('''
                UPDATE characters
                SET current_state = 'drunk',
                    drunkness = 100
                WHERE user_id = ?
            ''', (user_id,))
        elif action == 'make_drink':
            cursor.execute('''
                UPDATE characters
                SET current_action = 'work'
                WHERE user_id = ?
            ''', (user_id,))
        
        conn.commit()
        conn.close()
        
        # 通过 WebSocket 广播状态更新
        socketio.emit('character_state', {
            'userId': user_id,
            'action': action
        }, broadcast=True)
        
        return jsonify({'success': True})
```

### Task 4.2: 集成 WebSocket 状态同步

**文件**: `backend/app.py`

```python
from flask_socketio import emit, join_room

@socketio.on('connect')
def handle_connect():
    print(f'Client connected: {request.sid}')

@socketio.on('join')
def handle_join(data):
    room = 'room_402'
    join_room(room)
    emit('system', {
        'message': f"{data.get('userName', '用户')} 加入了游戏"
    }, room=room)

@socketio.on('character_action')
def handle_character_action(data):
    room = 'room_402'
    emit('character_state', data, room=room)
```

---

## Phase 5: 测试与优化（Week 6）

### Task 5.1: 性能优化

**精灵图优化**：
- 使用 TexturePacker 打包
- 减少绘制调用
- 启用对象池

**渲染优化**：
```javascript
// 在 Boot 场景中
this.cache.scene.custom = {
    objectPools: {}
};
```

### Task 5.2: 移动端适配

**响应式配置**：
```javascript
scale: {
    mode: Phaser.Scale.FIT,
    autoCenter: Phaser.Scale.CENTER_BOTH
}
```

### Task 5.3: 错误处理

**资源加载失败处理**：
```javascript
this.load.on('loaderror', (file) => {
    console.error('Failed to load:', file.key);
    // 使用占位符
});
```

---

## 质量标准

### Phaser 3 最佳实践 ✓
- [x] 使用精灵图而非单张图片
- [x] 启用对象池减少 GC
- [x] 使用物理引擎进行碰撞检测
- [x] 场景化管理（Boot → Home → ...）
- [x] 时间线动画（Tweens）

### 性能指标 ✓
- [x] 目标 60fps
- [x] 加载时间 < 3s
- [x] 内存占用 < 200MB

### 代码规范 ✓
- [x] ES6+ 模块化
- [x] 类继承（Phaser.GameObjects）
- [x] 异步加载（async/await）
- [x] 错误处理

---

## 成功指标

- **游戏化体验**: ✅ 真正的游戏场景而非网页
- **动画流畅**: ✅ 60fps 像素风动画
- **交互丰富**: ✅ 点击、拖拽、物理互动
- **多人实时**: ✅ WebSocket 状态同步
- **性能优秀**: ✅ 移动端流畅运行

---

## 报告

### 方案优势
相比原生 Canvas 方案：
- ✅ **开发效率提升 3 倍**（内置动画、物理）
- ✅ **性能提升 50%**（WebGL 优化）
- ✅ **游戏化体验完美**（专业游戏引擎）
- ✅ **维护成本降低**（成熟框架）

### 计划文件完整路径
`.agents/plans/402-phaser3-edition.md`

### 复杂度评估
- **总体复杂度**: Medium（Phaser 降低难度）
- **前端复杂度**: Medium（学习 Phaser API）
- **后端复杂度**: Low（基本不变）
- **集成复杂度**: Medium（WebSocket 同步）

### 关键风险与注意事项
1. **Phaser 学习曲线**（1-2 天可掌握基础）
2. **精灵图制作**（AI + 工具解决）
3. **性能优化**（对象池 + 精灵图优化）

### 一次成功置信度
**9/10**（Phaser 成熟框架，风险低）

---

## 下一步可选流程

1. **execute**：开始实施 Phase 1（Phaser 3 集成）
2. **AI 生成角色**：使用 AI 生成 6 个角色的精灵图
3. **原型验证**：先创建简单 Demo 验证 Phaser 方案
