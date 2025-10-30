from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

class PagoForm(FlaskForm):
    nombre = StringField('Nombre del Cliente', validators=[DataRequired()])
    monto = FloatField('Monto del Pago', validators=[DataRequired()])
    submit = SubmitField('Registrar')
