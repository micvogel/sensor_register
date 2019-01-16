from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length


class SensorsForm(FlaskForm):
    mac = StringField('MAC',
                           validators=[DataRequired(), Length(min=16, max=18)])
    uuid = StringField('UIID', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    target = Stringfiel('Target', validators=[DataRequired()])
    submit = SubmitField('Add')
