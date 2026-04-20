#!/usr/bin/env python3
"""402 虚拟生活社区系统 - Flask 主应用"""
import os
import json
from flask import Flask, send_from_directory, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 创建 Flask 应用
# 注意：static_folder 路径相对于 backend/ 目录
import os
backend_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(backend_dir)

app = Flask(__name__, 
            static_folder=os.path.join(project_root, 'frontend'),
            static_url_path='')

# 配置
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['JSON_AS_ASCII'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# 启用 CORS
CORS(app)

# 创建 SocketIO 实例
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# 加载配置
config_path = os.path.join(project_root, 'config', 'config.json')
with open(config_path, 'r', encoding='utf-8') as f:
    config = json.load(f)

# 注册路由
from routes.identify import init_identify_routes
init_identify_routes(app)

# 静态文件服务
@app.route('/')
def index():
    """Phaser 游戏主页面"""
    return send_from_directory(os.path.join(project_root, 'frontend'), 'index.html')

@app.route('/<path:path>')
def static_files(path):
    """静态文件服务"""
    return send_from_directory(os.path.join(project_root, 'frontend'), path)

@app.route('/scripts/<path:path>')
def scripts_files(path):
    """JavaScript 模块支持"""
    return send_from_directory(os.path.join(project_root, 'frontend/scripts'), path)

@app.route('/health')
def health():
    """健康检查"""
    return jsonify({
        "status": "healthy",
        "service": "402 Virtual Community System",
        "version": "1.0.0"
    })

# WebSocket 事件
@socketio.on('connect')
def handle_connect():
    """客户端连接"""
    print(f'Client connected: {request.sid}')

@socketio.on('disconnect')
def handle_disconnect():
    """客户端断开"""
    print(f'Client disconnected: {request.sid}')

@socketio.on('join')
def handle_join(data):
    """加入房间"""
    room = 'room_402'
    from flask_socketio import join_room
    join_room(room)
    socketio.emit('system', {
        'message': f"{data.get('userName', '匿名用户')} 加入了聊天室"
    }, room=room)

# 启动应用
if __name__ == '__main__':
    host = config['server']['host']
    port = config['server']['port']
    debug = config['server'].get('debug', False)
    
    print(f"""
    ╔════════════════════════════════════════╗
    ║   402 虚拟生活社区系统启动中...       ║
    ╠════════════════════════════════════════╣
    ║  地址: http://{host}:{port}          ║
    ║  模式: {'开发模式' if debug else '生产模式'}              ║
    ╚════════════════════════════════════════╝
    """)
    
    socketio.run(app, host=host, port=port, debug=debug)
