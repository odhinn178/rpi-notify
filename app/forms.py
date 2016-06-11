from flask_wtf import Form
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class NotifyForm(Form):
    message = StringField('Notification Message', validators=[DataRequired()])
    priority = BooleanField('Priority')
    send = SubmitField('Send')
