from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify({"service": "security-pipeline", "status": "ok"})


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})


@app.post("/echo")
def echo():
    payload = request.get_json(silent=True) or {}
    return jsonify({"received": payload})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
