import os
import pymysql
from flask import jsonify

db_user = os.environ.get("CLOUD_SQL_USERNAME")
db_password = os.environ.get("CLOUD_SQL_PASSWORD")
db_name = os.environ.get("CLOUD_SQL_DATABASE_NAME")
db_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")


def open_connection():
    unix_socket = f"/cloudsql/{db_connection_name}"
    try:
        if os.environ.get("GAE_ENV") == "standard":
            conn = pymysql.connect(
                user=db_user,
                password=db_password,
                unix_socket=unix_socket,
                db=db_name,
                cursorclass=pymysql.cursors.DictCursor,
            )
            return conn  # Return connection object here
    except pymysql.MySQLError as e:
        return e


def get_history(email):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM histories where email = %s;", (email,))
        history = cursor.fetchall()
        if history:
            got_history = jsonify(history)
        else:
            got_history = "Prediction not found"
        return got_history


def input_history(result, email):
    data = result.json()
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO histories (email, crop, location, description, imageURL) VALUES(%s, %s, %s, %s, %s)",
            (
                email,
                data["crop"],
                data["location"],
                data["description"],
                data["imageURL"],
            ),
        )
    conn.commit()
    conn.close()
