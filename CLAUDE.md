# CLAUDE.md - 402 虚拟生活社区系统

## 项目概览

**项目名称**：402 虚拟生活社区系统  
**项目类型**：游戏化虚拟社交网页平台  
**目标用户**：6 人固定团队（初、博、昊、千、东、竹）  
**核心目标**：构建融合虚拟角色、互动场景与轻量社交功能的"数字家园"

### 核心功能模块
1. **音乐播放系统**：内置 MP3 播放器，首曲《402》
2. **虚拟角色系统**：角色定制/换装/自动行为
3. **互动行为系统**：调酒/灌醉/备忘录/黑板
4. **树洞匿名系统**：情绪倾诉 + 画像绘制
5. **旅行地图与照片墙**：地点标记 + 图床存储
6. **内部聊天室**：实时通信

---

## 技术栈

### 前端
| 技术 | 版本 | 用途 |
|------|------|------|
| HTML5 | - | 页面结构 |
| CSS3 | - | 样式 + 动画（像素风） |
| JavaScript | ES6+ | 业务逻辑（无框架） |
| WebSocket API | - | 实时通信 |
| Canvas API | - | 像素画渲染 |

### 后端
| 技术 | 版本 | 用途 |
|------|------|------|
| Python | 3.12.3 | 后端语言 |
| Flask | 2.x | Web 框架 |
| SQLite | 3.x | 数据库 |
| Flask-SocketIO | - | WebSocket 支持 |
| SQLAlchemy | - | ORM（可选） |

### 基础设施
| 组件 | 说明 |
|------|------|
| 部署端口 | 8101 |
| 图床 | 腾讯云 COS |
| 版本控制 | Git + GitHub |

---

## 常用命令

### 开发环境启动
```bash
# 前端开发（静态服务器）
cd /root/.openclaw/workspace/402-welcome-site
python3 -m http.server 8101 --bind 0.0.0.0

# 后端开发（Flask 服务）
export FLASK_APP=backend/app.py
export FLASK_ENV=development
python3 -m flask run --host=0.0.0.0 --port=8101
```

### 依赖安装
```bash
# Python 依赖
pip install flask flask-socketio flask-cors sqlalchemy pillow eventlet

# 查看已安装依赖
pip list | grep -i flask
```

### 数据库操作
```bash
# 初始化数据库
sqlite3 database/community.db < database/schema.sql

# 查询数据
sqlite3 database/community.db "SELECT * FROM members;"

# 备份数据库
cp database/community.db database/community.db.backup
```

### Git 操作
```bash
# 查看状态
git status

# 提交变更
git add .
git commit -m "描述信息"
git push origin main

# 拉取最新
git pull origin main
```

### 验证与测试
```bash
# API 测试
curl http://localhost:8101/api/members
curl -X POST http://localhost:8101/api/identify -H "Content-Type: application/json"

# WebSocket 测试（浏览器控制台）
const socket = io('http://localhost:8101');
socket.on('connect', () => console.log('Connected'));
```

---

## 目录结构

```
402-welcome-site/
├── frontend/               # 前端资源
│   ├── index.html          # 主入口
│   ├── assets/             # 静态资源
│   │   ├── music/          # 音乐文件
│   │   ├── skins/          # 像素画皮肤
│   │   └── images/         # 其他图片
│   ├── styles/             # 样式文件
│   │   └── styles.css      # 全局样式
│   └── scripts/            # 前端脚本
│       ├── player.js       # 音乐播放器
│       ├── character.js    # 虚拟角色系统
│       ├── scene.js        # 生活场景渲染
│       ├── interaction.js  # 互动系统
│       ├── treehole.js     # 树洞系统
│       ├── map.js          # 旅行地图
│       └── chat.js         # 聊天室
├── backend/                # 后端服务
│   ├── app.py              # Flask 主应用
│   ├── models/             # 数据库模型
│   │   ├── __init__.py
│   │   ├── member.py
│   │   ├── character.py
│   │   └── treehole.py
│   ├── routes/             # API 路由
│   │   ├── identify.py     # 用户识别
│   │   ├── characters.py   # 角色状态
│   │   ├── treehole.py     # 树洞系统
│   │   └── locations.py    # 旅行地图
│   ├── services/           # 业务逻辑
│   │   └── behavior_engine.py  # 行为引擎
│   └── utils/              # 工具函数
│       ├── database.py     # 数据库连接
│       └── storage.py      # 腾讯云 COS
├── database/               # 数据库文件
│   ├── schema.sql          # 数据库结构
│   └── community.db        # SQLite 数据库
├── config/                 # 配置文件
│   └── config.json         # 系统配置
├── .agents/                # AI 代理配置
│   └── plans/              # 实施计划
│       └── 402-virtual-community-system.md
├── .claude/                # Claude AI 配置
│   ├── commands/           # Slash 命令
│   └── skills/             # 技能定义
├── index.html              # 当前欢迎页（待重构）
├── members.json            # 成员基础数据
├── PRD.md                  # 产品需求文档
├── README.md               # 项目说明
└── CLAUDE.md               # 本文件（开发规则）
```

