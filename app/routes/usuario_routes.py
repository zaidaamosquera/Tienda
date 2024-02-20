from flask import Blueprint, flash, render_template, request, redirect, url_for, jsonify,Flask,session
from numpy import roll
from app.models.Usuario import Usuario
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from flask_bcrypt import Bcrypt

bp = Blueprint('cliente', __name__)
app = Flask(__name__)
bcrypt = Bcrypt(app)

@bp.route('/', methods = ['GET','POST'])
def login():
    data = Usuario.query.all()
    if request.method == 'POST':
        NombreUsuario = request.form['Nombre']
        Contrasena = request.form['Contraseña']
        
        user = Usuario.query.filter_by(NombreUsuario=NombreUsuario).first()

        Contrasena = Contrasena.encode("utf-8")
        print(user)
        if not user:
            flash('Invalid credentials. Please try again.', 'danger')
            return render_template("producto/principal.html")
        if not bcrypt.check_password_hash(user.Contrasena, Contrasena):
            flash('Invalid credentials. Please try again.', 'danger')
            return render_template("usuario/login.html")

        if user:
            login_user(user)
            flash("Login successful!", "success")
            if user.rol_idrol==1:
             return render_template("usuario/administrador.html")
            return render_template("producto/principal.html")
        flash('Invalid credentials. Please try again.', 'danger')
        if current_user.is_authenticated:
            return render_template("producto/principal.html")
        return render_template("usuario/login.html")
    
    return render_template('usuario/login.html')
    

@bp.route('/Usuario/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        NombreUsuario = request.form['Nombre']
        Identificacion = request.form['Identificacion']
        Telefono = request.form['Telefono']
        Contrasena = request.form['Contraseña']
        
        new_cli = Usuario(NombreUsuario=NombreUsuario, Identificacion=Identificacion, Telefono=Telefono, Contrasena=bcrypt.generate_password_hash(Contrasena.encode("utf-8")))
        db.session.add(new_cli)
        db.session.commit()
        return redirect(url_for('cliente.add'))
    data = Usuario.query.all()
    return render_template('usuario/login.html', data=data)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    usuario = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        usuario.NombreUsuario = request.form['Nombre']
        usuario.Identificion = request.form['Identificacion']
        usuario.Telefono = request.form['Telefono']
        usuario.Contrasena= request.form['Contraseña']
        usuario.Rol = request.form['Rol']
        db.session.commit()
        
        return redirect(url_for('cliente.edit'))

    return render_template('usuario/edit.html', usuario=usuario)

@bp.route('/delete/<int:id>')
def delete(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('cliente.delete'))

@bp.route('/usuarioo')
@login_required
def Login():
    return 'Welcome, {current_user.NombreUsuario}! This is your dashboard.'

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('usuario.login'))

@bp.route('/listausuarios')
def listaUsuarios():
    usuarios = Usuario.query.all()
    return render_template('usuario/listausuarios.html', usuarios=usuarios)


@bp.route('/admi')
def administrador():
    return render_template('producto/agregarpro.html')

@bp.route('/citas')
def citas():
    return render_template('usuario/citas.html')

@bp.route('/registra')   
def registrarse():
    return render_template('usuario/registrarse.html')

@bp.route('/inicio')   
def paneladmini():
    return render_template('usuario/administrador.html')

@bp.route('/inici')   
def iniciar():
    return render_template('usuario/login.html')


@bp.route('/editar_perfil', methods=['GET', 'POST'])

@login_required
def editar_perfil():
    usuario = current_user  # Obtenemos el usuario actualmente autenticado

    if request.method == 'POST':
        # Obtenemos los datos del formulario enviado por el usuario
        nombreUsuario = request.form['NombreU']
        identificacion = request.form['identificacion']
        telefono = request.form['telefono']
        contrasena = request.form['contrasena']
        # Actualizamos los datos del usuario con los datos del formulario
        usuario.NombreUsuario = nombreUsuario
        usuario.Identificacion = identificacion
        usuario.Telefono = telefono
        # Si el usuario ha proporcionado una nueva contraseña, la encriptamos y la actualizamos
        if contrasena:
            usuario.Contrasena = bcrypt.generate_password_hash(contrasena.encode("utf-8"))

        # Guardamos los cambios en la base de datos
        db.session.commit()

        # Redirigimos al usuario a algún lugar después de editar su perfil
        flash('Tu perfil ha sido actualizado exitosamente', 'success')
        return redirect(url_for('cliente.editar_perfil'))


@bp.route('/isdco')   
def editarperfil():
    return render_template('usuario/actualizar.html')
