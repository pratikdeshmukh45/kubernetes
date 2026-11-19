
from flask import Flask, jsonify
import os
from datetime import datetime, timezone

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "OpsPulse API")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

services = [
    {
        "id": 1,
        "name": "Payment Service",
        "status": "UP",
        "environment": "production"
    },
    {
        "id": 2,
        "name": "Authentication Service",
        "status": "UP",
        "environment": "production"
    },
    {
        "id": 3,
        "name": "Database Service",
        "status": "DEGRADED",
        "environment": "production"
    },
    {
        "id": 4,
        "name": "Notification Service",
        "status": "UP",
        "environment": "production"
    }
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION,
        "message": "Welcome to OpsPulse"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200


@app.route("/api/services", methods=["GET"])
def get_services():
    return jsonify({
        "total_services": len(services),
        "services": services
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
