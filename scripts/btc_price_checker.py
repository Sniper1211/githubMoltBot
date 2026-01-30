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


def _fmt_money(v, prefix: str, decimals: int = 2) -> str:
    if v is None:
        return f"{prefix}N/A"
    try:
        n = float(v)
        return f"{prefix}{n:,.{decimals}f}"
    except Exception:
        # If API returns something unexpected, print raw
        return f"{prefix}{v}"


def main() -> None:
    try:
        btc = get_btc_price()
        ts = btc.get("timestamp")

        usd = _fmt_money(btc.get("usd"), "$", 2)
        cny = _fmt_money(btc.get("cny"), "¥", 2)

        print(f"BTC 现货 · {ts}")
        print(f"USD: {usd}")
        print(f"CNY: {cny}")
        print("来源: CoinGecko")
    except Exception as e:
        print(f"获取 BTC 价格失败: {e}")


if __name__ == "__main__":
    main()
