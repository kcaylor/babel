from flask import abort, jsonify
from . import main
from app.models import Dataset

dataset = Dataset.objects(name='vic_conus_3km').first()

@main.route("/")
def hello():
    return "Hello World"


@main.route("/<api_key>/<location>", methods=['GET'])
def opendap_json(api_key=None, location=None):
    try:
        loc = location.split(',')
    except:
        abort(404)
    try:
        lat = float(loc[0])
        lon = float(loc[1])
    except:
        abort(404)
    if lat and lon:
        return dataset.get_xy(lat=lat,lon=lon)
    else:
        return "error: provide latitude and longitude"
