#!/usr/bin/env python3
"""
创建 HD-2D 八方旅人风格的占位符角色（简化版）
"""

from PIL import Image, ImageDraw
import os
import random

def hex_to_rgb(hex_color):
    """转换十六进制颜色为 RGB"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_octopath_character(char_name, char_config, output_path):
    """创建八方旅人风格角色"""
    size = 256
    
    # 创建图片（透明背景）
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    color = char_config['color']
    gender = char_config['gender']
    
    rgb_color = hex_to_rgb(color)
    
    # 基础肤色
    skin_color = (255, 228, 196, 255)
    
    # 头部阴影
    for offset in range(8, 0, -1):
        alpha = 30 - offset * 3
        draw.ellipse([
            size//2 - 60 + offset, 
            size//2 - 60 + offset, 
            size//2 + 60 + offset, 
            size//2 + 60 + offset
        ], fill=(0, 0, 0, alpha))
    
    # 头部主体（大）
    draw.ellipse([size//2 - 70, size//2 - 70, size//2 + 70, size//2 + 70], 
                  fill=skin_color, outline=(0, 0, 0, 200))
    
    # 头发（根据角色）
    if gender == 'male':
        if char_name == '初':
            # 红色刺猬头
            draw.ellipse([size//2 - 65, size//2 - 75, size//2 + 65, size//2 + 10], 
                          fill=(180, 60, 60, 230), outline=(0, 0, 0, 200))
            # 刺
            for i in range(12):
                x = size//2 + random.randint(-30, 30)
                y = size//2 - 70 + random.randint(0, 20)
                draw.line([x, y, x, y+25], fill=(150, 50, 50, 180))
        elif char_name == '博':
            # 青色短发
            draw.ellipse([size//2 - 60, size//2 - 65, size//2 + 60, size//2 + 10], 
                          fill=(78, 205, 196, 230), outline=(0, 0, 0, 200))
            # 眼镜框
            draw.rectangle([size//2 - 22, size//2 - 5, size//2 + 22, size//2 + 8], 
                         outline=(40, 40, 40, 200), width=2)
            # 镜片
            draw.ellipse([size//2 - 18, size//2 - 2, size//2 + 18, size//2 + 6], 
                          fill=(135, 206, 250, 120))
        elif char_name == '昊':
            # 金色乱发
            draw.ellipse([size//2 - 62, size//2 - 68, size//2 + 62, size//2 + 8], 
                          fill=(255, 230, 109, 230), outline=(0, 0, 0, 200))
            # 凌乱发丝
            for i in range(15):
                x = random.randint(size//2 - 60, size//2 + 60)
                y = random.randint(size//2 - 68, size//2 - 50)
                draw.line([x, y, x+random.randint(-8, 8), y+random.randint(10, 25)], 
                        fill=(200, 180, 80, 150))
            # 手表（左手上）
            draw.ellipse([size//2 - 55, size//2 + 20, size//2 - 25, size//2 + 40], 
                          fill=(150, 150, 150, 200), outline=(80, 80, 80, 255))
    else:
        # 女生长发
        if char_name == '竹':
            # 浅绿长发
            draw.ellipse([size//2 - 70, size//2 - 70, size//2 + 70, size//2 + 90], 
                          fill=(149, 225, 211, 200), outline=(0, 0, 0, 200))
            # 蝴蝶结
            draw.ellipse([size//2 + 20, size//2 - 55, size//2 + 40, size//2 - 40], 
                          fill=(255, 105, 180, 255))
        elif char_name == '东':
            # 粉色双马尾
            draw.ellipse([size//2 - 72, size//2 - 60, size//2 - 48, size//2 + 35], 
                          fill=(243, 129, 129, 200), outline=(0, 0, 0, 200))
            draw.ellipse([size//2 + 48, size//2 - 60, size//2 + 72, size//2 + 35], 
                          fill=(243, 129, 129, 200), outline=(0, 0, 0, 200))
            # 发夹
            draw.ellipse([size//2 + 55, size//2 - 35, size//2 + 70, size//2 - 25], 
                          fill=(255, 255, 0, 255))
        elif char_name == '千':
            # 紫色长发
            draw.ellipse([size//2 - 75, size//2 - 75, size//2 + 75, size//2 + 90], 
                          fill=(170, 150, 218, 200), outline=(0, 0, 0, 200))
            # 耳环
            draw.ellipse([size//2 - 68, size//2 + 12, size//2 - 62, size//2 + 22], 
                          fill=(255, 215, 0, 255))
            draw.ellipse([size//2 + 62, size//2 + 12, size//2 + 68, size//2 + 22], 
                          fill=(255, 215, 0, 255))
    
    # 眼睛（大而详细）
    eye_width, eye_height = 20, 26
    
    # 左眼
    draw.ellipse([size//2 - 28, size//2 - 8, size//2 - 28 + eye_width, size//2 - 8 + eye_height], 
                  fill=(255, 255, 255, 255), outline=(0, 0, 0, 255))
    draw.ellipse([size//2 - 22, size//2, size//2 - 6, size//2 + 6], 
                  fill=(60, 60, 60, 230))
    draw.ellipse([size//2 - 18, size//2 + 2, size//2 - 14, size//2 + 3], 
                  fill=(20, 20, 20, 255))
    draw.ellipse([size//2 - 20, size//2 - 3, size//2 - 16, size//2], 
                  fill=(255, 255, 255, 180))
    
    # 右眼
    draw.ellipse([size//2 + 28 - eye_width, size//2 - 8, size//2 + 28, size//2 - 8 + eye_height], 
                  fill=(255, 255, 255, 255), outline=(0, 0, 0, 255))
    draw.ellipse([size//2 + 6, size//2, size//2 + 22, size//2 + 6], 
                  fill=(60, 60, 60, 230))
    draw.ellipse([size//2 + 14, size//2 + 2, size//2 + 18, size//2 + 3], 
                  fill=(20, 20, 20, 255))
    draw.ellipse([size//2 + 16, size//2 - 3, size//2 + 20, size//2], 
                  fill=(255, 255, 255, 180))
    
    # 腮红
    draw.ellipse([size//2 - 8, size//2 + 18, size//2 + 8, size//2 + 26], 
                  fill=(255, 200, 200, 100))
    
    # 嘴巴（微笑曲线）
    draw.ellipse([size//2 - 10, size//2 + 18, size//2 + 10, size//2 + 22], 
                  fill=(255, 255, 255, 255), outline=(0, 0, 0, 200), width=2)
    draw.line([size//2 - 6, size//2 + 22, size//2 + 6, size//2 + 22], 
               fill=(0, 0, 0, 255), width=2)
    
    # 服装/装饰
    if char_name == '初':
        # 战士铠甲
        draw.ellipse([size//2 - 68, size//2 + 35, size//2 + 68, size//2 + 75], 
                      fill=(180, 60, 60, 200), outline=(0, 0, 0, 255))
        # 金色边框
        draw.ellipse([size//2 - 60, size//2 + 38, size//2 + 60, size//2 + 70], 
                      outline=(255, 215, 0, 255), width=3)
    elif char_name == '竹':
        # 舞者裙子
        draw.ellipse([size//2 - 72, size//2 + 45, size//2 + 72, size//2 + 95], 
                      fill=(34, 139, 34, 200), outline=(0, 0, 0, 255))
        # 白色层叠
        draw.ellipse([size//2 - 62, size//2 + 48, size//2 + 62, size//2 + 88], 
                      fill=(240, 255, 240, 180), outline=(0, 0, 0, 255))
    
    # 外边框（角色主题色）
    padding = 6
    draw.rectangle([padding, padding, size-padding, size-padding], 
                   outline=(rgb_color[0], rgb_color[1], rgb_color[2], 255), width=4)
    
    # 内边框（金色）
    draw.rectangle([padding + 4, padding + 4, size - padding - 4, size - padding - 4], 
                   outline=(255, 215, 0, 200), width=2)
    
    # 保存
    img.save(output_path)
    print(f"✅ 创建 HD-2D 角色: {char_name} -> {output_path} (256x256)")
    
    return img

def main():
    """创建所有 HD-2D 角色"""
    characters = {
        '初': {'color': '#E74C3C', 'gender': 'male'},
        '博': {'color': '#3498DB', 'gender': 'male'},
        '昊': {'color': '#F39C12', 'gender': 'male'},
        '竹': {'color': '#90EE90', 'gender': 'female'},
        '东': {'color': '#FF69B4', 'gender': 'female'},
        '千': {'color': '#9B59B6', 'gender': 'female'}
    }
    
    random.seed(42)
    
    output_dir = 'frontend/assets/skins/characters/'
    os.makedirs(output_dir, exist_ok=True)
    
    print("🎨 开始创建 HD-2D 八方旅人风格角色...")
    print("📏 尺寸: 256x256 像素")
    print("🎭 风格: 模拟 HD-2D 立绘效果")
    print()
    
    for char_name, char_config in characters.items():
        output_path = os.path.join(output_dir, f"{char_name}.png")
        create_octopath_character(char_name, char_config, output_path)
    
    print("\n✅ 所有 HD-2D 角色创建完成！")
    print(f"📁 输出目录: {output_dir}")
    print("\n📝 文件列表:")
    for char_name in characters.keys():
        print(f"   - {char_name}.png (256x256, 八方旅人风格)")
    
    print("\n💡 这是算法生成的增强版占位符")
    print("   如需真正的 HD-2D 立绘，建议使用 AI 工具：")
    print("   - Bing Image Creator (免费)")
    print("   - docs/OCTOPATH_STYLE.md 中的提示词")

if __name__ == '__main__':
    main()
