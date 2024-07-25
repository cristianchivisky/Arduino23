from api_config import db

class Vehiculo(db.Model):
    __tablename__ = "vehiculo"
    patente_vehiculo = db.Column(db.String(20), primary_key=True)
    anio_fabricacion = db.Column(db.Integer, nullable=False)
    nombre_propietario = db.Column(db.String(50), nullable=False)
    apellido_propietario = db.Column(db.String(50), nullable=False)
    domicilio_propietario_calle = db.Column(db.String(50), nullable=False)
    domicilio_propietario_numero = db.Column(db.Integer, nullable=False)
    domicilio_propietario_ciudad = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
