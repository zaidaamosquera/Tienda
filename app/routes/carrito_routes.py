from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Carrito import Carrito
from app.models.Detalle import Detalle
from app.models.Factura import Factura
from app.models.Producto import Producto
from app.models.Rol import Rol
from app.models.Usuario import Usuario
from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.Producto import Producto
from app.models.Carrito import Carrito


from app import db

bp = Blueprint('carrito', __name__)

@bp.route('/Carro/Carrito')
def carrito():
    data = Carrito.query.all()
    return render_template('usuario/carrito.html', data=data)

@bp.route('/carrito/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        usuario = request.form['Usuario']
        producto = request.form['Producto']
        new_compra = Carrito(producto=producto, usuario=usuario)
        db.session.add(new_compra)
        db.session.commit()

        return redirect(url_for('carrito.add'))
    data = Carrito.query.all()
    return render_template('usuario/carrito.html', data=data)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    Compra = Carrito.query.get_or_404(id)

    if request.method == 'POST':
        Compra.producto = request.form['Producto']
        Compra.usuario = request.form['Usuario']
        
        db.session.commit()
        
        return redirect(url_for('carrito.delete'))

    return render_template('usuario/carrito.html', Compra=Compra)

@bp.route('/delete/<int:id>')
def delete(id):
    Compra = Carrito.query.get_or_404(id)
    
    db.session.delete(Compra)
    db.session.commit()

    return redirect(url_for('carrito.delete'))




bp = Blueprint('carritos', __name__)
carrito_compras = Carrito()

@bp.route('/ListarCarrito')
def listar():
    items = carrito_compras.getItems()
    return render_template('productos/List.html', items=items)

@bp.route('/ListarProductos')
def index():
    productos = carrito_compras
    return render_template('index.html', productos=productos)

@bp.route('/agregar/<int:id>', methods=['POST'])
def agregar_al_carrito(idproducto):
    Cantidad = int(request.form.get('cantidad', 1))
    carrito_compras.agregar_producto(idproducto, Cantidad)
    return redirect(url_for('producto.index'))

@bp.route('/realizar_compra')
def realizar_compra():
    total = carrito_compras.calcular_total()
    return render_template('realizar_compra.html', total=total)

@bp.route('/generar_factura', methods=['POST'])
def generar_factura():
    total = carrito_compras.calcular_total()
    carrito_compras.carrito = []
    return render_template('factura.html', total=total)

@bp.route('/itemscarrito', methods=['GET', 'POST'])
def tCarrito():
    a = carrito_compras.tamañoD()
    print("Entra a carrito rutas", a)
    return f"Entra a carrito {carrito_compras.tamañoD()}"