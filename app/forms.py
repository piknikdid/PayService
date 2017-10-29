from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, TextAreaField


class ServiceForm(FlaskForm):
    amount = FloatField('Amount')
    currency = SelectField('Currency', choices=[('978', 'EUR'), ('840', 'USD')])
    description = TextAreaField('Description')