#!/usr/bin/env python3
"""用户识别路由"""
from flask import request, jsonify
import hashlib
import json
import os

def get_client_id():
    """获取客户端唯一标识"""
    # 优先使用 Cookie
    user_id = request.cookies.get('user_id')
    if user_id:
        return user_id
    
    # 降级使用 IP + User-Agent 模拟
    ip = request.remote_addr
    ua = request.headers.get('User-Agent', '')
    return hashlib.md5(f"{ip}{ua}".encode()).hexdigest()[:8]

def load_members():
    """加载成员数据"""
    members_file = os.path.join(os.path.dirname(__file__), '..', '..', 'members.json')
    with open(members_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def init_identify_routes(app):
    """初始化用户识别路由"""
    
    @app.route('/api/identify', methods=['POST'])
    def identify():
        """识别用户身份"""
        client_id = get_client_id()
        members = load_members()
        
        # 简单映射：根据 client_id 最后一位分配用户
        # 实际应用中应该让用户选择或记住上次选择
        last_char = ord(client_id[-1]) % len(members)
        member = members[last_char]
        
        response = jsonify({
            "clientId": client_id,
            "userId": member['id'],
            "userName": member['name']
        })
        
        # 设置 Cookie（有效期 30 天）
        response.set_cookie('user_id', client_id, max_age=30*24*3600)
        return response
    
    @app.route('/api/members', methods=['GET'])
    def get_members():
        """获取所有成员列表"""
        members = load_members()
        return jsonify(members)
    
    @app.route('/api/members/<user_id>', methods=['GET'])
    def get_member(user_id):
        """获取单个成员信息"""
        members = load_members()
        member = next((m for m in members if m['id'] == user_id), None)
        if member:
            return jsonify(member)
        return jsonify({"error": "Member not found"}), 404
