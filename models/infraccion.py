from api_config import db

class Infraccion(db.Model):
    __tablename__ = "infraccion"
    numero_infraccion = db.Column(db.Integer, primary_key=True)
    numero_registro_id = db.Column(db.Integer, db.ForeignKey("registro.numero_registro"), nullable=False)
    patente_vehiculo_id = db.Column(db.String(20), db.ForeignKey("vehiculo.patente_vehiculo"), nullable=False)
    codigo_infraccion = db.Column(db.String(20), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    observaciones = db.Column(db.String(300), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    pagado = db.Column(db.Boolean(), default=False)
    registro = db.relationship("Registro", backref="infracciones")
    vehiculo = db.relationship("Vehiculo", backref="infracciones")
