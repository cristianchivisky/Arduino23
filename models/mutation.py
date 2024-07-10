from graphene import (
    ObjectType,
    Mutation,
    Int,
    String,
    Float,
    Boolean,
    Field,
)
from api_config import (
    db,
)

from models.objects import (
    Infraccion,
    Vehiculo,
    Registro,
    Usuario
)
from models.vehiculo import Vehiculo as VehiculoModel
from models.infraccion import Infraccion as InfraccionModel
from models.registro import Registro as RegistroModel
from models.usuario import Usuario as UsuarioModel

class createInfraccion(Mutation):
    class Arguments:
        numero_registro_id = Int(required=True)
        patente_vehiculo_id = String(required=True)
        codigo_infraccion = String(required=True)
        fecha = String(required=True)
        hora = String(required=True)
        observaciones = String(required=False)
        monto = Float(required=True)
        pagado = Boolean(required=True)
    
    infraccion = Field(lambda: Infraccion)

    def mutate(self, info, numero_registro_id, patente_vehiculo_id, codigo_infraccion, fecha, hora, monto, pagado, observaciones=None):
        infraccion = InfraccionModel(numero_registro_id=numero_registro_id,
                                     patente_vehiculo_id=patente_vehiculo_id,
                                     codigo_infraccion=codigo_infraccion,
                                     fecha=fecha,
                                     hora=hora,
                                     monto=monto,
                                     pagado=pagado,
                                     observaciones=observaciones)

        db.session.add(infraccion)
        db.session.commit()

        return createInfraccion(infraccion=infraccion)

class updateInfraccion(Mutation):
    class Arguments:
        numero_infraccion = Int(required=True)
        numero_registro_id = Int()
        patente_vehiculo_id = String()
        codigo_infraccion = String()
        observaciones = String()
        monto = Float()
        pagado = Boolean()

    infraccion = Field(lambda: Infraccion)

    def mutate(self, info, numero_infraccion, numero_registro_id=None, patente_vehiculo_id=None, codigo_infraccion=None, monto=None, pagado=None, observaciones=None):
        infraccion = InfraccionModel.query.get(numero_infraccion)
        if infraccion:
            if numero_registro_id:
                infraccion.numero_registro_id = numero_registro_id
            if patente_vehiculo_id:
                infraccion.patente_vehiculo_id = patente_vehiculo_id
            if codigo_infraccion:
                infraccion.codigo_infraccion = codigo_infraccion
            if observaciones:
                infraccion.observaciones = observaciones
            if monto:
                infraccion.monto = monto
            if pagado:
                infraccion.pagado = pagado
            db.session.add(infraccion)
            db.session.commit()

        return updateInfraccion(infraccion=infraccion)

class deleteInfraccion(Mutation):
    class Arguments:
        numero_infraccion = Int(required=True)

    infraccion = Field(lambda: Infraccion)

    def mutate(self, info, numero_infraccion):
        infraccion = InfraccionModel.query.get(numero_infraccion)
        if infraccion:
            db.session.delete(infraccion)
            db.session.commit()

        return deleteInfraccion(infraccion=infraccion)

class createVehiculo(Mutation):
    class Arguments:
        patente_vehiculo = String(required=True)
        anio_fabricacion = Int(required=True)
        nombreyapellido_propietario = String(required=True)
        domicilio_propietario = String(required=True)
        modelo = String(required=True)
        marca = String(required=True)
    
    vehiculo = Field(lambda: Vehiculo)

    def mutate(self, info, patente_vehiculo, anio_fabricacion,  nombreyapellido_propietario, domicilio_propietario, modelo, marca):
        vehiculo = VehiculoModel(patente_vehiculo=patente_vehiculo,
                                anio_fabricacion=anio_fabricacion,
                                nombreyapellido_propietario=nombreyapellido_propietario,
                                domicilio_propietario=domicilio_propietario,
                                modelo=modelo,
                                marca=marca)

        db.session.add(vehiculo)
        db.session.commit()

        return createVehiculo(vehiculo=vehiculo)
    
class updateVehiculo(Mutation):
    class Arguments:
        patente_vehiculo = String(required=True)
        anio_fabricacion = Int()
        nombreyapellido_propietario = String()
        domicilio_propietario = String()
        modelo = String()
        marca = String()


    vehiculo = Field(lambda: Vehiculo)

    def mutate(self, info, patente_vehiculo, anio_fabricacion=None,  nombreyapellido_propietario=None, domicilio_propietario=None, modelo=None, marca=None):
        vehiculo = VehiculoModel.query.get(patente_vehiculo)
        if vehiculo:
            if anio_fabricacion:
                vehiculo.anio_fabricacion = anio_fabricacion
            if nombreyapellido_propietario:
                vehiculo.nombreyapellido_propietario = nombreyapellido_propietario
            if domicilio_propietario:
                vehiculo.domicilio_propietario = domicilio_propietario
            if modelo:
                vehiculo.modelo = modelo
            if marca:
                vehiculo.marca = marca
            db.session.add(vehiculo)
            db.session.commit()

        return updateVehiculo(vehiculo=vehiculo)

