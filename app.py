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

