# Telegram File Manager

一个强大的命令行工具，用于管理Telegram文件，包括备份、组织、搜索等功能。

## 功能特性

### 免费版功能
- 📥 文件下载：从指定聊天下载文件
- 🔍 文件搜索：根据名称、类型、日期搜索文件
- 📁 基础组织：按日期、类型自动组织文件
- 🔄 批量操作：批量下载、删除、移动

### 付费版功能（计划中）
- 🎯 高级搜索：按内容、标签搜索
- ☁️ 云端同步：与云存储同步
- 📊 自动备份：定时自动备份
- 📈 数据分析：文件使用统计、趋势分析
- ⚙️ 自定义规则：定义文件处理规则

## 安装

### 前置要求
- Python 3.6+
- Telegram Bot Token

### 安装步骤
```bash
# 克隆仓库
git clone https://github.com/your-username/telegram-file-manager.git
cd telegram-file-manager

# 安装依赖
pip install -r requirements.txt

# 验证安装
python3 tgfm.py --help
```

## 使用方法

### 基本命令
```bash
# 下载文件
python3 tgfm.py download --token YOUR_BOT_TOKEN --chat-id YOUR_CHAT_ID

# 搜索文件
python3 tgfm.py search --token YOUR_BOT_TOKEN --chat-id YOUR_CHAT_ID --pattern "文件名"

# 组织文件
python3 tgfm.py organize --token YOUR_BOT_TOKEN --chat-id YOUR_CHAT_ID --by type
```

### 高级用法
```bash
# 限制下载消息数量
python3 tgfm.py download --token YOUR_BOT_TOKEN --chat-id YOUR_CHAT_ID --limit 50

# 按多种方式组织
python3 tgfm.py organize --token YOUR_BOT_TOKEN --chat-id YOUR_CHAT_ID --by date
python3 tgfm.py organize --token YOUR_BOT_TOKEN --chat-id YOUR_CHAT_ID --by size
```

## 配置

### Telegram Bot Token获取
1. 在Telegram中找到 @BotFather
2. 发送 `/newbot` 创建新机器人
3. 按提示设置机器人名称和用户名
4. 保存获得的API Token

### 获取Chat ID
1. 发送消息给你的机器人
2. 访问 `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
3. 找到你的chat_id

## 项目结构
```
telegram-file-manager/
├── tgfm.py              # 主程序文件
├── README.md             # 项目说明
├── requirements.txt      # 依赖列表
├── LICENSE             # 开源许可证
└── docs/              # 文档目录
```

## 开发路线图

### 当前版本 (v0.1.0)
- [x] 基础文件下载功能
- [x] 基本文件搜索功能
- [x] 文件组织框架
- [ ] 完善错误处理
- [ ] 添加更多文档

### 下一版本 (v0.2.0)
- [ ] 批量操作优化
- [ ] 配置文件支持
- [ ] 进度显示
- [ ] 文件类型过滤

### 未来计划
- [ ] 付费版功能开发
- [ ] 图形界面版本
- [ ] 多平台支持
- [ ] 云同步功能

## 贡献指南

欢迎贡献代码、报告bug、提出建议！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 许可证

本项目采用 MIT 许可证 - 详见 LICENSE 文件

## 支持

如果遇到问题或有任何建议，请：
- 📧 提交Issue
- 💬 在Discussion中讨论
- ⭐ 给项目加星支持

## 致谢

感谢所有贡献者和用户的支持！

## 赞助

如果你觉得这个工具有帮助，欢迎通过GitHub Sponsors赞助支持！

- ⭐ GitHub Sponsors: [赞助链接]
- ☕ 请我喝咖啡: [链接待添加]

---

**注意**: 本工具仅供个人学习和研究使用，请遵守Telegram的服务条款。