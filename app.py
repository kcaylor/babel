#!/usr/bin/python
import os
if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

from flask import Flask, abort
from dataset import Dataset, database_list

app = Flask(__name__)

@app.route("/")
def opendap_json(url_dataset=None, lat=None, lon=None):
    # dataset = opendap_database_list.find(name=url_dataset).first()?
    if not url_dataset:
        abort(404)
    else:
        database_obj = database_list[url_dataset]
        database_obj.get_xy()
        database_obj.get_data()
        database_obj.make_json()
        return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)

