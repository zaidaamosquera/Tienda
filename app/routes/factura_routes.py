from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Factura import Factura
from app import db
from app.models.Factura import Factura
from app.models.Detalle import Detalle
from app.routes.carrito_routes import carrito_compras
from app import db

bp = Blueprint('factura', __name__)

@bp.route('/facturas/factura')
def factura():
    data = Factura.query.all()
    return render_template('factura/factura.html', data=data)

@bp.route('/facturas/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        idFactura = request.form['NumeroFactura']
        fecha = request.form['Fecha']
        usuario = request.form['Usuario']
        total = request.form['Total']

        new_factura = Factura( idfactura= idFactura,  fecha= fecha, usuario=usuario,  total=total)
        db.session.add(new_factura)
        db.session.commit()
        
        return redirect(url_for('factura.add'))
    data = Factura.query.all()

    return render_template('factura/factura.html', data=data)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    fac = Factura.query.get_or_404(id)

    if request.method == 'POST':

        fac.idFactura = request.form['idFactura']
        fac.usuario = request.form['Usuario']
        fac.fecha = request.form['Fecha']
        fac.direccion = request.form['Direccion']
    
        db.session.commit()
        
        return redirect(url_for('cliente.edit'))

    return render_template('factura/factura.html', fac=fac)

@bp.route('/delete/<int:id>')
def delete(idfactura):
    fac = Factura.query.get_or_404(id)
    db.session.delete(fac)
    db.session.commit()

    return redirect(url_for('cliente.delete'))




bp = Blueprint('factura', __name__)

@bp.route('/factura')
def index():
    data = Factura.query.all()
    return render_template('producto/principal.html', data=data)

@bp.route('/addfactura', methods=['GET', 'POST'])
def add():
    factura = Factura(fecha="Hoy", idUsuario=1, direccion="Tunja")
    db.session.add(factura)
    db.session.commit()
    print("factura id  ", factura.idfactura)
    return redirect(url_for('factura.addDetalle',id=factura.idfactura))

@bp.route('/adddetalle/<int:id>', methods=['GET', 'POST'])  
def addDetalle(id):  
    for item in carrito_compras.getItems():
        idproducto = item["producto"].idproducto        
        detallefactura = detallefactura(idfactura=id,idproducto=idproducto)
        db.session.add(detallefactura)
        db.session.commit() 
    carrito_compras.vaciarcarrito()
    return redirect(url_for('producto.index'))

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    book = Factura.query.get_or_404(id)

    if request.method == 'POST':
        book.titulo = request.form['titulo']
        book.author = request.form['author']
        
        db.session.commit()
        
        return redirect(url_for('book.index'))

    return render_template('books/edit.html', book=book)

@bp.route('/delete/<int:id>')
def delete(id):
    book = Factura.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for('Book.index'))