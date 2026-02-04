#!/usr/bin/env python3
"""
通过Telegram发送文件的脚本（修复版）
使用urllib3直接调用Telegram API，避免OpenSSL冲突
"""

import urllib3
import os

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

        # 准备文件和数据
        with open(file_path, 'rb') as f:
            files = {'document': f.read(), 'filename': os.path.basename(file_path)}
        
        data = {
            'chat_id': chat_id,
            'document': file_path,
            'caption': caption if caption else ''
        }

        # 使用multipart/form-data发送
        response = http.request_encode_body(
            'POST',
            url,
            fields={
                'chat_id': chat_id,
                'document': (os.path.basename(file_path), open(file_path, 'rb')),
                'caption': caption if caption else ''
            }
        )
        
        # 关闭文件
        if 'document' in data and hasattr(data['document'], 'close'):
            data['document'].close()

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