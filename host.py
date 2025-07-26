from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

orders = []

@app.route('/receive_order', methods=['POST'])
def receive_order():
    order = request.json
    print("📦 Received order:", order)  # 🖨️ Show the received order
    orders.append(order)
    return jsonify({"status": "success", "message": "Order received"}), 200

@app.route('/get_orders', methods=['GET'])
def get_orders():
    if orders:
        return jsonify(orders.pop(0))  # return next order
    else:
        return jsonify({})  # empty if no order

if __name__ == '__main__':
    app.run(debug=True)
