from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import carrito_routes, detalle_routes, factura_routes, producto_routes, rol_routes, usuario_routes
