__author__ = 'jackgolding'

from app import db

class DeviceLog(db.Model):
    __tablename__ = 'devicelogs'

    log_id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String)
    power = db.Column(db.Integer())
    temp = db.Column(db.Integer())
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    face = db.Column(db.Integer)


    def __init__(self, device_id, power, temp):
        self.device_id = device_id
        self.power = power
        self.temp = temp
        self.face = 0

#may want to change this according to http://stackoverflow.com/questions/7102754/jsonify-a-sqlalchemy-result-set-in-flask

    def __repr__(self):
        return '<id {}>'.format(self.log_id)