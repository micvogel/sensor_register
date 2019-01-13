from sensor_register import db

class Sensors(db.Model):
    sensorid = db.Column(db.Integer, unique=True, primary_key=True)
    mac = db.Column(db.String(16), unique=True, nullable=False)
    uuid = db.Column(db.String(40), nullable=False)
    location = db.Column(db.String(40))
    detection_value = db.Column(db.String(40))
    battery_state = db.Column(db.String(40))
    connection_state = db.Column(db.String(40))
    target = db.Column(db.String(40))

class Detections(db.Model):
    detectid = db.Column(db.Integer, unique=True, primary_key=True)
    sensorid = db.Column(db.Integer, nullable=False)
    detection_time = db.Column(db.String(40))

class Targets(db.Model):
    targetid = db.Column(db.Integer, unique=True, primary_key=True)
    service = db.Column(db.String(40), nullable=False)
    command = db.Column(db.String(40), nullable=False)

    
