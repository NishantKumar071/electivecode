# app.py

from flask import Flask, request, jsonify, send_file
from sentiment import simple_sentiment
import json, os, uuid, time

app = Flask(__name__)

DATA_FILE = "sentiments.json"

# Create empty file if not exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# Serve the dashboard HTML
@app.route("/")
def home():
    return send_file("dashboard.html")

# API: Sentiment results
@app.route("/api/sentiment_results")
def get_results():
    with open(DATA_FILE) as f:
        return jsonify(json.load(f))

# API: Analyze sentiment
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

    return jsonify({"sentiment": sentiment, "status": "success"})


if __name__ == "__main__":
    app.run(debug=True)
