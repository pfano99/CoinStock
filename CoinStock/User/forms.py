from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField, SelectField

class InterstForm(FlaskForm):
    i_type = SelectField('Interest Type', validators=[DataRequired()], choices=['stock', 'crypto'])
    i_name = StringField('Name', validators=(DataRequired(), Length(min=2)))
    currency = SelectField('Currency', validators=[DataRequired()], choices=['ZAR', 'USD', 'EUR' ])
    submit = SubmitField('Add interest')