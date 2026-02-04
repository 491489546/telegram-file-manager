#!/usr/bin/env python3
"""
GitHub仓库创建脚本（简化版）
使用requests直接调用GitHub API
"""

import requests
import os
import json

def create_github_repo(repo_name, description, token, private=False):
    """
    创建GitHub仓库

    参数:
        repo_name: 仓库名称
        description: 仓库描述
        token: GitHub个人访问令牌
        private: 是否为私有仓库

    返回:
        创建的仓库信息
    """
    try:
        url = "https://api.github.com/user/repos"
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        data = {
            "name": repo_name,
            "description": description,
            "private": private,
            "auto_init": True,
            "has_wiki": True,
            "has_issues": True,
            "has_downloads": True
        }
        
        response = requests.post(url, headers=headers, data=json.dumps(data))
        
        if response.status_code == 201:
            return response.json()
        else:
            return {"error": response.text}
            
    except Exception as e:
        return {"error": str(e)}

# 使用示例
if __name__ == "__main__":
    # 从环境变量获取GitHub token
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    
    if not GITHUB_TOKEN:
        print("请设置GITHUB_TOKEN环境变量")
        print("在GitHub上创建Personal Access Token:")
        print("https://github.com/settings/tokens")
        print("需要权限: repo (完整仓库访问权限)")
    else:
        # 创建Telegram文件管理CLI工具仓库
        result = create_github_repo(
            repo_name="telegram-file-manager",
            description="一个强大的命令行工具，用于管理Telegram文件，包括备份、组织、搜索等功能。",
            token=GITHUB_TOKEN,
            private=False
        )
        
        if "error" not in result:
            print(f"✅ 仓库创建成功!")
            print(f"📦 仓库名称: {result['name']}")
            print(f"🔗 仓库地址: {result['html_url']}")
            print(f"📝 仓库描述: {result['description']}")
        else:
            print(f"❌ 仓库创建失败: {result['error']}")