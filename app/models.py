__author__ = 'jackgolding'

from app import db

class DeviceLog(db.Model):
    __tablename__ = 'devicelogs'

    log_id = db.Column(db.Integer, primary_key=True)
    power = db.Column(db.Float())
    temp = db.Column(db.Float())
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())


    def __init__(self, power, temp):
        self.power = power
        self.temp = temp

#may want to change this according to http://stackoverflow.com/questions/7102754/jsonify-a-sqlalchemy-result-set-in-flask

    def __repr__(self):
        return '<id {}>'.format(self.log_id)