# 像素风角色生成脚本
# 为每个角色生成更详细的像素画

import json
import base64

# 角色配置
characters = {
    'chu': {
        'name': '初',
        'gender': 'male',
        'color': '#FF6B6B',
        'style': 'energetic',
        'features': {
            'hair': 'red spiky',
            'clothes': 'casual t-shirt',
            'accessory': 'headphones'
        }
    },
    'bo': {
        'name': '博',
        'gender': 'male',
        'color': '#4ECDC4',
        'style': 'cool',
        'features': {
            'hair': 'cyan short',
            'clothes': 'hoodie',
            'accessory': 'glasses'
        }
    },
    'hao': {
        'name': '昊',
        'gender': 'male',
        'color': '#FFE66D',
        'style': 'friendly',
        'features': {
            'hair': 'blonde messy',
            'clothes': 't-shirt jeans',
            'accessory': 'watch'
        }
    },
    'zhu': {
        'name': '竹',
        'gender': 'female',
        'color': '#95E1D3',
        'style': 'gentle',
        'features': {
            'hair': 'light green long',
            'clothes': 'dress',
            'accessory': 'ribbon'
        }
    },
    'dong': {
        'name': '东',
        'gender': 'female',
        'color': '#F38181',
        'style': 'cute',
        'features': {
            'hair': 'pink twin tails',
            'clothes': 'cute outfit',
            'accessory': 'hair clip'
        }
    },
    'qian': {
        'name': '千',
        'gender': 'female',
        'color': '#AA96DA',
        'style': 'mysterious',
        'features': {
            'hair': 'purple long',
            'clothes': 'modern',
            'accessory': 'earrings'
        }
    }
}

# 生成 AI 提示词
def generate_prompt(character_id):
    char = characters[character_id]
    gender_text = "boy" if char['gender'] == 'male' else "girl"
    
    prompt = f"""Pixel art character sprite sheet, 64x64 pixels per frame,
cute anime {gender_text} with {char['features']['hair']}, wearing {char['features']['clothes']},
accessory: {char['features']['accessory']},
idle animation frames (4 frames),
walking animation frames (8 frames),
working animation frames (4 frames),
drunk animation frames (2 frames),
transparent background, 16-bit RPG style,
{char['color']} color scheme,
{char['style']} style,
high contrast, clear outlines"""
    
    return prompt

# 生成所有角色的提示词
for char_id in characters:
    print(f"\n## {char_id.upper()} - {characters[char_id]['name']}")
    print(f"性别: {'男' if characters[char_id]['gender'] == 'male' else '女'}")
    print(f"主题色: {characters[char_id]['color']}")
    print(f"风格: {characters[char_id]['style']}")
    print(f"\nAI 提示词:")
    print(generate_prompt(char_id))
    print("-" * 50)

# 输出配置文件
with open('frontend/assets/skins/characters-config.json', 'w', encoding='utf-8') as f:
    json.dump(characters, f, ensure_ascii=False, indent=2)

print("\n✅ 配置文件已生成: frontend/assets/skins/characters-config.json")
print("✅ 请复制上述提示词到 AI 图像生成工具")
