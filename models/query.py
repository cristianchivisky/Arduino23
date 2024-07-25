from graphene import (
    ObjectType,
    Field,
    String,
    Boolean,
    Float,
    List,
    Int
)

from models.vehiculo import Vehiculo as VehiculoModel
from models.registro import Registro as RegistroModel
from models.infraccion import Infraccion as InfraccionModel
from models.usuario import Usuario as UsuarioModel
from models.objects import Vehiculo, Registro, Infraccion, Usuario

class Query(ObjectType):
    all_infracciones = List(lambda: Infraccion)
    all_vehiculos = List(lambda: Vehiculo)
    all_registros = List(lambda: Registro)
    infracciones = List(lambda: Infraccion, numero_infraccion=Int(),  codigo_infraccion=String(), fecha=String(), hora=String(), monto=Float(), pagado=Boolean())
    vehiculos = List(lambda: Vehiculo, patente_vehiculo=String(), anio_fabricacion=Int(), nombre_propietario=String(), apellido_propietario=String(), domicilio_propietario_calle=String(), domicilio_propietario_ciudad=String(), marca=String(), modelo=String())
    registros = List(lambda: Registro, numero_registro=Int(), nombre=String(), apellido=String(), domicilio_calle=String(), domicilio_ciudad=String(), edad=Int(), fecha_emision=String(), fecha_vencimiento=String())
    infraccion = Field(lambda: Infraccion, numero_infraccion=Int())
    vehiculo = Field(lambda: Vehiculo, patente_vehiculo=String())
    registro = Field(lambda: Registro, numero_registro=Int())
    all_usuarios = List(lambda: Usuario)
    usuarios = List(lambda: Usuario, id=Int(), nombre=String(), email=String(), creado=String())
    usuario = Field(lambda: Usuario, nombre=String(required=True))

    def resolve_all_usuarios(self, info):
        query = Usuario.get_query(info=info)
        return query.all()

    def resolve_usuarios(self, info, id=None, nombre=None, email=None, creado=None):
        query = Usuario.get_query(info=info)
        if id:
            query = query.filter(UsuarioModel.id==id)
        if nombre:
            query = query.filter(UsuarioModel.nombre==nombre)
        if email:
            query = query.filter(UsuarioModel.email==email)
        if creado:
            query = query.filter(UsuarioModel.creado == creado)
        return query.all()

    def resolve_usuario(self, info, nombre):
        usuario = UsuarioModel.query.filter_by(nombre=nombre).first()
        return usuario
    
    def resolve_all_infracciones(self, info):
        query = Infraccion.get_query(info=info)
        return query.all()

    def resolve_infracciones(self, info, numero_infraccion=None, codigo_infraccion=None, fecha=None, hora=None, monto=None, pagado=None):
        query = Infraccion.get_query(info=info)
        if numero_infraccion:
            query = query.filter(InfraccionModel.numero_infraccion==numero_infraccion)
        if codigo_infraccion:
            query = query.filter(InfraccionModel.codigo_infraccion==codigo_infraccion)
        if fecha:
            query = query.filter(InfraccionModel.fecha==fecha)
        if hora:
            query = query.filter(InfraccionModel.hora == hora)
        if pagado:
            query = query.filter(InfraccionModel.pagado == pagado)
        if monto:
            query = query.filter(InfraccionModel.monto == monto)
        return query.all()

    def resolve_infraccion(self, info, numero_infraccion):
        infraccion = InfraccionModel.query.get(numero_infraccion)
        return infraccion
    
    def resolve_all_vehiculos(self, info):
        query = Vehiculo.get_query(info=info)
        return query.all()

    def resolve_vehiculos(self, info, patente_vehiculo=None, anio_fabricacion=None, nombre_propietario=None, apellido_propietario=None, domicilio_propietario_calle=None, domicilio_propietario_ciudad=None, modelo=None, marca=None):
        query = Vehiculo.get_query(info=info)
        if patente_vehiculo:
            query = query.filter(VehiculoModel.patente_vehiculo==patente_vehiculo)
        if anio_fabricacion:
            query = query.filter(VehiculoModel.anio_fabricacion==anio_fabricacion)
        if nombre_propietario:
            query = query.filter(VehiculoModel.nombre_propietario==nombre_propietario)
        if apellido_propietario:
            query = query.filter(VehiculoModel.apellido_propietario==apellido_propietario)
        if domicilio_propietario_calle:
            query = query.filter(VehiculoModel.domicilio_propietario_calle==domicilio_propietario_calle)
        if domicilio_propietario_ciudad:
            query = query.filter(VehiculoModel.domicilio_propietario_ciudad==domicilio_propietario_ciudad)
        if marca:
            query = query.filter(VehiculoModel.marca==marca)
        if modelo:
            query = query.filter(VehiculoModel.modelo==modelo)
        return query.all()
    
    def resolve_vehiculo(self, info, patente_vehiculo):
        vehiculo = VehiculoModel.query.get(patente_vehiculo)
        return vehiculo
    
    def resolve_all_registros(self, info):
        query = Registro.get_query(info=info)
        return query.all()
    
    def resolve_registros(self, info, numero_registro=None, nombre=None, apellido=None, domicilio_calle=None, domicilio_ciudad=None, edad=None, fecha_emision=None, fecha_vencimiento=None):
        query = Registro.get_query(info=info)
        if numero_registro:
            query = query.filter(RegistroModel.numero_registro==numero_registro)
        if nombre:
            query = query.filter(RegistroModel.nombre==nombre)
        if apellido:
            query = query.filter(RegistroModel.apellido==apellido)
        if domicilio_calle:
            query = query.filter(RegistroModel.domicilio_calle==domicilio_calle)
        if domicilio_ciudad:
            query = query.filter(RegistroModel.domicilio_ciudad==domicilio_ciudad)
        if edad:
            query = query.filter(RegistroModel.edad==edad)
        if fecha_emision:
            query = query.filter(RegistroModel.fecha_emision==fecha_emision)
        if fecha_vencimiento:
            query = query.filter(RegistroModel.fecha_vencimiento==fecha_vencimiento)
        return query.all()

    def resolve_registro(self, info, numero_registro):
        registro = RegistroModel.query.get(numero_registro)
        return registro