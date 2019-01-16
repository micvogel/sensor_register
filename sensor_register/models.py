from sensor_register import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"



# class Sensors(db.Model):
#     sensorid = db.Column(db.Integer, unique=True, primary_key=True)
#     mac = db.Column(db.String(16), unique=True, nullable=False)
#     uuid = db.Column(db.String(40), nullable=False)
#     location = db.Column(db.String(40))
#     detection_value = db.Column(db.String(40))
#     battery_state = db.Column(db.String(40))
#     connection_state = db.Column(db.String(40))
#     target = db.Column(db.String(40))
#
# class Detections(db.Model):
#     detectid = db.Column(db.Integer, unique=True, primary_key=True)
#     sensorid = db.Column(db.Integer, nullable=False)
#     detection_time = db.Column(db.String(40))
#
# class Targets(db.Model):
#     targetid = db.Column(db.Integer, unique=True, primary_key=True)
#     service = db.Column(db.String(40), nullable=False)
#     command = db.Column(db.String(40), nullable=False)
