from api_config import db

class Registro(db.Model):
    __tablename__ = "registro"
    numero_registro = db.Column(db.Integer, primary_key=True)
    nombreyapellido = db.Column(db.String(100))
    domicilio = db.Column(db.String(100))
    edad = db.Column(db.Integer, nullable=True)
    fecha_emision = db.Column(db.String(10), nullable=True)
    fecha_vencimiento = db.Column(db.String(10))
