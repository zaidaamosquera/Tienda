from app import db


class Rol(db.Model):
    idrol = db.Column(db.Integer, primary_key=True)
    NombreRol = db.Column(db.String(50), nullable=False)
    
  