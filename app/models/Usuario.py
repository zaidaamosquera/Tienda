from app import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    idUsuario = db.Column(db.Integer, primary_key=True)
    NombreUsuario = db.Column(db.String(50), nullable=False)
    Identificacion = db.Column(db.String(50), nullable=False)
    Telefono = db.Column(db.String(50), nullable=False)
    Contrasena = db.Column(db.String(256), nullable=False)
    rol_idrol = db.Column(db.Integer, db.ForeignKey('rol.idrol'), default=2)
    RolUsuario = db.relationship("Rol")

    def get_id(self):
        return str(self.idUsuario)