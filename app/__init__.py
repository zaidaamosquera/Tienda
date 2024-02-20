from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)

    from app.routes import carrito_routes, detalle_routes, factura_routes, producto_routes, rol_routes, usuario_routes
    app.register_blueprint(carrito_routes.bp)
    app.register_blueprint(detalle_routes.bp)
    app.register_blueprint(factura_routes.bp)
    app.register_blueprint(producto_routes.bp)
    app.register_blueprint(rol_routes.bp)
    app.register_blueprint(usuario_routes.bp)


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'usuario.login'

    @login_manager.user_loader
    def load_user(idUsuario):
        from .models.Usuario import Usuario
        return Usuario.query.get(int(idUsuario))

    from app.routes import (
        carrito_routes, 
        detalle_routes, 
        factura_routes, 
        producto_routes, 
        rol_routes, 
        usuario_routes
    )
    app.register_blueprint(carrito_routes.bp)
    app.register_blueprint(detalle_routes.bp)
    app.register_blueprint(factura_routes.bp)
    app.register_blueprint(producto_routes.bp)
    app.register_blueprint(rol_routes.bp)
    app.register_blueprint(usuario_routes.bp)


    return app