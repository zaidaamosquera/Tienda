from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Rol import Rol
from app import db

bp = Blueprint('Cargo', __name__)

@bp.route('/Rol/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        idRol = request.form['idRol']
        NombreRol = request.form['Rol']
        
        new_rol = Rol( idRol= idRol, NombreRol=NombreRol)
        db.session.add(new_rol)
        db.session.commit()
        
        return redirect(url_for('Cargo.add'))
    data = Rol.query.all()
    return render_template('usuario/login.html', data=data)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    Cargo = Rol.query.get_or_404(id)

    if request.method == 'POST':
        Cargo.idRol = request.form['idRol']
        Cargo.NombreRol = request.form['Rol']
        db.session.commit()
        
        return redirect(url_for('Cargo.edit'))

    return render_template('usuario/login.html', Cargo=Cargo)

@bp.route('/delete/<int:id>')
def delete(id):
    Cargo = Rol.query.get_or_404(id)
    
    db.session.delete(Rol)
    db.session.commit()

    return redirect(url_for('Cargo.delete'))
