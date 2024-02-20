from app import db
from app.models.Producto import Producto



class Carrito(db.Model):
    idcarrito = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.Integer, db.ForeignKey('usuario.idUsuario'))
    producto = db.Column(db.Integer, db.ForeignKey('producto.idproducto'))


def __init__(self):
        self.carrito = []

def agregar_producto(self, idProducto, Cantidad):
        producto =Producto.query.get(idProducto)
        if producto:
            item = {'NombreProduto': NombreProducto, 'Cantidad': Cantidad}
            self.carrito.append(item)

def calcular_total(self):
        return sum(item['NombreProducto'].PrecioProducto * item['Cantidad'] for item in self.carrito)
    
def tamañoD(self):   
        return len(self.carrito)

def getItems(self):
        return self.carrito
    
def vaciarcarrito(self):
        self.carrito = []

   