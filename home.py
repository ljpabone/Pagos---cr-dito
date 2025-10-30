from flask import Blueprint, render_template, request
from models.pago import db, Pago
from routes.form import PagoForm

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/', methods=['GET', 'POST'])
def home():
    form = PagoForm()
    mensaje = None
    if form.validate_on_submit():
        nuevo_pago = Pago(nombre=form.nombre.data, monto=form.monto.data)
        db.session.add(nuevo_pago)
        db.session.commit()
        mensaje = "Pago registrado exitosamente."
        form.nombre.data = ""
        form.monto.data = ""
    return render_template('index.html', form=form, mensaje=mensaje)
