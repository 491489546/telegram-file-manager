# Replicate API 配置指南

## Replicate API 概述
Replicate 是一个可以让您在云端运行开源机器学习模型的平台，无需本地 GPU 即可使用强大的 AI 图像和视频生成能力。

## 获取 Replicate API 密钥
1. 访问 https://replicate.com/
2. 注册账户
3. 在 "Account settings" 的 "API tokens" 选项卡中获取 API Key

## 在 OpenClaw 中配置 Replicate

### 方法 1: 创建自定义技能
由于 OpenClaw 支持 MCP (Model Context Protocol) 和自定义技能，我们可以创建一个 Replicate 技能：

1. 首先需要创建一个新的技能目录：
```bash
mkdir -p ~/.openclaw/workspace/skills/replicate
cd ~/.openclaw/workspace/skills/replicate
```

2. 创建 SKILL.md 文件：
```markdown
---
name: replicate
description: 使用 Replicate API 进行图像和视频生成
homepage: https://replicate.com
metadata:
  {
    "openclaw":
      {
        "emoji": "🖼️",
        "requires": { "env": ["REPLICATE_API_TOKEN"] },
        "primaryEnv": "REPLICATE_API_TOKEN"
      }
  }
---

# Replicate 图像/视频生成技能

通过 Replicate API 生成图像和视频内容。

## 环境变量
- `REPLICATE_API_TOKEN`: 从 Replicate 账户获取的 API 密钥

## 使用方式
- 通过 OpenClaw 调用 Replicate 模型进行图像/视频生成
- 支持多种流行的 AI 生成模型
```

### 方法 2: 配置自定义模型提供商
在 OpenClaw 配置中添加 Replicate 作为模型提供商：

```json
{
  "models": {
    "providers": {
      "replicate": {
        "baseUrl": "https://api.replicate.com/v1",
        "apiKey": "YOUR_REPLICATE_API_TOKEN",
        "api": "openai-completions",
        "models": [
          {
            "id": "stability-ai/sdxl",
            "name": "Stable Diffusion XL",
            "input": ["text"],
            "output": ["image"]
          }
        ]
      }
    }
  }
}
```

### 方法 3: 使用现有技能
检查是否有现成的 Replicate 相关技能可以安装：

```bash
openclaw skills list
openclaw skills search replicate
```

## 常用 Replicate 模型示例
- `stability-ai/sdxl`: Stable Diffusion XL 图像生成
- `stability-ai/stable-video-diffusion`: 视频生成
- `meta/llama-2-70b-chat`: Llama 2 大语言模型
- `prompthero/openjourney`: Open Journey 图像生成

## 安全注意事项
1. API 密钥应妥善保管，不要泄露
2. 建议设置 API 调用限制以控制成本
3. 定期检查 API 使用情况和账单

## 配置步骤总结
1. 获取 Replicate API 密钥
2. 选择合适的集成方式（自定义技能或模型提供商）
3. 配置环境变量或配置文件
4. 重启 OpenClaw 服务
5. 测试图像/视频生成功能