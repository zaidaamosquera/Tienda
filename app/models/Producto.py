from app import db


class Producto(db.Model):
    idproducto = db.Column(db.Integer, primary_key=True)
    NombreProducto = db.Column(db.String(45), nullable=False)
    PrecioProducto = db.Column(db.Integer, nullable=False)
    Cantidad = db.Column(db.Integer, nullable=False)
    Imagenes= db.Column(db.String(10000), nullable=False)
