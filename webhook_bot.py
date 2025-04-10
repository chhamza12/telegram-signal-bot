from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '7821117718:AAHVrKHg16917MtzDRSC6C4j6Off4P63nNE'
TELEGRAM_CHAT_ID = '6054996245'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {'chat_id': TELEGRAM_CHAT_ID, 'text': message, 'parse_mode': 'Markdown'}
    requests.post(url, data=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = f"""
*New Signal Alert*

*Symbol:* {data.get('symbol', 'N/A')}
*Action:* {data.get('action', 'N/A')}
*Timeframe:* {data.get('timeframe', '5M')}
*Price:* {data.get('price', 'N/A')}
*Strategy:* Precision Scalper
"""
    send_telegram_message(message)
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
