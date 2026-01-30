# githubMoltBot

This repo contains small helper scripts/config for a Clawdbot-based bot.

## BTC price reminder (recommended)
Use **Clawdbot cron** (more reliable than a `while true; sleep ...` loop).

Example (Telegram chat/group id as destination):

```bash
clawdbot cron add \
  --name btc-price-every-30min \
  --every 30m \
  --session isolated \
  --message "获取当前 BTC 现货价格并直接输出一行：BTC: $<price> (Coinbase spot) · <UTC时间>。用 web_fetch 请求 https://api.coinbase.com/v2/prices/spot?currency=USD ，解析 JSON 的 data.amount。若失败，改用备用公开接口并注明来源。不要输出多余解释。" \
  --deliver --channel telegram --to <TELEGRAM_CHAT_ID>
```

## Manual BTC price check (optional)
A simple manual tool that fetches and prints BTC price:

```bash
python3 scripts/btc_price_checker.py
```
