from app import db


class Factura(db.Model):
    idfactura = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.Integer, db.ForeignKey('usuario.idUsuario'))
    fecha = db.Column(db.String(45), nullable=False)
    direccion = db.Column(db.String(45), nullable=False)
