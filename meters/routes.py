from flask import Blueprint
from meters.models import Meter

meter_routes = Blueprint('meter_routes', __name__)


@meter_routes.route('/meters', methods=['GET'])
def fetch_meters():
    meter_data = Meter().get_all()
    return meter_data


@meter_routes.route('/meters/<id>', methods=['GET'])
def fetch_meter_data(id):
    return Meter().getByID(id)
