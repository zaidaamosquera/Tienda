import base64
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.Producto import Producto
from app import db
import os
from flask import Flask
from werkzeug.utils import secure_filename

bp = Blueprint('produc', __name__)

@bp.route('/producto/agregarpro', methods=['GET'])
def agregarpro():
    data = Producto.query.all()
    return render_template('producto/agregarpro.html', data= data)
 

@bp.route('/producto/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        NombreProducto = request.form['Nombre']
        PrecioProducto = request.form['Precio']
        Cantidad = request.form ['Cantidad']
        imagen = request.files['Imagen']
        if imagen:
            filename = secure_filename(imagen.filename)  
            imagen.save(os.path.join('/app/static/imagenes filename'))

            ruta_imagen = filename
        else:
            ruta_imagen= 'static/imagenes/default.jpg'
            new_produc = Producto(NombreProducto=NombreProducto, PrecioProducto=PrecioProducto, Cantidad=Cantidad, Imagenes=imagen)
        db.session.add(new_produc)
        db.session.commit()
        return redirect(url_for('produc.add'))
    data = Producto.query.all()
    return render_template('producto/agregarpro.html', data=data)


@bp.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    producto = Producto.query.get_or_404(id)
    if request.method == 'POST':

        producto.NombreProducto = request.form['Nombre']
        producto.PrecioProducto = request.form['Precio']
        producto.Cantidad = request.form['Cantidad']
        producto.Imagen= request.form['Imagen']

        db.session.commit()

    

@bp.route('/delete/<int:id>',methods=['POST'] )
def delete(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    
@bp.route('/list', methods=['GET'])
def listaProductos():
         producto = Producto.query.all()
         return render_template('producto/agregarpro.html', data=producto)


@bp.route('/pro/', methods=['POST'] )
def acciones():
    opcion = request.form['fopcion']
    id = request.form['idproductos']
    if opcion == 'Eliminar': 
        delete(id)
    elif opcion == "Editar":
        edit(id)
    return redirect(url_for('produc.agregarpro'))


app = Flask(__name__)

# Configuración de la carpeta de carga de imágenes
app.config['UPLOAD_FOLDER'] = 'imagenes'

def subir_carpeta_de_imagenes():
    # Ruta de la carpeta de imágenes
    ruta_carpeta_imagenes = 'imagenes'
    # Ruta de la carpeta de carga de imágenes
    ruta_carpeta_carga = app.config['UPLOAD_FOLDER']

    # Verifica si la carpeta de carga existe, si no, la crea
    if not os.path.exists(ruta_carpeta_carga):
        os.makedirs(ruta_carpeta_carga)
    # Lista los archivos en la carpeta de imágenes
    archivos_imagenes = os.listdir(ruta_carpeta_imagenes)

    # Copia cada imagen a la carpeta de carga
    for archivo in archivos_imagenes:
        ruta_imagen = os.path.join(ruta_carpeta_imagenes, archivo)
        if os.path.isfile(ruta_imagen):
            ruta_destino = os.path.join(ruta_carpeta_carga, archivo)
            os.rename(ruta_imagen, ruta_destino)
            print(f"Se ha subido la imagen {archivo} al servidor.")

if __name__ == '__main__':
    subir_carpeta_de_imagenes()

