# Replicate 集成配置方案

## 当前系统状态
- 已有 openai-image-gen 技能（需要OpenAI API密钥）
- 已有 video-frames 技能（用于视频帧处理）
- 需要集成 Replicate API 以获得图像和视频生成能力

## 实施步骤

### 步骤 1: 获取 Replicate API Token
需要从 https://replicate.com/account 获取 API Token

### 步骤 2: 配置环境变量
```bash
export REPLICATE_API_TOKEN="your_replicate_token_here"
```

### 步骤 3: 创建 Replicate 技能配置
在 ~/.openclaw/workspace/skills/replicate 目录下创建技能文件

### 步骤 4: 安装必要依赖
```bash
pip3 install replicate  # 或者通过 uv 安装
```

### 步骤 5: 配置 OpenClaw 使用 Replicate
修改配置文件以添加 Replicate 作为模型提供商

## Replicate 集成脚本示例

```python
#!/usr/bin/env python3
"""
Replicate API 集成脚本
用于在 OpenClaw 中集成 Replicate 的图像和视频生成功能
"""

import os
import replicate
import asyncio
from typing import Dict, Any

class ReplicateIntegration:
    def __init__(self):
        self.api_token = os.getenv("REPLICATE_API_TOKEN")
        if not self.api_token:
            raise ValueError("REPLICATE_API_TOKEN 环境变量未设置")
        
        # 设置 API token
        os.environ["REPLICATE_API_TOKEN"] = self.api_token
    
    async def generate_image(self, prompt: str, model_version: str = "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535523258f72b12ea30d5783"):
        """生成图像"""
        try:
            output = await replicate.async_run(
                model_version,
                input={"prompt": prompt}
            )
            return output
        except Exception as e:
            print(f"图像生成失败: {str(e)}")
            return None
    
    async def generate_video(self, prompt: str, model_version: str = "stability-ai/stable-video-diffusion-img2vid:9cafb2680a7d84b05c60c8c69e9779d09c69df7119451ac6f9bde4c1ecc1e10e"):
        """生成视频"""
        try:
            output = await replicate.async_run(
                model_version,
                input={"prompt": prompt}
            )
            return output
        except Exception as e:
            print(f"视频生成失败: {str(e)}")
            return None

# 使用示例
async def main():
    replicator = ReplicateIntegration()
    
    # 生成图像
    image_result = await replicator.generate_image("一只可爱的猫在阳光下玩耍")
    if image_result:
        print(f"图像生成成功: {image_result}")
    
    # 生成视频
    video_result = await replicator.generate_video("一只猫在阳光下玩耍的短视频")
    if video_result:
        print(f"视频生成成功: {video_result}")

if __name__ == "__main__":
    asyncio.run(main())
```

## 配置文件示例 (添加到 openclaw.json)

```json
{
  "models": {
    "providers": {
      "replicate": {
        "baseUrl": "https://api.replicate.com/v1",
        "apiKey": "REPLICATE_API_TOKEN",  // 这将从环境变量获取
        "api": "replicate-api",
        "models": [
          {
            "id": "stability-ai/sdxl",
            "name": "Stable Diffusion XL",
            "input": ["text"],
            "output": ["image"],
            "contextWindow": 1024,
            "maxTokens": 1024
          },
          {
            "id": "stability-ai/stable-video-diffusion-img2vid",
            "name": "Stable Video Diffusion",
            "input": ["text"],
            "output": ["video"],
            "contextWindow": 1024,
            "maxTokens": 1024
          }
        ]
      }
    }
  }
}
```

## 实施建议
1. 先获取 Replicate API Token
2. 配置环境变量
3. 创建技能文件
4. 测试图像生成功能
5. 逐步扩展到视频生成功能