# 快速开始指南

## 1. 获取Telegram Bot Token

1. 在Telegram中搜索并找到 @BotFather
2. 发送 `/newbot` 命令
3. 按提示输入机器人名称和用户名
4. 保存收到的API Token（格式如：`123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`）

## 2. 获取Chat ID

1. 向你的机器人发送一条消息
2. 在浏览器中访问：`https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
3. 找到 `message.chat.id` 的值，这就是你的Chat ID

## 3. 安装工具

```bash
# 克隆仓库
git clone https://github.com/your-username/telegram-file-manager.git
cd telegram-file-manager

# 安装依赖
pip install -r requirements.txt
```

## 4. 开始使用

### 下载文件
```bash
python3 tgfm.py download --token YOUR_BOT_TOKEN --chat-id YOUR_CHAT_ID --limit 50
```

### 搜索文件
```bash
python3 tgfm.py search --token YOUR_BOT_TOKEN --chat-id YOUR_CHAT_ID --pattern "pdf"
```

### 组织文件
```bash
python3 tgfm.py organize --token YOUR_BOT_TOKEN --chat-id YOUR_CHAT_ID --by type
```

## 5. 常见问题

### Q: 如何提高下载速度？
A: 可以减少`--limit`参数，分批下载文件。

### Q: 下载的文件保存在哪里？
A: 默认保存在当前目录的 `downloads` 文件夹中。

### Q: 支持哪些文件类型？
A: 支持所有Telegram支持的文件类型，包括文档、图片、视频等。

## 6. 获取帮助

```bash
python3 tgfm.py --help
python3 tgfm.py download --help
python3 tgfm.py search --help
python3 tgfm.py organize --help
```

祝使用愉快！