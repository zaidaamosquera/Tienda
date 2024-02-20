from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Detalle import Detalle
from app import db

bp = Blueprint('detalle', __name__)

@bp.route('/detalles/detalle')
def detalle():
    data = Detalle.query.all()
    return render_template('detalle/detalle.html', data=data)
     
@bp.route('/detalle/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        factura = request.form['Factura']
        producto = request.form['Producto']
        Cantidad = request.form['Cantidad']
        Total = request.form['Total']
        new_detalle = Detalle()
        db.session.add(new_detalle)
        db.session.commit()
        
        return redirect(url_for('detalle.add'))

    data = Detalle.query.all()
    return render_template('producto.detalle.html', data=data)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    Deta = Detalle.query.get_or_404(id)

    if request.method == 'POST':
        Deta.factura = request.form['Factura']
        Deta.producto = request.form['Producto']
        Deta.Cantidad = request.form['Cantidad']
        Deta.Total = request.form['Total']
        
        db.session.commit()
        
        return redirect(url_for('detalle.cliente'))

    return render_template('producto/detalle.html', Deta=Deta)

@bp.route('/delete/<int:id>')
def delete(id):
    Deta = Detalle.query.get_or_404(id)
    
    db.session.delete(Deta)
    db.session.commit()

    return redirect(url_for('detalle.delete'))
