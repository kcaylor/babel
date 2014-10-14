from flask import abort, jsonify
from . import main
from app.models import Dataset
import json
import pydap.client


dataset = Dataset.objects(name='vic_conus_3km').first()
dataset.data = pydap.client.open_url(dataset.url)


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
        location = json.loads(dataset.get_xy(lat=lat,lon=lon))
    else:
        return "error: provide latitude and longitude"
    result = 'dummy ' + str(lat) + str(lon)
    #result = str(dataset.get_data(x=location[0]['x'],y=location[0]['y']))
    return result


@main.route("/latlon/<location>", methods=['GET'])
def latlon_json(location=None):
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
    