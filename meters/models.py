#!/usr/bin/env Python3

from flask.json import jsonify
from utils import get_db_connection


class Meter:

    def get_all(self):
        try:
            conn = get_db_connection()
            meters = conn.execute('SELECT * FROM meters').fetchall()
            conn.close()
            meter_data = []
            if meters:
                for meterF in meters:
                    meter_data_dict = {}
                    meter_data_dict = {key: meterF[key]
                                       for key in meterF.keys()}
                    meter_data_dict.update({
                        'meter_id': 'http://127.0.0.1:5000/meters/' +
                        str(meterF['id'])})
                    meter_data.append(meter_data_dict)
                return jsonify(meter_data), 200
            return jsonify({'data': 'No data found!'})
        except Exception as e:
            return jsonify({'error': e})

    def getByID(self, id):
        try:
            conn = get_db_connection()
            meter_data = conn.execute('SELECT * FROM meter_data \
                                      WHERE meter_id = ? ORDER BY DATE(time_stamp)',
                                      (id,)).fetchall()
            conn.close()
            meter_data_found = []
            if meter_data:
                for meterF in meter_data:
                    meter_data_found.append({key: meterF[key]
                                             for key in meterF.keys()})

                return jsonify(meter_data_found), 200
            return jsonify({'data': 'No data found!'})
        except Exception as e:
            return jsonify({'error': e})
