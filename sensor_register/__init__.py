from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ererwww33++'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test2.db'
db = SQLAlchemy(app)

from sensor_register import views
