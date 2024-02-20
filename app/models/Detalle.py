from app import db


class Detalle(db.Model):
    idDetalle = db.Column(db.Integer, primary_key=True)
    factura = db.Column(db.Integer, db.ForeignKey('factura.idfactura'))
    producto = db.Column(db.Integer, db.ForeignKey('producto.idproducto'))
    Cantidad = db.Column(db.Integer, nullable=False)
    Total = db.Column(db.Integer, nullable=False)


   