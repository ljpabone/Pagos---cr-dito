from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pago(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    monto = db.Column(db.Float, nullable=False)
