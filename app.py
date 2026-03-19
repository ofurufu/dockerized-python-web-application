from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "development")

@app.route("/")
def home():
    return f"Hello from Docker project v2 UPDATED! Environment: {APP_ENV}"

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "version": "v2",
        "environment": APP_ENV
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)