from flask import Flask , jsonify, request

app = Flask(__name__)
user = [{"Name": "Akshay"}]

@app.route("/test", methods=["POST"])
def test():
    data = request.get_json()
    
    if not data or "name" not in data and "name" != None and "name" == str():
        return jsonify({"error": "JSON body name required"}), 400

    name = data["name"]
    return jsonify({"message": f"Hello {name}"}), 200

app.run(debug=True)