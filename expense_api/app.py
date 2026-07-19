from flask import Flask, request, jsonify

app = Flask(__name__)

expenses = [
    {"category": "food", "amount":6000},
    {"category": "rent", "amount": 5500}
]

@app.route("/expenses", methods=["GET"])
def get_expense():
    return jsonify(expenses)

@app.route("/expenses", methods=["POST"])
def add_expense():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid or missing data"})

    category = data.get("category")
    amount = data.get("amount")

    if category is None:
        return jsonify({"error":"category cannot be empty"}, {400: "bad request"})
    
    if amount < 0:
        return jsonify({"error": "amount must be greater than 0"},{400: "bad request"})

    new_expenses = {
        "category": category,
        "amount": amount
    }

    expenses.append(new_expenses)

    return jsonify(expenses),201
    


app.run(debug=True)