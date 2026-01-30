#!/bin/bash
# BTC 价格定时任务启动脚本
# 每半小时运行一次

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$SCRIPT_DIR/../logs/btc_price.log"

# 创建日志目录
mkdir -p "$(dirname "$LOG_FILE")"

# 设置你的 WhatsApp 号码或 Telegram ID
TARGET_RECIPIENT="${1:-+15555550123}"  # 修改为你的联系人

echo "[$(date '+%Y-%m-%d %H:%M:%S')] 启动 BTC 价格检查器 - 目标: $TARGET_RECIPIENT" >> "$LOG_FILE"

# 无限循环，每半小时执行一次
while true; do
    python3 "$SCRIPT_DIR/btc_price_checker.py"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 等待下一次检查..." >> "$LOG_FILE"
    sleep 1800  # 1800秒 = 30分钟
done
