from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


@app.route("/demo")
def demo():
    return jsonify(message="Demo endpoint working!"), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
