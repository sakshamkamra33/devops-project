from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to DevOps Project 🚀")

@app.route('/about')
def about():
    return jsonify(message="This project demonstrates CI/CD pipeline")

@app.route('/status')
def status():
    return jsonify(status="Running", version="1.0")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)