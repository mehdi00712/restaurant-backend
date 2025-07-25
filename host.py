from flask import Flask, request, jsonify
from flask_cors import CORS
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get port from environment
    app.run(host='0.0.0.0', port=port)


app = Flask(__name__)
CORS(app)

orders = []  # Store orders here

@app.route("/receive_order", methods=["POST"])
def receive_order():
    data = request.get_json()
    print("ORDER RECEIVED:", data)
    orders.append(data)
    return {"status": "received"}, 200

@app.route("/get_orders", methods=["GET"])
def get_orders():
    if orders:
        return jsonify(orders.pop(0))  # Send next order and remove it
    else:
        return jsonify({})  # Nothing yet

if __name__ == "__main__":
    app.run(debug=True)
