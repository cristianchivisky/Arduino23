from api_config import db

class Vehiculo(db.Model):
    __tablename__ = "vehiculo"
    patente_vehiculo = db.Column(db.String(20), primary_key=True)
    anio_fabricacion = db.Column(db.Integer, nullable=True)
    nombreyapellido_propietario = db.Column(db.String(100))
    domicilio_propietario  = db.Column(db.String(100))
