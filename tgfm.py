#!/usr/bin/env python3
"""
Telegram文件管理CLI工具
用于管理Telegram中的文件
"""

import click
import urllib3
import os
from datetime import datetime
import mimetypes

class TelegramFileManager:
    """Telegram文件管理器"""
    
    def __init__(self, bot_token, chat_id):
        """
        初始化文件管理器
        
        参数:
            bot_token: Telegram Bot Token
            chat_id: 目标聊天ID
        """
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.base_url = f"https://api.telegram.org/bot{bot_token}"
        self.http = urllib3.PoolManager()
        
    def get_messages(self, limit=100):
        """
        获取消息列表
        
        参数:
            limit: 获取消息数量限制
        
        返回:
            消息列表
        """
        try:
            url = f"{self.base_url}/getUpdates"
            params = {"offset": -limit, "timeout": 30}
            response = self.http.request('GET', url, params=params)
            
            if response.status == 200:
                return response.data.decode('utf-8')
            else:
                return {"error": f"HTTP {response.status}"}
                
        except Exception as e:
            return {"error": str(e)}
    
    def download_file(self, file_id, save_path):
        """
        下载文件
        
        参数:
            file_id: 文件ID
            save_path: 保存路径
        
        返回:
            (成功状态, 路径或错误信息)
        """
        try:
            url = f"{self.base_url}/getFile"
            params = {"file_id": file_id}
            response = self.http.request('GET', url, params=params)
            
            if response.status == 200:
                data = response.data.decode('utf-8')
                import json
                data = json.loads(data)
                
                if data.get('ok'):
                    file_path = data['result']['file_path']
                    file_url = f"https://api.telegram.org/file/bot{self.bot_token}/{file_path}"
                    
                    # 下载文件
                    file_response = self.http.request('GET', file_url)
                    
                    if file_response.status == 200:
                        # 确保目录存在
                        os.makedirs(os.path.dirname(save_path), exist_ok=True)
                        
                        # 保存文件
                        with open(save_path, 'wb') as f:
                            f.write(file_response.data)
                        
                        return True, save_path
                    else:
                        return False, f"下载失败 HTTP {file_response.status}"
                else:
                    return False, data.get('description', '下载失败')
            else:
                return False, f"获取文件信息失败 HTTP {response.status}"
                
        except Exception as e:
            return False, f"异常: {str(e)}"

@click.group()
def cli():
    """Telegram文件管理工具 - 管理Telegram文件的CLI工具"""
    pass

@cli.command()
@click.option('--token', required=True, help='Telegram Bot Token')
@click.option('--chat-id', required=True, help='Chat ID')
@click.option('--limit', default=100, help='消息数量限制')
def download(token, chat_id, limit):
    """
    下载Telegram文件
    
    参数:
        token: Bot Token
        chat_id: 聊天ID
        limit: 限制消息数量
    """
    manager = TelegramFileManager(token, chat_id)
    messages_json = manager.get_messages(limit)
    
    try:
        import json
        messages = json.loads(messages_json)
        
        if messages.get('ok'):
            result = messages.get('result', [])
            click.echo(f"找到 {len(result)} 条消息")
            
            download_count = 0
            error_count = 0
            
            for msg in result:
                if 'message' in msg:
                    message = msg['message']
                    if 'document' in message:
                        file_info = message['document']
                        file_id = file_info['file_id']
                        file_name = file_info.get('file_name', 'unknown')
                        file_size = file_info.get('file_size', 0)
                        
                        success, path = manager.download_file(file_id, f"downloads/{file_name}")
                        if success:
                            click.echo(f"✓ 下载成功: {file_name} ({file_size} bytes)")
                            download_count += 1
                        else:
                            click.echo(f"✗ 下载失败: {file_name} - {path}")
                            error_count += 1
            
            click.echo(f"\n总计: {download_count} 成功, {error_count} 失败")
        else:
            click.echo("获取消息失败: " + messages.get('description', '未知错误'))
            
    except json.JSONDecodeError as e:
        click.echo(f"解析JSON失败: {str(e)}")
    except Exception as e:
        click.echo(f"发生错误: {str(e)}")

