#!/usr/bin/env python3
"""
创建更精细的像素风角色占位符
使用 PIL 库生成 PNG 图片
"""

from PIL import Image, ImageDraw
import os
import random

def hex_to_rgb(hex_color):
    """转换十六进制颜色为 RGB"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_character(char_name, char_config, output_path):
    """创建像素风角色"""
    size = 64
    
    # 创建图片（透明背景）
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    color = char_config['color']
    gender = char_config['gender']
    
    # 解析颜色
    rgb_color = hex_to_rgb(color)
    
    # 绘制角色主体
    body_color = (rgb_color[0], rgb_color[1], rgb_color[2], 230)
    
    # 身体（圆形）
    draw.ellipse([8, 8, 56, 56], fill=body_color, outline=(0, 0, 0, 255))
    
    # 根据性别和角色绘制细节
    if gender == 'male':
        # 男生发型
        if char_name == '初':
            # 红色头发
            draw.ellipse([10, 10, 54, 30], fill=(180, 50, 50, 255), outline=(0, 0, 0, 255))
            # 耳机
            draw.rectangle([8, 20, 14, 28], fill=(80, 80, 80, 200))
            draw.rectangle([50, 20, 56, 28], fill=(80, 80, 80, 200))
        elif char_name == '博':
            # 青色头发
            draw.ellipse([12, 12, 52, 28], fill=(78, 205, 196, 255), outline=(0, 0, 0, 255))
            # 眼镜
            draw.rectangle([18, 24, 46, 34], outline=(30, 30, 30, 255), width=2)
        elif char_name == '昊':
            # 金色头发
            draw.ellipse([10, 10, 54, 30], fill=(255, 230, 109, 255), outline=(0, 0, 0, 255))
            # 手表
            draw.ellipse([16, 44, 24, 52], fill=(150, 150, 150, 200), outline=(50, 50, 50, 255))
    else:
        # 女生发型
        if char_name == '竹':
            # 浅绿头发
            draw.ellipse([8, 8, 56, 56], fill=(149, 225, 211, 255), outline=(0, 0, 0, 255))
            # 蝴蝶结
            draw.ellipse([46, 12, 54, 20], fill=(255, 105, 180, 255))
        elif char_name == '东':
            # 粉色头发
            draw.ellipse([8, 8, 56, 56], fill=(243, 129, 129, 255), outline=(0, 0, 0, 255))
            # 双马尾
            draw.ellipse([4, 16, 12, 28], fill=(243, 129, 129, 255), outline=(0, 0, 0, 255))
            draw.ellipse([52, 16, 60, 28], fill=(243, 129, 129, 255), outline=(0, 0, 0, 255))
            # 发夹
            draw.ellipse([54, 14, 60, 22], fill=(255, 255, 0, 255))
        elif char_name == '千':
            # 紫色头发
            draw.ellipse([8, 8, 56, 56], fill=(170, 150, 218, 255), outline=(0, 0, 0, 255))
            # 耳环
            draw.ellipse([10, 28, 12, 32], fill=(255, 215, 0, 255))
            draw.ellipse([52, 28, 54, 32], fill=(255, 215, 0, 255))
    
    # 眼睛（左）
    draw.ellipse([22, 28, 28, 36], fill=(255, 255, 255, 255), outline=(0, 0, 0, 255))
    draw.ellipse([24, 30, 26, 34], fill=(0, 0, 0, 255))
    
    # 眼睛（右）
    draw.ellipse([36, 28, 42, 36], fill=(255, 255, 255, 255), outline=(0, 0, 0, 255))
    draw.ellipse([38, 30, 40, 34], fill=(0, 0, 0, 255))
    
    # 嘴巴（微笑）
    draw.ellipse([28, 40, 36, 48], fill=(255, 255, 255, 255), outline=(0, 0, 0, 255))
    draw.line([30, 42, 34, 42], fill=(0, 0, 0, 255))
    
    # 高光
    draw.ellipse([24, 30, 25, 31], fill=(255, 255, 255, 150))
    draw.ellipse([38, 30, 39, 31], fill=(255, 255, 255, 150))
    
    # 保存
    img.save(output_path)
    print(f"✅ 创建角色: {char_name} -> {output_path}")

def main():
    """创建所有角色"""
    characters = {
        '初': {'color': '#FF6B6B', 'gender': 'male'},
        '博': {'color': '#4ECDC4', 'gender': 'male'},
        '昊': {'color': '#FFE66D', 'gender': 'male'},
        '竹': {'color': '#95E1D3', 'gender': 'female'},
        '东': {'color': '#F38181', 'gender': 'female'},
        '千': {'color': '#AA96DA', 'gender': 'female'}
    }
    
    random.seed(42)  # 固定随机种子，确保结果一致
    
    output_dir = 'frontend/assets/skins/characters/'
    os.makedirs(output_dir, exist_ok=True)
    
    for char_name, char_config in characters.items():
        output_path = os.path.join(output_dir, f"{char_name}.png")
        create_character(char_name, char_config, output_path)
    
    print("\n✅ 所有角色创建完成！")
    print(f"📁 输出目录: {output_dir}")
    print("📝 文件列表:")
    for char_name in characters.keys():
        print(f"   - {char_name}.png")

if __name__ == '__main__':
    main()
