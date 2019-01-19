import sys
sys.path.append("../")

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SensorsForm(FlaskForm):
    mac = StringField('MAC',
                           validators=[DataRequired(), Length(min=0, max=18)])
    uuid = StringField('UIID', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    target = StringField('Target', validators=[DataRequired()])
    submit = SubmitField('Add')
