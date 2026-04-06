from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Home route (UI)
@app.route('/')
def home():
    return render_template("index.html")

# Status route (used in tests + API)
@app.route('/status')
def status():
    return jsonify(status="Running", version="1.0.0")

# About route
@app.route('/about')
def about():
    return jsonify(message="This project demonstrates CI/CD pipeline with Docker.")

# Optional API route
@app.route('/api/status')
def api_status():
    return jsonify(status="Running", version="1.0.0")

# Run app (important for Render deployment)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)