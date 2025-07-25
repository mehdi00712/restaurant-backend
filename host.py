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
    return {"status": "received"}, 200

@app.route("/get_orders", methods=["GET"])
def get_orders():
    if orders:
        return jsonify(orders.pop(0))  # Return and remove first order
    else:
        return jsonify({})  # No orders yet

if __name__ == "__main__":
    # ✅ Bind to 0.0.0.0 and use Render's assigned PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
