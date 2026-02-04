#!/usr/bin/env python3
"""
Telegram文件管理CLI工具
用于管理Telegram中的文件
"""

import click
import requests
import os
from pathlib import Path
import json
import sqlite3
from datetime import datetime

class TelegramFileManager:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.base_url = f"https://api.telegram.org/bot{bot_token}"
        
    def get_messages(self, limit=100):
        """获取消息列表"""
        url = f"{self.base_url}/getUpdates"
        params = {"offset": -limit, "timeout": 30}
        response = requests.get(url, params=params)
        return response.json()
    
    def download_file(self, file_id, save_path):
        """下载文件"""
        url = f"{self.base_url}/getFile"
        params = {"file_id": file_id}
        response = requests.get(url, params=params)
        data = response.json()
        
        if data.get('ok'):
            file_path = data['result']['file_path']
            file_url = f"https://api.telegram.org/file/bot{self.bot_token}/{file_path}"
            
            # 下载文件
            response = requests.get(file_url)
            
            # 确保目录存在
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            
            # 保存文件
            with open(save_path, 'wb') as f:
                f.write(response.content)
            
            return True, save_path
        else:
            return False, data.get('description', '下载失败')

@click.group()
def cli():
    """Telegram文件管理工具"""
    pass

@cli.command()
@click.option('--token', required=True, help='Telegram Bot Token')
@click.option('--chat-id', required=True, help='Chat ID')
@click.option('--limit', default=100, help='消息数量限制')
def download(token, chat_id, limit):
    """下载Telegram文件"""
    manager = TelegramFileManager(token, chat_id)
    messages = manager.get_messages(limit)
    
    if messages.get('ok'):
        result = messages.get('result', [])
        click.echo(f"找到 {len(result)} 条消息")
        
        # 这里可以添加文件下载逻辑
        for msg in result:
            if 'message' in msg:
                message = msg['message']
                if 'document' in message:
                    file_info = message['document']
                    file_id = file_info['file_id']
                    file_name = file_info.get('file_name', 'unknown')
                    
                    success, path = manager.download_file(file_id, f"downloads/{file_name}")
                    if success:
                        click.echo(f"✓ 下载成功: {file_name}")
                    else:
                        click.echo(f"✗ 下载失败: {file_name}")
    else:
        click.echo("获取消息失败")

@cli.command()
@click.option('--token', required=True, help='Telegram Bot Token')
@click.option('--chat-id', required=True, help='Chat ID')
@click.option('--pattern', help='搜索模式')
def search(token, chat_id, pattern):
    """搜索文件"""
    manager = TelegramFileManager(token, chat_id)
    messages = manager.get_messages(200)
    
    if messages.get('ok'):
        result = messages.get('result', [])
        click.echo(f"搜索到 {len(result)} 条消息")
        
        for msg in result:
            if 'message' in msg:
                message = msg['message']
                if 'document' in message:
                    file_info = message['document']
                    file_name = file_info.get('file_name', 'unknown')
                    
                    if pattern is None or pattern.lower() in file_name.lower():
                        click.echo(f"📄 {file_name}")
                        click.echo(f"   大小: {file_info.get('file_size', 0)} bytes")
                        click.echo(f"   日期: {datetime.fromtimestamp(message.get('date', 0))}")
                        click.echo()
    else:
        click.echo("搜索失败")

@cli.command()
@click.option('--token', required=True, help='Telegram Bot Token')
@click.option('--chat-id', required=True, help='Chat ID')
@click.option('--by', type=click.Choice(['date', 'type', 'size']), help='组织方式')
def organize(token, chat_id, by):
    """组织文件"""
    manager = TelegramFileManager(token, chat_id)
    messages = manager.get_messages(200)
    
    if messages.get('ok'):
        result = messages.get('result', [])
        click.echo(f"找到 {len(result)} 条消息")
        click.echo(f"按 {by} 组织文件")
        
        # 这里可以添加文件组织逻辑
        click.echo("文件组织功能开发中...")
    else:
        click.echo("组织失败")

if __name__ == '__main__':
    cli()