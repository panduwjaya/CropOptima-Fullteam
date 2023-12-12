from flask import Flask, request, jsonify
import numpy as np
import pickle
import json

with open("CloudComputing/plant-desc.json") as desc:
    plantDescData = json.load(desc)

# importing model
model = pickle.load(open("CloudComputing/model.pkl", "rb"))

# flask app
app = Flask(__name__)


@app.route("/detect", methods=["POST"])
def root():
    data = request.get_json()
    print(data)
    N = float(data.get("n"))
    P = float(data.get("p"))
    K = float(data.get("k"))
    temp = float(data.get("temp"))
    humid = float(data.get("humid"))
    ph = float(data.get("ph"))
    rainfall = float(data.get("rainfall"))

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
                "description": plantDescData[result]["description"],
            }
        )
    else:
        return jsonify({"crop": "N/A"})


if __name__ == "__main__":
    app.run(debug=True)
