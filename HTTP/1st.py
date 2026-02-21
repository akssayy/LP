from flask import Flask , jsonify, request

app = Flask(__name__)
user = [{"Name": "Akshay"}]

@app.route("/test", methods=["POST"])
def test():
    data = request.get_json()
    return jsonify(data)

app.run(debug=True)