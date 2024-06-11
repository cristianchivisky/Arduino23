from api_config import db

class Infraccion(db.Model):
    __tablename__ = "infraccion"
    numero_infraccion = db.Column(db.Integer, primary_key=True)
    numero_registro_id = db.Column(db.Integer, db.ForeignKey("registro.numero_registro"))
    patente_vehiculo_id = db.Column(db.String(20), db.ForeignKey("vehiculo.patente_vehiculo"))
    codigo_infraccion = db.Column(db.String(20))
    fecha = db.Column(db.String(10))
    hora = db.Column(db.String(10))
    observaciones = db.Column(db.String(300))
    registro = db.relationship("Registro", backref="infracciones")
    vehiculo = db.relationship("Vehiculo", backref="infracciones")