---

## 代码模式

### 命名约定

#### 文件命名
- **前端文件**：`kebab-case`（如 `tree-hole.js`）
- **后端文件**：`snake_case`（如 `behavior_engine.py`）
- **组件文件**：`PascalCase`（如 `Character.js`，如使用组件化）

#### 变量命名
- **JavaScript**：`camelCase`（如 `currentUserId`）
- **Python**：`snake_case`（如 `current_user_id`）
- **常量**：`UPPER_SNAKE_CASE`（如 `MAX_UPLOAD_SIZE`）
- **类名**：`PascalCase`（如 `MusicPlayer`）

#### CSS 类名
- **BEM 风格**：`block__element--modifier`
- **工具类**：`kebab-case`（如 `.member-card`）

### 代码组织模式

#### 前端模块化
```javascript
// 推荐：ES6 模块
class MusicPlayer {
    constructor() {
        this.audio = new Audio();
        this.playlist = [];
    }
    
    play() {
        this.audio.play();
    }
}

// 导出
export default MusicPlayer;

// 导入
import MusicPlayer from './scripts/player.js';
```

#### 后端路由组织
```python
# 推荐：蓝图模式
from flask import Blueprint

treehole_bp = Blueprint('treehole', __name__)

@treehole_bp.route('/api/treehole', methods=['GET'])
def get_treehole():
    pass

# 在 app.py 中注册
from routes.treehole import treehole_bp
app.register_blueprint(treehole_bp)
```

#### 错误处理
```javascript
// 前端：try-catch + 用户友好提示
async function loadMembers() {
    try {
        const response = await fetch('./members.json');
        if (!response.ok) throw new Error('加载失败');
        return response.json();
    } catch (err) {
        console.error(err);
        showErrorToast('成员数据加载失败，请刷新重试');
    }
}
```

```python
# 后端：统一错误处理
from flask import jsonify

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500
```

### 数据验证模式

#### 前端输入验证
```javascript
function validateEmotionContent(content) {
    if (!content || content.trim().length === 0) {
        throw new Error('内容不能为空');
    }
    if (content.length > 500) {
        throw new Error('内容不能超过 500 字');
    }
    return content.trim();
}
```

#### 后端输入验证
```python
from bleach import clean

def sanitize_input(text):
    """防止 XSS 攻击"""
    return clean(text, tags=[], strip=True)

def validate_content(content):
    if not content or len(content) > 500:
        raise ValueError('Invalid content')
    return sanitize_input(content)
```

### API 设计模式

#### RESTful API
```
GET    /api/members          # 获取成员列表
GET    /api/members/:id      # 获取单个成员
POST   /api/treehole         # 发布情绪
GET    /api/treehole         # 获取情绪列表
DELETE /api/treehole/:id     # 删除情绪
```

#### WebSocket 事件
```javascript
// 客户端发送
socket.emit('chat', {
    userId: 'hao',
    content: '大家好',
    timestamp: Date.now()
});

// 服务端广播
socket.emit('chat', data);
```

---

## 关键文件

### 核心配置文件

#### `config/config.json`
```json
{
    "server": {
        "host": "0.0.0.0",
        "port": 8101,
        "debug": false
    },
    "database": {
        "path": "database/community.db"
    },
    "storage": {
        "provider": "tencent_cos",
        "bucket": "your-bucket-name",
        "region": "ap-guangzhou"
    },
    "members": {
        "ids": ["chu", "bo", "hao", "qian", "dong", "zhu"],
        "defaultRole": "402 成员"
    }
}
```

#### `members.json`
```json
[
    {
        "id": "chu",
        "name": "初",
        "role": "402 成员",
        "note": "欢迎回家"
    }
    // ... 其他成员
]
```

### 核心逻辑文件

#### `backend/app.py`
Flask 主应用入口，负责：
- 注册路由蓝图
- 配置 WebSocket
- 静态文件服务
- 错误处理

#### `frontend/scripts/player.js`
音乐播放器核心逻辑：
- 播放列表管理
- 播放/暂停/切歌
- 循环模式

#### `backend/services/behavior_engine.py`
角色行为引擎：
- 生成每日行为计划
- 定时更新角色状态
- WebSocket 状态推送

---

## 开发约定

