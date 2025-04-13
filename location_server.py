from flask import Flask, request, jsonify, render_template_string
import datetime

app = Flask(__name__)
latest_location = {"lat": None, "lon": None, "time": None}

@app.route('/')
def index():
    return render_template_string("""
        <h2>📍 Live Phone Location Tracker</h2>
        {% if lat and lon %}
            <p><strong>Latitude:</strong> {{ lat }}</p>
            <p><strong>Longitude:</strong> {{ lon }}</p>
            <p><strong>Last Updated:</strong> {{ time }}</p>
            <a href="https://www.google.com/maps?q={{ lat }},{{ lon }}" target="_blank">Open in Google Maps</a>
        {% else %}
            <p>No location data received yet.</p>
        {% endif %}
    """, lat=latest_location["lat"], lon=latest_location["lon"], time=latest_location["time"])

@app.route('/update', methods=['POST'])
def update_location():
    data = request.json
    latest_location['lat'] = data.get('lat')
    latest_location['lon'] = data.get('lon')
    latest_location['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"status": "Location updated!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)