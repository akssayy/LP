from flask import Flask , jsonify, request

app = Flask(__name__)
user = [{"Name": "Akshay"}]

@app.route("/test", methods=["POST"])
def test():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "JSON body required"}), 400
       
    return jsonify(data), 200

app.run(debug=True)