#!/usr/bin/env python3
"""
GitHub仓库创建脚本
用于自动化创建和管理GitHub仓库
"""

from github import Github
import os

def create_github_repo(repo_name, description, token, private=False):
    """
    创建GitHub仓库

    参数:
        repo_name: 仓库名称
        description: 仓库描述
        token: GitHub个人访问令牌
        private: 是否为私有仓库

    返回:
        创建的仓库对象
    """
    try:
        # 使用GitHub API
        g = Github(token)
        
        # 获取当前用户
        user = g.get_user()
        
        # 创建仓库
        repo = user.create_repo(
            name=repo_name,
            description=description,
            private=private,
            auto_init=True,
            has_wiki=True,
            has_issues=True,
            has_downloads=True
        )
        
        return repo
        
    except Exception as e:
        print(f"创建仓库失败: {str(e)}")
        return None

def setup_repo_structure(repo):
    """
    设置仓库结构

    参数:
        repo: GitHub仓库对象
    """
    try:
        # 创建基本文件结构
        # 这里可以添加更多初始化文件
        
        print(f"仓库结构设置完成: {repo.full_name}")
        return True
        
    except Exception as e:
        print(f"设置仓库结构失败: {str(e)}")
        return False

# 使用示例
if __name__ == "__main__":
    # 从环境变量获取GitHub token
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    
    if not GITHUB_TOKEN:
        print("请设置GITHUB_TOKEN环境变量")
        print("在GitHub上创建Personal Access Token:")
        print("https://github.com/settings/tokens")
    else:
        # 创建Telegram文件管理CLI工具仓库
        repo = create_github_repo(
            repo_name="telegram-file-manager",
            description="一个强大的命令行工具，用于管理Telegram文件，包括备份、组织、搜索等功能。",
            token=GITHUB_TOKEN,
            private=False
        )
        
        if repo:
            print(f"✅ 仓库创建成功: {repo.full_name}")
            print(f"🔗 仓库地址: {repo.html_url}")
            
            # 设置仓库结构
            if setup_repo_structure(repo):
                print("✅ 仓库基础结构设置完成")
            else:
                print("❌ 仓库结构设置失败")
        else:
            print("❌ 仓库创建失败")