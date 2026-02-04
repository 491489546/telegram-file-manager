#!/usr/bin/env python3
"""
通过Telegram发送文件的脚本（最终版）
使用urllib3的multipart上传
"""

import urllib3
import os
import mimetypes

def send_file_via_telegram(file_path, chat_id, bot_token, caption=None):
    """
    通过Telegram Bot API发送文件

    参数:
        file_path: 文件路径
        chat_id: 接收文件的聊天ID
        bot_token: Telegram Bot Token
        caption: 文件说明（可选）

    返回:
        API响应结果
    """
    try:
        http = urllib3.PoolManager()
        url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
        
        # 检查文件是否存在
        if not os.path.exists(file_path):
            return {"error": f"文件不存在: {file_path}"}

        # 获取文件信息
        filename = os.path.basename(file_path)
        with open(file_path, 'rb') as f:
            file_data = f.read()
        
        # 获取MIME类型
        mime_type = mimetypes.guess_type(file_path)[0] or 'application/octet-stream'

        # 构建multipart数据
        boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
        
        body = b''
        
        # 添加chat_id
        body += f'--{boundary}\r\n'.encode('utf-8')
        body += f'Content-Disposition: form-data; name="chat_id"\r\n\r\n{chat_id}\r\n'.encode('utf-8')
        
        # 添加文件
        body += f'--{boundary}\r\n'.encode('utf-8')
        body += f'Content-Disposition: form-data; name="document"; filename="{filename}"\r\n'.encode('utf-8')
        body += f'Content-Type: {mime_type}\r\n\r\n'.encode('utf-8')
        body += file_data
        body += b'\r\n'
        
        # 添加caption
        if caption:
            body += f'--{boundary}\r\n'.encode('utf-8')
            body += f'Content-Disposition: form-data; name="caption"\r\n\r\n{caption}\r\n'.encode('utf-8')
        
        body += f'--{boundary}--\r\n'.encode('utf-8')

        # 设置headers
        headers = {
            'Content-Type': f'multipart/form-data; boundary={boundary}',
            'Content-Length': str(len(body))
        }

        # 发送请求
        response = http.request(
            'POST',
            url,
            headers=headers,
            body=body
        )
        
        return response.data.decode('utf-8')

    except Exception as e:
        return {"error": str(e)}

# 使用示例
if __name__ == "__main__":
    BOT_TOKEN = "8579241072:AAHnGaIgv-2Rj-qgOd-WSnWVPacozam_CBA"
    CHAT_ID = "1008397041"
    
    # 发送README文件
    result = send_file_via_telegram("README.md", CHAT_ID, BOT_TOKEN, "项目README文件")
    print(result)