import sys
sys.path.append("../")

from flask import Flask, render_template, flash, redirect, url_for
from flask_table import Table, Col
from sensor_register.forms import SensorsForm
from sensor_register.models import Sensors
from sensor_register import app, db

@app.route('/', methods=['GET','POST'])
def home():
    class SensorsTable(Table):
        sensorid = Col('SensorID')
        mac = Col('MAC address')
        uuid = Col('UUID')
        location = Col('Location')
        detection_value = Col('Detection')
        battery_state = Col('Battery')
        connection_state = Col('Connection')
        target = Col('Target')

    table = SensorsTable(Sensors.query.all())
    return render_template('home.html', table=table)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = SensorsForm()

    if form.validate_on_submit():

        return redirect(url_for('home'))
    return render_template('add.html', form=form)
