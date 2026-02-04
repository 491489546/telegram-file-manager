# OpenClaw 更换模型操作指南

## 当前模型配置
目前你的 OpenClaw 使用的是 Qwen 模型，配置如下：
- 提供商：qwen-portal
- 主要模型：qwen-portal/coder-model
- API 类型：openai-completions

## 更换模型的步骤

### 方法一：通过配置文件直接编辑
1. 备份当前配置文件
```
cp /home/ubuntu/.openclaw/openclaw.json /home/ubuntu/.openclaw/openclaw.json.backup
```

2. 添加新的模型提供商（以OpenRouter为例）
```json
"models": {
  "providers": {
    "qwen-portal": {
      // 原有配置保持不变
    },
    "openrouter": {
      "baseUrl": "https://openrouter.ai/api/v1",
      "apiKey": "YOUR_OPENROUTER_API_KEY",
      "api": "openai-completions",
      "models": [
        {
          "id": "nvidia/nemotron-3-nano-30b-a3b:free",
          "name": "NVIDIA: Nemotron 3 Nano 30B A3B",
          "reasoning": false,
          "input": [
            "text"
          ],
          "cost": {
            "input": 0,
            "output": 0,
            "cacheRead": 0,
            "cacheWrite": 0
          },
          "contextWindow": 4096,
          "maxTokens": 4096
        }
      ]
    }
  }
}
```

3. 修改默认模型
```json
"agents": {
  "defaults": {
    "model": {
      "primary": "openrouter/nvidia/nemotron-3-nano-30b-a3b:free"
    },
    // 其他配置...
  }
}
```

### 方法二：通用OpenAI兼容模型模板
如果你想接入任何兼容OpenAI协议的模型，可以使用以下通用模板：

```json
{
  "provider": "custom-openai",
  "baseUrl": "YOUR_MODEL_ENDPOINT_URL",
  "apiKey": "YOUR_API_KEY",
  "api": "openai-completions",
  "models": [
    {
      "id": "your-model-id",
      "name": "Your Custom Model Name",
      "reasoning": false,
      "input": [
        "text"
      ],
      "cost": {
        "input": 0,
        "output": 0,
        "cacheRead": 0,
        "cacheWrite": 0
      },
      "contextWindow": 4096,
      "maxTokens": 4096
    }
  ]
}
```

### 方法三：常见的OpenAI兼容模型提供商示例

#### 1. OpenRouter 示例
```json
"openrouter": {
  "baseUrl": "https://openrouter.ai/api/v1",
  "apiKey": "YOUR_API_KEY",
  "api": "openai-completions",
  "models": [
    {
      "id": "microsoft/wizardlm-2-8x22b",
      "name": "WizardLM 2 8x22B",
      "input": ["text"]
    }
  ]
}
```

#### 2. Ollama 本地模型示例
```json
"ollama": {
  "baseUrl": "http://localhost:11434/v1",
  "apiKey": "ollama",
  "api": "openai-completions",
  "models": [
    {
      "id": "llama3.1",
      "name": "Llama 3.1",
      "input": ["text"]
    }
  ]
}
```

#### 3. Groq 示例
```json
"groq": {
  "baseUrl": "https://api.groq.com/openai/v1",
  "apiKey": "YOUR_GROQ_API_KEY",
  "api": "openai-completions",
  "models": [
    {
      "id": "llama3-70b-8192",
      "name": "Llama 3 70B",
      "input": ["text"]
    }
  ]
}
```

## 更换模型后重启服务
编辑完配置文件后，需要重启 OpenClaw 服务：

```bash
openclaw gateway stop
openclaw gateway start
```

或者使用配置应用命令：
```bash
openclaw config apply
```

## 注意事项
1. 替换 YOUR_API_KEY 为你实际的API密钥
2. 替换 YOUR_MODEL_ENDPOINT_URL 为实际的模型端点URL
3. 模型ID需要与提供商的文档保持一致
4. 建议先备份配置文件再进行修改
5. 更换模型后测试功能是否正常

## 验证新模型是否生效
更换模型后，可以通过以下方式验证：
1. 查看日志输出
2. 发送一条消息测试响应
3. 检查模型是否按预期工作