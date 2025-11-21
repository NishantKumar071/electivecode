from flask import Flask, send_file, jsonify, request
import json, os, time, uuid
from sentiment import simple_sentiment

app = Flask(_name_)
DATA_FILE = "sentiments.json"

# Create local DB if missing
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

@app.route("/")
def home():
    return send_file("dashboard.html")

@app.route("/api/sentiment_results")
def results():
    with open(DATA_FILE) as f:
        return jsonify(json.load(f))

@app.route("/api/analyze_sentiment", methods=["POST"])
def analyze():
    text = request.json.get("text", "").strip()
    if not text:
        return jsonify({"error": "Text is required"}), 400

    sentiment = simple_sentiment(text)
    entry = {
        "text": text,
        "sentiment": sentiment,
        "timestamp": time.time(),
        "id": str(uuid.uuid4())
    }

    with open(DATA_FILE) as f:
        data = json.load(f)
    data.append(entry)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

    return jsonify({"sentiment": sentiment})

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=10000)
