from flask import Flask, request, jsonify
import numpy as np
import pickle
import json
from flask_mysqldb import MySQL

with open("CloudComputing/plant-desc.json") as desc:
    plantDescData = json.load(desc)

# importing model
model = pickle.load(open("CloudComputing/model.pkl", "rb"))

# flask app
app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "crop-optima-db"

mysql = MySQL(app)


@app.route("/predict", methods=["POST"])
def root():
    data = request.get_json()
    print(data)
    email = data.get("email")
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
        cursor = mysql.connection.cursor()
        cursor.execute(""" INSERT INTO predict VALUES(%s,%s) """, (email, result))
        mysql.connection.commit()
        cursor.close()
        return jsonify(
            {
                "crop": result,
                "description": plantDescData[result]["description"],
            }
        )
    else:
        return jsonify({"crop": "N/A"})


# app.run(host="localhost", port=5000)

if __name__ == "__main__":
    app.run(debug=True)
