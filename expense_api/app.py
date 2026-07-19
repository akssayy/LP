from flask import Flask, request, jsonify

app = Flask(__name__)

expenses = [
    {"category": "food", "amount":6000},
    {"category": "rent", "amount": 5500}
]

@app.route("/expenses", methods=["GET"])
def get_expense():
    return jsonify(expenses)

@app.route("/add", methods=["POST"])
def add_expense():
    data = request.get_json

    category = data.get("category")
    amount = data.get("amount")

    if not category:
        return jsonify-
app.run(debug=True)