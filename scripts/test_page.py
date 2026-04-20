#!/usr/bin/env python3
"""
网页自动化测试脚本
检查页面是否能正常加载
"""

import requests
import sys
import subprocess

def test_page(url):
    """测试页面是否可访问"""
    try:
        print(f"🌐 正在测试: {url}")
        
        # 获取页面内容
        response = requests.get(url, timeout=10)
        print(f"✅ HTTP 状态: {response.status_code}")
        
        if response.status_code != 200:
            print(f"❌ HTTP 错误: {response.status_code}")
            return False
        
        # 检查关键内容
        content = response.text
        if '402 虚拟生活社区' in content:
            print("✅ 标题正确")
        else:
            print("❌ 缺少标题")
            return False
        
        if 'Octopath Traveler' in content:
            print("✅ 风格正确")
        else:
            print("⚠️ 风格标注可能缺失")
        
        # 检查是否有 JavaScript 错误的迹象
        if 'phaser' in content.lower():
            print("✅ Phaser 已包含")
        else:
            print("❌ 缺少 Phaser")
        
        # 检查角色资源
        if 'assets/skins/characters' in content:
            print("✅ 角色路径正确")
        else:
            print("⚠️ 角色路径可能有问题")
        
        return True
        
    except requests.exceptions.Timeout:
        print("❌ 请求超时")
        return False
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        return False

def test_api():
    """测试 API 端点"""
    api_endpoints = [
        'http://localhost:8101/',
        'http://localhost:8101/api/members',
        'http://localhost:8101/health'
    ]
    
    print("\n🔍 测试 API 端点...")
    for url in api_endpoints:
        try:
            response = requests.get(url, timeout=5)
            print(f"✅ {url}: {response.status_code}")
        except Exception as e:
            print(f"❌ {url}: {e}")

def main():
    """主函数"""
    url = 'http://localhost:8101/'
    
    print("=" * 50)
    print("📱 402 虚拟生活社区系统 - 自动化测试")
    print("=" * 50)
    
    # 测试主页面
    if test_page(url):
        print("\n✅ 主页面测试通过")
    else:
        print("\n❌ 主页面测试失败")
        return
    
    # 测试 API
    test_api()
    
    print("\n" + "=" * 50)
    print("🎯 建议：")
    print("1. 如果测试通过，手动打开浏览器确认")
    print("2. 按 F12 打开开发者工具查看 Console")
    print("3. 检查是否有 JavaScript 错误")
    print("4. 测试点击角色是否能交互")
    print("=" * 50)

if __name__ == '__main__':
    main()
