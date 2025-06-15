import requests
import time
import os

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram(message):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=data)

def get_price():
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=WLDUSDT'
    r = requests.get(url)
    return float(r.json()['price'])

last_alert = None

while True:
    try:
        price = get_price()
        print(f"[WLD] Harga sekarang: ${price}")

        if price > 1.10 and last_alert != 'up':
            send_telegram(f"🚀 WLD/USDT Breakout! Harga: ${price}")
            last_alert = 'up'

        elif price < 0.94 and last_alert != 'down':
            send_telegram(f"⚠️ WLD/USDT Breakdown! Harga: ${price}")
            last_alert = 'down'

        time.sleep(60)

    except Exception as e:
        print("Error:", e)
        time.sleep(60)
