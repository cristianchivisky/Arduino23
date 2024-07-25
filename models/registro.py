from api_config import db

class Registro(db.Model):
    __tablename__ = "registro"
    numero_registro = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    domicilio_calle = db.Column(db.String(50), nullable=False)
    domicilio_numero = db.Column(db.Integer, nullable=False)
    domicilio_ciudad = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    fecha_emision = db.Column(db.Date, nullable=False)
    fecha_vencimiento = db.Column(db.Date, nullable=False)
