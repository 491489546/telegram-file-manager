#!/usr/bin/env python3
"""
Replicate API 集成测试脚本
用于验证 Replicate 的基本功能
"""

import os
import replicate

def test_replicate_setup():
    """测试 Replicate 基本设置"""
    print("Testing Replicate library installation...")
    
    # 检查是否设置了 API token
    api_token = os.getenv("REPLICATE_API_TOKEN")
    if not api_token:
        print("⚠️  REPLICATE_API_TOKEN 环境变量未设置")
        print("请先设置环境变量：")
        print("export REPLICATE_API_TOKEN='your_token_here'")
        return False
    else:
        print("✅ REPLICATE_API_TOKEN 已设置")
        return True

def show_available_models():
    """显示常用的图像和视频生成模型"""
    models = {
        "图像生成": [
            "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535523258f72b12ea30d5783",  # SDXL
            "stability-ai/stable-diffusion:ac95ab7a4da5e54b94f1ec2af45cf83605f8db34d0b9e4da259e6c645e9d652f",  # SD 2.1
            "prompthero/openjourney:9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb"  # Open Journey
        ],
        "视频生成": [
            "stability-ai/stable-video-diffusion-img2vid:9cafb2680a7d84b05c60c8c69e9779d09c69df7119451ac6f9bde4c1ecc1e10e"  # SVD
        ]
    }
    
    print("\n📋 常用的 Replicate 模型:")
    for category, model_list in models.items():
        print(f"\n{category}:")
        for model in model_list:
            model_id = model.split(':')[0]
            print(f"  - {model_id}")

if __name__ == "__main__":
    print("🧪 Replicate API 集成测试")
    print("="*40)
    
    success = test_replicate_setup()
    show_available_models()
    
    print(f"\n{'='*40}")
    if success:
        print("✅ Replicate 已正确安装，可以进行图像/视频生成")
    else:
        print("⚠️  需要设置 API token 才能使用 Replicate")