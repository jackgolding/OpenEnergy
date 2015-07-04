__author__ = 'jackgolding'
import os
from flask import request, redirect, url_for,flash
from app import app, db
from app.models import DeviceLog

@app.route('/')
@app.route('/index')
def index():
    return 'Hey Govhack'


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
    id = DeviceLog.query.filter_by(device_id=id)
    if id is None:
        flash('Device {} not found').format(id)
        return redirect(url_for('index'))
    else:
        return DeviceLog.query.filter_by(device_id=id)