from flask import abort, jsonify
from . import main
from app.models import Dataset

datasets = Dataset.objects()
    
def get_xy(dataset,lat,lon):
    return "boo"


@main.route("/")
def hello():
    return "Hello World"

@main.route("/<api_key>/<lat>,<lon>", methods=['GET'])
def opendap_json(api_key=None, lat=None, lon=None):
    if lat and lon:
        for dataset in datasets:
            return get_xy(dataset,lat,lon)

    else:
        return "error: provide latitude and longitude"
