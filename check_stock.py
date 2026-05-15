import os
import requests

URL = "https://www.sanroque.com.uy/catalogo/sobres-de-figuritas-mundial-fifa-2026_140112_140112"

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_telegram(message):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

html = requests.get(URL).text

if True:
#if '"tieneStock":true' in html:
    send_telegram(
        "🚨 HAY STOCK de figuritas FIFA 2026 en San Roque!\n\n" + URL
    )
else:
    print("Sin stock")
