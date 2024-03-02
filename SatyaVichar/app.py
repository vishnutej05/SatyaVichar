from flask import Flask, request, render_template, jsonify
import json
from dataextract import Everything
import pandas as pd

app = Flask(__name__)

fake_data = pd.read_csv('Fake.csv')
true_data = pd.read_csv('True.csv')
obj = Everything(fake_data, true_data)


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/index.html")
def indexMain():
    return render_template("index.html")

@app.route("/index2.html")
def index():
    return render_template("index2.html")

@app.route("/help.html")
def help():
    return render_template("help.html")

@app.route("/improve.html")
def improve():
    return render_template("improve.html")


@app.route("/textGen", methods=["POST"])
def txt():
    data = request.get_json()
    prompt = data["prompt"]
    result = obj.manual_testing(prompt)
    # result="Hello"
    print(jsonify(result))
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
