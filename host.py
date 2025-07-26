from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

orders = []

@app.route("/receive_order", methods=["POST"])
def receive_order():
    data = request.get_json()
    print("ORDER RECEIVED:", data)
    orders.append(data)
    return jsonify({"status": "received"}), 200  # ✅ FIXED: use jsonify

@app.route("/get_orders", methods=["GET"])
def get_orders():
    if orders:
        return jsonify(orders.pop(0))
    else:
        return jsonify({})
        
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