class deleteVehiculo(Mutation):
    class Arguments:
        patente_vehiculo = String(required=True)

    vehiculo = Field(lambda: Vehiculo)

    def mutate(self, info, patente_vehiculo):
        vehiculo = VehiculoModel.query.get(patente_vehiculo)
        if vehiculo:
            db.session.delete(vehiculo)
            db.session.commit()

        return deleteVehiculo(vehiculo=vehiculo)
    
class createRegistro(Mutation):
    class Arguments:
        numero_registro = Int(required=True)
        nombreyapellido = String(required=True)
        domicilio = String(required=True)
        edad = Int(required=False)
        fecha_emision = String(required=False)
        fecha_vencimiento = String(required=True)
    
    registro = Field(lambda: Registro)

    def mutate(self, info, numero_registro,  nombreyapellido, domicilio, edad=None, fecha_emision=None, fecha_vencimiento=None):
        registro = RegistroModel(numero_registro=numero_registro,
                                nombreyapellido=nombreyapellido,
                                domicilio=domicilio,
                                edad=edad,
                                fecha_emision=fecha_emision,
                                fecha_vencimiento=fecha_vencimiento)

        db.session.add(registro)
        db.session.commit()

        return createRegistro(registro=registro)

class updateRegistro(Mutation):
    class Arguments:
        numero_registro = Int(required=True)
        nombreyapellido = String()
        domicilio = String()
        edad = Int()
        fecha_emision = String()
        fecha_vencimiento = String()

    registro = Field(lambda: Registro)

    def mutate(self, info, numero_registro, nombreyapellido=None, domicilio=None, edad=None, fecha_emision=None, fecha_vencimiento=None):
        registro = RegistroModel.query.get(numero_registro)
        if registro:
            if nombreyapellido:
                registro.nombreyapellido = nombreyapellido
            if domicilio:
                registro.domicilio = domicilio
            if edad:
                registro.edad = edad
            if fecha_emision:
                registro.fecha_emision = fecha_emision
            if fecha_vencimiento:
                registro.fecha_vencimiento = fecha_vencimiento
            db.session.add(registro)
            db.session.commit()

        return updateRegistro(registro=registro)

class deleteRegistro(Mutation):
    class Arguments:
        numero_registro = Int(required=True)

    registro = Field(lambda: Registro)

    def mutate(self, info, numero_registro):
        registro = RegistroModel.query.get(numero_registro)
        if registro:
            db.session.delete(registro)
            db.session.commit()

        return deleteRegistro(registro=registro)

class createUsuario(Mutation):
    class Arguments:
        nombre = String(required=True)
        contrasenia = String(required=True)
        email = String(required=True)

    usuario = Field(lambda: Usuario)

    def mutate(self, info, nombre, email, contrasenia):
        usuario = UsuarioModel(nombre=nombre, email=email, contrasenia=contrasenia)
        db.session.add(usuario)
        db.session.commit()

        return createUsuario(usuario=usuario)

class updateUsuario(Mutation):
    class Arguments:
        id = Int(required=True)
        nombre = String()
        email = String()
        contrasenia = String()

    usuario = Field(lambda: Usuario)

    def mutate(self, info, id, nombre=None, email=None, contrasenia=None):
        usuario = UsuarioModel.query.get(id)
        if usuario:
            if nombre:
                usuario.nombre = nombre
            if email:
                usuario.email = email
            if contrasenia:
                usuario.contrasenia = contrasenia
            db.session.add(usuario)
            db.session.commit()

        return updateUsuario(usuario=usuario)

class deleteUsuario(Mutation):
    class Arguments:
        id = Int(required=True)

    usuario = Field(lambda: Usuario)

    def mutate(self, info, id):
        usuario = UsuarioModel.query.get(id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()

        return deleteUsuario(usuario=usuario)

class Mutation(ObjectType):
    create_infraccion = createInfraccion.Field()
    update_infraccion = updateInfraccion.Field()
    delete_infraccion = deleteInfraccion.Field()
    create_vehiculo = createVehiculo.Field()
    update_vehiculo = updateVehiculo.Field()
    delete_vehiculo = deleteVehiculo.Field()
    create_registro = createRegistro.Field()
    update_registro = updateRegistro.Field()
    delete_registro = deleteRegistro.Field()
    create_usuario = createUsuario.Field()
    update_usuario = updateUsuario.Field()
    delete_usuario = deleteUsuario.Field()