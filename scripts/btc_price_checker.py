#!/usr/bin/env python3
"""
BTC 价格检查脚本
每半小时检查一次 BTC 当前价格
"""

import requests
import json
import subprocess
from datetime import datetime


def get_btc_price():
    """从 CoinGecko API 获取 BTC 价格"""
    try:
        response = requests.get(
            'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,cny',
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        
        price_usd = data.get('bitcoin', {}).get('usd', 'N/A')
        price_cny = data.get('bitcoin', {}).get('cny', 'N/A')
        
        return {
            'usd': price_usd,
            'cny': price_cny,
            'timestamp': datetime.now().isoformat()
        }
    except Exception as e:
        return {'error': str(e)}


def send_message(target, message):
    """通过 ClawdBot 发送消息"""
    try:
        cmd = [
            'clawdbot',
            'message',
            'send',
            '--target', target,
            '--message', message
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return result.returncode == 0
    except Exception as e:
        print(f"发送消息失败: {e}")
        return False


def main():
    """主函数"""
    btc_data = get_btc_price()
    
    if 'error' in btc_data:
        message = f"❌ 获取 BTC 价格失败: {btc_data['error']}"
    else:
        price_usd = btc_data['usd']
        price_cny = btc_data['cny']
        message = f"💰 BTC 当前价格\n\n" \
                  f"USD: ${price_usd:,}\n" \
                  f"CNY: ¥{price_cny:,.2f}\n\n" \
                  f"更新时间: {btc_data['timestamp']}"
    
    print(message)
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 价格检查完成")


if __name__ == '__main__':
    main()
