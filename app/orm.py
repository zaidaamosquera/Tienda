from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definir el modelo (una tabla en la base de datos)
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    idUsuario = Column(Integer, Sequence('usuario_idUsuario_seq'), primary_key=True)
    NombreUsuario = Column(String(50))
    Identificacion = Column(Integer)
    Contrasena=Column(String(50))

# Modificar la URL de conexión para MySQL
# Sustituye 'usuario', 'contraseña', 'localhost' y 'nombre_de_base_de_datos' con tus propios valores
engine = create_engine('mysql+pymysql://root:He2Ee5D4cgEcAHa5D1hd--AhDbDh46-e@monorail.proxy.rlwy.net:49591/Tienda')

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión de SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Operaciones CRUD (igual que en el ejemplo anterior)

# Cerrar la sesión
session.close()