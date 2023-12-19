# main.py
from flask import Flask, jsonify, request
from db import get_history, input_history
import requests
import json

app = Flask(__name__)

verification_url = "https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=AIzaSyDNWTMdf4RoFlXr6tuTRUlBJ7hex2Y02Nk"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    idToken = data.get("idToken")
    N = float(data.get("n"))
    P = float(data.get("p"))
    K = float(data.get("k"))
    ph = float(data.get("ph"))
    lat = data.get("lat")
    lon = data.get("lon")

    verification_header = {"Content-Type": "application/x-www-form-urlencoded"}
    email = json.loads(
        requests.post(
            verification_url,
            headers=verification_header,
            data={"idToken": idToken},
        ).text
    )

    if "error" in email:
        return jsonify({"error": "true", "message": email["error"]["message"]})
    else:
        model_payload = json.dumps(
            {
                "n": N,
                "p": P,
                "k": K,
                "ph": ph,
                "lat": lat,
                "lon": lon,
            }
        )
        model_header = {"Content-Type": "application/json"}
        model_url = "https://crop.mautau.tk/predict"
        result = requests.post(model_url, headers=model_header, data=model_payload)
        input_history(result, email["users"][0]["email"])
        return jsonify({"error": "false", "message": result.json()})


@app.route("/history", methods=["POST"])
def history():
    idToken = str(request.get_json().get("idToken"))
    verification_header = {"Content-Type": "application/x-www-form-urlencoded"}
    email = json.loads(
        requests.post(
            verification_url, headers=verification_header, data={"idToken": idToken}
        ).text
    )
    if "error" in email:
        return jsonify({"error": "true", "message": email["error"]["message"]})
    else:
        return get_history(email["users"][0]["email"])


if __name__ == "__main__":
    app.run()
