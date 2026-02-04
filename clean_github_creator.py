#!/usr/bin/env python3
"""
GitHub仓库创建脚本（清理版）
"""

import urllib3
import os
import json

def create_github_repo(repo_name, description, token, private=False):
    """
    创建GitHub仓库
    """
    try:
        http = urllib3.PoolManager()
        url = "https://api.github.com/user/repos"
        
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json",
            "User-Agent": "telegram-file-manager"
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
        
        encoded_data = json.dumps(data).encode('utf-8')
        
        response = http.request(
            'POST',
            url,
            headers=headers,
            body=encoded_data
        )
        
        if response.status == 201:
            return json.loads(response.data.decode('utf-8'))
        else:
            return {"error": f"HTTP {response.status}: {response.data.decode('utf-8')}"}
            
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # 从环境变量获取GitHub token
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    
    if not GITHUB_TOKEN:
        print("请设置GITHUB_TOKEN环境变量")
        print("使用方式: export GITHUB_TOKEN='your_token_here'")
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
            print(f"⭐ 克隆命令: git clone {result['clone_url']}")
        else:
            print(f"❌ 仓库创建失败: {result['error']}")