### 前端开发约定
1. **无框架依赖**：使用 Vanilla JavaScript，避免引入重型框架
2. **渐进增强**：基础功能不依赖 JavaScript，增强功能使用 JS
3. **移动优先**：优先考虑移动端体验
4. **像素风设计**：所有视觉元素统一像素风格

### 后端开发约定
1. **轻量优先**：优先使用轻量级库（Flask vs Django）
2. **API 版本控制**：所有 API 以 `/api/v1/` 开头（预留版本号）
3. **错误日志**：所有错误必须记录日志
4. **数据库事务**：写操作必须在事务中执行

### Git 提交约定
```
feat: 新功能
fix: 修复 bug
docs: 文档更新
style: 代码格式调整
refactor: 重构
test: 测试相关
chore: 构建/工具相关

示例：
feat(player): 添加音乐播放器循环模式
fix(chat): 修复 WebSocket 断线重连问题
docs(readme): 更新部署文档
```

### 代码审查清单
- [ ] 代码符合命名约定
- [ ] 错误处理完善
- [ ] 无敏感信息泄露（API Key、密码）
- [ ] 注释清晰易懂
- [ ] 性能无明显问题
- [ ] 安全检查（XSS、CSRF、SQL 注入）

---

## 安全规范

### 前端安全
1. **XSS 防护**：所有用户输入必须过滤
   ```javascript
   const safe = DOMPurify.sanitize(userInput);
   ```
2. **CSP 策略**：设置 Content-Security-Policy 头
3. **HTTPS 强制**：生产环境强制使用 HTTPS

### 后端安全
1. **SQL 注入防护**：使用参数化查询
   ```python
   # 错误
   query = f"SELECT * FROM members WHERE id = {user_id}"
   # 正确
   query = "SELECT * FROM members WHERE id = ?", (user_id,)
   ```
2. **文件上传限制**：限制文件类型和大小
3. **速率限制**：API 调用频率限制

### 数据安全
1. **敏感数据加密**：聊天记录加密存储
2. **定期备份**：数据库每日备份
3. **访问控制**：6 人固定访问，无注册接口

---

## 性能优化

### 前端优化
1. **图片懒加载**：使用 IntersectionObserver
2. **代码分割**：按需加载 JavaScript 模块
3. **缓存策略**：合理使用 LocalStorage / SessionStorage

### 后端优化
1. **数据库索引**：为常用查询字段添加索引
2. **响应缓存**：API 响应缓存（Redis 可选）
3. **连接池**：数据库连接池管理

---

## 测试策略

### 前端测试
- **手动测试**：浏览器开发者工具
- **功能测试**：每个模块独立测试
- **兼容性测试**：Chrome / Firefox / Safari / Edge

### 后端测试
- **API 测试**：curl / Postman
- **数据库测试**：SQLite CLI 查询验证
- **集成测试**：前后端联调

---

## 部署流程

### 开发环境
```bash
export FLASK_ENV=development
python3 backend/app.py
```

### 生产环境
```bash
export FLASK_ENV=production
# 使用 systemd 服务
sudo systemctl start 402-community
sudo systemctl enable 402-community
```

### 验证部署
```bash
# 检查服务状态
curl http://localhost:8101/api/members

# 检查日志
sudo journalctl -u 402-community -f
```

---

## 故障排查

### 常见问题

#### 1. WebSocket 连接失败
**症状**：聊天室无法连接  
**排查**：
```bash
# 检查端口占用
lsof -i :8101

# 检查防火墙
sudo ufw status
```

#### 2. 图片上传失败
**症状**：腾讯云 COS 返回 403  
**排查**：
- 检查 COS 密钥配置
- 检查 Bucket 权限设置
- 查看后端日志

#### 3. 数据库锁定
**症状**：SQLite 数据库无法写入  
**排查**：
```bash
# 检查数据库文件权限
ls -la database/community.db

# 检查是否有锁定文件
ls -la database/community.db-shm
ls -la database/community.db-wal
```

---

## 扩展阅读

### 项目文档
- [PRD.md](./PRD.md) - 产品需求文档
- [.agents/plans/402-virtual-community-system.md](./agents/plans/402-virtual-community-system.md) - 实施计划
- [README.md](./README.md) - 项目说明

### 外部资源
- [Flask 官方文档](https://flask.palletsprojects.com/)
- [Flask-SocketIO 文档](https://flask-socketio.readthedocs.io/)
- [腾讯云 COS SDK](https://cloud.tencent.com/document/product/436/31747)
- [MDN Web API 文档](https://developer.mozilla.org/)

---

## 更新日志

- **2026-04-20**: 创建 CLAUDE.md，定义开发规则与约定
- **2026-04-20**: 完成项目规划，准备进入实施阶段

---

**维护者**：AI 助手（基于用户需求生成）  
**最后更新**：2026-04-20  
**状态**：活跃开发中
