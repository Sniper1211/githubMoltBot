# githubMoltBot

This repo contains small helper scripts/config for a Clawdbot-based bot.

## BTC price reminder (recommended)
Use **Clawdbot cron** (more reliable than a `while true; sleep ...` loop).

Example (Telegram chat/group id as destination). This version prints **USD + CNY** with a clean, consistent format:

```bash
clawdbot cron add \
  --name btc-price-every-30min \
  --every 30m \
  --session isolated \
  --message "请输出 BTC 现货价格（USD+CNY），格式如下（不要输出多余解释）：\n\nBTC 现货 · <UTC时间>\nUSD: $<usd_price>\nCNY: ¥<cny_price>\n来源: CoinGecko\n\n实现：用 web_fetch 请求 https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,cny ，解析 bitcoin.usd 与 bitcoin.cny；价格做千分位/保留2位小数（若拿不到就原样输出）。若接口不可用，换备用公开 API 并注明来源。" \
  --deliver --channel telegram --to <TELEGRAM_CHAT_ID>
```

## Manual BTC price check (optional)
A simple manual tool that fetches and prints BTC price:

```bash
python3 scripts/btc_price_checker.py
```
