from flask import Flask
from models.pago import db
from routes.home import home_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta_segura'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pagos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(home_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
