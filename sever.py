from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy list of valid keys
valid_keys = ["free", "free2", "free3"]


@app.route("/check_key", methods=["POST"])
def check_key():
    data = request.get_json()
    if "key" in data:
        key = data["key"]
        if key in valid_keys:
            response = {"valid": True}
        else:
            response = {"valid": False}
    else:
        response = {"error": "Key not provided in request"}

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
