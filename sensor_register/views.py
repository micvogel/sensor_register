from flask import Flask, render_template
from sensor_register.forms import Sensors

@app.route('/')
def index():
    return render_template('home.html')
