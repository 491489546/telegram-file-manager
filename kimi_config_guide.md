# Kimi 2.5 模型配置指南

## 重要说明
Kimi 2.5 并不是通过 OpenAI 兼容 API 运行的模型，而是有自己的 API 接口。要配置 Kimi 模型，需要以下步骤：

## 步骤 1: 获取 Kimi API 密钥
1. 访问 https://www.kimi.com/code/console?from=kfc_overview_topbar
2. 注册账户并获取 API 密钥

## 步骤 2: 配置 OpenClaw 使用 Kimi 模型
有两种方式可以配置：

### 方式一：通过 OpenClaw 配置命令（推荐）
```bash
# 配置 Kimi 作为模型提供商
openclaw config patch --json '{"models":{"providers":{"kimi":{"baseUrl":"https://api.kimi.com/v1","apiKey":"YOUR_KIMI_API_KEY","api":"openai-completions","models":[{"id":"kimi-2.5","name":"Kimi 2.5","input":["text"],"cost":{"input":0,"output":0},"contextWindow":32768,"maxTokens":8192}]}}}}'

# 设置 Kimi 为默认模型
openclaw config patch --json '{"agents":{"defaults":{"model":{"primary":"kimi/kimi-2.5"}}}}'
```

### 方式二：直接编辑配置文件
1. 编辑配置文件：
```bash
nano ~/.openclaw/openclaw.json
```

2. 在配置文件中添加 Kimi 模型提供商：
```json
{
  "models": {
    "providers": {
      "qwen-portal": {
        // 原有配置保持不变
      },
      "kimi": {
        "baseUrl": "https://api.kimi.com/v1",
        "apiKey": "YOUR_KIMI_API_KEY",
        "api": "openai-completions",
        "models": [
          {
            "id": "kimi-2.5",
            "name": "Kimi 2.5",
            "input": [
              "text"
            ],
            "cost": {
              "input": 0,
              "output": 0
            },
            "contextWindow": 32768,
            "maxTokens": 8192
          }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "kimi/kimi-2.5"
      }
    }
  }
}
```

## 步骤 3: 重启 OpenClaw 服务
```bash
openclaw config apply
```

## 注意事项
1. 需要有效的 Kimi API 密钥才能使用
2. Kimi 2.5 模型可能需要付费使用
3. 配置后会替换当前的 Qwen 模型作为主要模型
4. 建议先备份现有配置文件

## 验证配置
配置完成后，可以通过简单的对话测试 Kimi 模型是否正常工作。