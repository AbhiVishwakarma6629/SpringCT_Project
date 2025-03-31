from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from models import db, bcrypt
from auth import auth_bp
from routes import product_bp, order_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(product_bp)
app.register_blueprint(order_bp)

if __name__ == "__main__":
    app.run(debug=True)
