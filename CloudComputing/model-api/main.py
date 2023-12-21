from flask import Flask, jsonify, request
import numpy as np
import pickle
import json
import requests
import datetime

with open("data.json") as data:
    jsondata = json.load(data)

model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    N = float(data.get("n"))
    P = float(data.get("p"))
    K = float(data.get("k"))
    ph = float(data.get("ph"))
    lon = data.get("lon")
    lat = data.get("lat")
    weather = json.loads(
        requests.get(
            "https://api.openweathermap.org/data/2.5/weather?lat="
            + str(lat)
            + "&lon="
            + str(lon)
            + "&appid=64dd867de5e5d328aa7ee8d45c5271ad"
        ).text
    )
    temp = float(weather["main"]["temp"])
    humid = float(weather["main"]["humidity"])
    location = weather["name"]
    rainfall = jsondata["rainfall"][datetime.datetime.now().strftime("%m")]

    feature_list = [N, P, K, temp, humid, ph, rainfall]
    singl_pred = np.array(feature_list).reshape(1, -1)

    prediction = model.predict(singl_pred)
    result = prediction[0]

    crop_arr = [
        "rice",
        "maize",
        "chickpea",
        "kidneybeans",
        "pigeonpeas",
        "mothbeans",
        "mungbean",
        "blackgram",
        "lentil",
        "pomegranate",
        "banana",
        "mango",
        "grapes",
        "watermelon",
        "muskmelon",
        "apple",
        "orange",
        "papaya",
        "coconut",
        "cotton",
        "jute",
        "coffee",
    ]

    if result in crop_arr:
        return jsonify(
            {
                "crop": result,
                "description": jsondata["plant-description"][result]["description"],
                "imageURL": jsondata["plant-description"][result]["imageURL"],
                "location": location,
            }
        )
    else:
        return jsonify({"crop": "N/A"})


if __name__ == "__main__":
    app.run()