@cli.command()
@click.option('--token', required=True, help='Telegram Bot Token')
@click.option('--chat-id', required=True, help='Chat ID')
@click.option('--pattern', help='搜索模式')
def search(token, chat_id, pattern):
    """
    搜索文件
    
    参数:
        token: Bot Token
        chat_id: 聊天ID
        pattern: 搜索模式（文件名）
    """
    manager = TelegramFileManager(token, chat_id)
    messages_json = manager.get_messages(200)
    
    try:
        import json
        messages = json.loads(messages_json)
        
        if messages.get('ok'):
            result = messages.get('result', [])
            match_count = 0
            
            for msg in result:
                if 'message' in msg:
                    message = msg['message']
                    if 'document' in message:
                        file_info = message['document']
                        file_name = file_info.get('file_name', 'unknown')
                        
                        if pattern is None or pattern.lower() in file_name.lower():
                            match_count += 1
                            file_size = file_info.get('file_size', 0)
                            file_date = message.get('date', 0)
                            
                            click.echo(f"📄 {file_name}")
                            click.echo(f"   大小: {file_size} bytes ({file_size/1024:.2f} KB)")
                            click.echo(f"   日期: {datetime.fromtimestamp(file_date)}")
                            click.echo()
            
            click.echo(f"找到 {match_count} 个匹配文件")
        else:
            click.echo("搜索失败: " + messages.get('description', '未知错误'))
            
    except json.JSONDecodeError as e:
        click.echo(f"解析JSON失败: {str(e)}")
    except Exception as e:
        click.echo(f"发生错误: {str(e)}")

@cli.command()
@click.option('--token', required=True, help='Telegram Bot Token')
@click.option('--chat-id', required=True, help='Chat ID')
@click.option('--by', type=click.Choice(['date', 'type', 'size']), help='组织方式')
def organize(token, chat_id, by):
    """
    组织文件
    
    参数:
        token: Bot Token
        chat_id: 聊天ID
        by: 组织方式 (date/type/size)
    """
    manager = TelegramFileManager(token, chat_id)
    messages_json = manager.get_messages(200)
    
    try:
        import json
        messages = json.loads(messages_json)
        
        if messages.get('ok'):
            result = messages.get('result', [])
            click.echo(f"找到 {len(result)} 条消息")
            click.echo(f"按 {by} 组织文件")
            
            # 简单的文件组织逻辑
            files = []
            
            for msg in result:
                if 'message' in msg:
                    message = msg['message']
                    if 'document' in message:
                        file_info = message['document']
                        file_name = file_info.get('file_name', 'unknown')
                        file_size = file_info.get('file_size', 0)
                        file_date = message.get('date', 0)
                        
                        # 获取文件扩展名作为类型
                        file_ext = os.path.splitext(file_name)[1].lower() if '.' in file_name else 'unknown'
                        mime_type = mimetypes.guess_type(file_name)[0] if mimetypes.guess_type(file_name) else 'unknown'
                        
                        files.append({
                            'name': file_name,
                            'size': file_size,
                            'date': file_date,
                            'type': file_ext,
                            'mime': mime_type
                        })
            
            if by == 'date':
                # 按日期排序
                files.sort(key=lambda x: x['date'])
                click.echo("按日期排序:")
                for f in files[:10]:  # 显示前10个
                    click.echo(f"  {datetime.fromtimestamp(f['date'])} - {f['name']}")
                    
            elif by == 'type':
                # 按类型分组
                type_groups = {}
                for f in files:
                    if f['type'] not in type_groups:
                        type_groups[f['type']] = []
                    type_groups[f['type']].append(f)
                
                click.echo("按文件类型分组:")
                for file_type, file_list in type_groups.items():
                    click.echo(f"  {file_type} ({len(file_list)} 个文件)")
                    
            elif by == 'size':
                # 按大小排序
                files.sort(key=lambda x: x['size'], reverse=True)
                click.echo("按文件大小排序:")
                for f in files[:10]:  # 显示前10个
                    click.echo(f"  {f['size']} bytes - {f['name']}")
            
            click.echo(f"\n总计 {len(files)} 个文件")
        else:
            click.echo("组织失败: " + messages.get('description', '未知错误'))
            
    except json.JSONDecodeError as e:
        click.echo(f"解析JSON失败: {str(e)}")
    except Exception as e:
        click.echo(f"发生错误: {str(e)}")

if __name__ == '__main__':
    cli()