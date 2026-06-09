# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello from Docker!"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():

    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")

    return f"""
    DB Host: {db_host}<br>
    DB Name: {db_name}
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)