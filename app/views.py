__author__ = 'jackgolding'
import os
from flask import request, redirect, url_for,flash, render_template
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
                    temp = json['temp']
                )
        db.session.add(log)
        db.session.commit()
        return 'success'
    except Exception as e:
        return str(e)

@app.route('/device/<id>')
def show_logs(id):
    id_bool = DeviceLog.query.filter_by(device_id=id)
    if id_bool is None:
        flash('Device {} not found').format(id)
        return redirect(url_for('index'))
    else:
         logs = DeviceLog.query.filter_by(device_id=id).all()
         return render_template('logs.html',logs=logs)