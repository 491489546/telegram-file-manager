#!/usr/bin/env python3
"""
通过Telegram发送文件的脚本
基于Telegram Bot API实现文件传输功能
"""

import requests
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
        # 检查文件是否存在
        if not os.path.exists(file_path):
            return {"error": f"文件不存在: {file_path}"}

        # 准备API请求
        url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
        
        # 准备文件和数据
        files = {'document': open(file_path, 'rb')}
        data = {'chat_id': chat_id}
        
        if caption:
            data['caption'] = caption

        # 发送文件
        response = requests.post(url, files=files, data=data)
        
        # 关闭文件
        files['document'].close()

        return response.json()

    except Exception as e:
        return {"error": str(e)}

def send_text_via_telegram(text, chat_id, bot_token):
    """
    通过Telegram Bot API发送文本消息

    参数:
        text: 要发送的文本
        chat_id: 接收消息的聊天ID
        bot_token: Telegram Bot Token

    返回:
        API响应结果
    """
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        
        data = {
            'chat_id': chat_id,
            'text': text
        }

        response = requests.post(url, data=data)
        return response.json()

    except Exception as e:
        return {"error": str(e)}

# 使用示例
if __name__ == "__main__":
    # 从环境变量或配置文件获取参数
    BOT_TOKEN = "8579241072:AAHnGaIgv-2Rj-qgOd-WSnWVPacozam_CBA"
    CHAT_ID = "1008397041"
    
    # 发送文件示例
    # result = send_file_via_telegram("test.txt", CHAT_ID, BOT_TOKEN, "这是一个测试文件")
    # print(result)
    
    # 发送文本示例
    # result = send_text_via_telegram("这是一个测试消息", CHAT_ID, BOT_TOKEN)
    # print(result)