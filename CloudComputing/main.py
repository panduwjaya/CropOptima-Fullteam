from flask import Flask, request, jsonify
import numpy as np
import pickle
import json
import requests
import datetime


# from flask_mysqldb import MySQL

with open("CloudComputing/data.json") as data:
    jsondata = json.load(data)

# importing model
model = pickle.load(open("CloudComputing/model.pkl", "rb"))

# flask app
app = Flask(__name__)

# app.config["MYSQL_HOST"] = "10.128.0.9"
# app.config["MYSQL_USER"] = "root"
# app.config["MYSQL_PASSWORD"] = "ce2031aa-c83a-4384-84bd-ef36c5f95c58"
# app.config["MYSQL_DB"] = "crop_optima_db"

# mysql = MySQL(app)


@app.route("/predict", methods=["POST"])
def root():
    data = request.get_json()
    email = data.get("email")
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
        # cursor = mysql.connection.cursor()
        # cursor.execute(""" INSERT INTO history VALUES(%s,%s) """, (email, result))
        # mysql.connection.commit()
        # cursor.close()
        return jsonify(
            {
                "email": email,
                "crop": result,
                "description": jsondata["plant-description"][result]["description"],
                "location": location,
            }
        )
    else:
        return jsonify({"crop": "N/A"})


if __name__ == "__main__":
    app.run(debug=True)
