from flask import Flask
from dataset import Dataset
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
opendap_databases = client['opendap_databases']

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

