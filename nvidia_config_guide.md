# NVIDIA NIM API 配置指南

## 重要说明
根据搜索结果，NVIDIA 提供了多种模型API，包括通过 NVIDIA API Catalog 访问的模型。要配置 NVIDIA 模型，需要以下步骤：

## 步骤 1: 获取 NVIDIA API 密钥
1. 访问 NVIDIA API Catalog (https://build.nvidia.com/explore/discover)
2. 注册账户并获取 API 密钥
3. 选择你想要使用的特定模型（如 Llama、Mixtral 等）

## 步骤 2: 配置 OpenClaw 使用 NVIDIA 模型
有两种方式可以配置：

### 方式一：通过 OpenClaw 配置命令（推荐）
```bash
# 配置 NVIDIA 作为模型提供商
openclaw config patch --json '{"models":{"providers":{"nvidia":{"baseUrl":"https://integrate.api.nvidia.com/v1","apiKey":"YOUR_NVIDIA_API_KEY","api":"openai-completions","models":[{"id":"meta/llama3-70b-instruct","name":"Llama 3 70B Instruct","input":["text"],"cost":{"input":0,"output":0},"contextWindow":8192,"maxTokens":8192}]}}}}'

# 设置 NVIDIA 模型为默认模型
openclaw config patch --json '{"agents":{"defaults":{"model":{"primary":"nvidia/meta/llama3-70b-instruct"}}}}'
```

### 方式二：直接编辑配置文件
1. 编辑配置文件：
```bash
nano ~/.openclaw/openclaw.json
```

2. 在配置文件中添加 NVIDIA 模型提供商：
```json
{
  "models": {
    "providers": {
      "qwen-portal": {
        // 原有配置保持不变
      },
      "nvidia": {
        "baseUrl": "https://integrate.api.nvidia.com/v1",
        "apiKey": "YOUR_NVIDIA_API_KEY",
        "api": "openai-completions",
        "models": [
          {
            "id": "meta/llama3-70b-instruct",
            "name": "Llama 3 70B Instruct",
            "input": [
              "text"
            ],
            "cost": {
              "input": 0,
              "output": 0
            },
            "contextWindow": 8192,
            "maxTokens": 8192
          },
          {
            "id": "mistralai/mixtral-8x7b-instruct",
            "name": "Mixtral 8x7B Instruct",
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
        "primary": "nvidia/meta/llama3-70b-instruct"
      }
    }
  }
}
```

## 常用 NVIDIA 模型列表
- `meta/llama3-70b-instruct` - Meta Llama 3 70B Instruct
- `mistralai/mixtral-8x7b-instruct` - Mixtral 8x7B Instruct
- `microsoft/phi-3-medium-128k-instruct` - Phi-3 Medium 128K Instruct
- `nvidia/nemotron-4-340b-instruct` - Nemotron 4 340B Instruct
- `google/gemma-2b` - Google Gemma 2B
- `snowflake/snowflake-arctic-instruct` - Snowflake Arctic Instruct

## 步骤 3: 重启 OpenClaw 服务
```bash
openclaw config apply
```

## 注意事项
1. 需要有效的 NVIDIA API 密钥才能使用
2. NVIDIA 模型可能需要付费使用（根据使用量计费）
3. 配置后会替换当前的 Qwen 模型作为主要模型
4. 建议先备份现有配置文件
5. 可以根据需要选择不同的 NVIDIA 模型

## 验证配置
配置完成后，可以通过简单的对话测试 NVIDIA 模型是否正常工作。