__author__ = 'jackgolding'
import os
from flask import request, redirect, url_for,flash, render_template,jsonify
from app import app, db
from app.models import DeviceLog

@app.route('/')
@app.route('/index')
def index():
    return 'Hey Govhack'

'''
Example request:

Header: application/json
{
   "device_id": "999",
   "power": 999,
   "temp": 999
}
'''

@app.route('/'+os.environ['WRITE_URL'], methods=['GET', 'POST'])
def get_data():
    json = request.get_json(force=True)
    try:
        log = DeviceLog(
                    device_id=json['device_id'],
                    power = json['power'],
                    temp = 23
                )
        db.session.add(log)
        db.session.commit()
        return 'NUL'
    except Exception as e:
        return 'SOH'

@app.route('/device/<id>')
def show_logs(id):
    id_bool = DeviceLog.query.filter_by(device_id=id)
    if id_bool is None:
        flash('Device {} not found'.format(id))
        return redirect(url_for('index'))
    else:
         logs = DeviceLog.query.filter_by(device_id=id).all()
         return render_template('logs.html',logs=logs)

@app.route('/usage/<id>')
def return_usage(id):
    return jsonify({"average": 17})

@app.route('/plot/<id>')
def return_data():
    return DeviceLog.query.filter_by(device_id=id).order_by(DeviceLog.created_on).first()
