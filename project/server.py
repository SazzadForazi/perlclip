from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

latest_text = ""

@app.route('/update', methods=['POST'])
def update_text():
    global latest_text
    data = request.json
    latest_text = data.get("text", "")
    return jsonify({"status": "ok"})

@app.route('/latest', methods=['GET'])
def get_latest():
    return jsonify({"text": latest_text})

if __name__ == "__main__":
    app.run(port=8081)
