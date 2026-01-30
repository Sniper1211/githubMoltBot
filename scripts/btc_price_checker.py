#!/usr/bin/env python3
"""BTC 价格检查脚本（手动工具）

这个脚本只负责“获取并打印”BTC 价格。
定时推送建议使用 Clawdbot 内置 cron（更可靠、可观测、易维护）。
"""

from __future__ import annotations

from datetime import datetime, timezone

import requests


COINGECKO_URL = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=bitcoin&vs_currencies=usd,cny"
)


def get_btc_price() -> dict:
    """从 CoinGecko API 获取 BTC 价格（USD/CNY）"""
    response = requests.get(COINGECKO_URL, timeout=10)
    response.raise_for_status()
    data = response.json()

    price_usd = data.get("bitcoin", {}).get("usd")
    price_cny = data.get("bitcoin", {}).get("cny")

    return {
        "usd": price_usd,
        "cny": price_cny,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source": "CoinGecko",
    }


def main() -> None:
    try:
        btc = get_btc_price()
        # 容错：如果 API 返回结构变化，仍然能输出
        usd = btc.get("usd")
        cny = btc.get("cny")
        ts = btc.get("timestamp")

        print("BTC 当前价格")
        print(f"USD: ${usd}")
        print(f"CNY: ¥{cny}")
        print(f"更新时间(UTC): {ts}")
        print("来源: CoinGecko")
    except Exception as e:
        print(f"获取 BTC 价格失败: {e}")


if __name__ == "__main__":
    main()
