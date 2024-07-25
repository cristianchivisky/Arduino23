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

class CreateInfraccion(Mutation):
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

        return CreateInfraccion(infraccion=infraccion)

class UpdateInfraccion(Mutation):
    class Arguments:
        numero_infraccion = Int(required=True)
        numero_registro_id = Int()
        patente_vehiculo_id = String()
        codigo_infraccion = String()
        observaciones = String()
        monto = Float()
        pagado = Boolean()
        hora = String()
        fecha = String()

    infraccion = Field(lambda: Infraccion)

    def mutate(self, info, numero_infraccion, numero_registro_id=None, patente_vehiculo_id=None, codigo_infraccion=None, monto=None, pagado=None, observaciones=None, fecha=None, hora=None):
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
            if fecha:
                infraccion.fecha = fecha
            if hora:
                infraccion.hora = hora
            db.session.add(infraccion)
            db.session.commit()

        return UpdateInfraccion(infraccion=infraccion)

class DeleteInfraccion(Mutation):
    class Arguments:
        numero_infraccion = Int(required=True)

    infraccion = Field(lambda: Infraccion)

    def mutate(self, info, numero_infraccion):
        infraccion = InfraccionModel.query.get(numero_infraccion)
        if infraccion:
            db.session.delete(infraccion)
            db.session.commit()

        return DeleteInfraccion(infraccion=infraccion)

class CreateVehiculo(Mutation):
    class Arguments:
        patente_vehiculo = String(required=True)
        anio_fabricacion = Int(required=True)
        nombre_propietario = String(required=True)
        apellido_propietario = String(required=True)
        domicilio_propietario_calle = String(required=True)
        domicilio_propietario_numero = Int(required=True)
        domicilio_propietario_ciudad = String(required=True)
        modelo = String(required=True)
        marca = String(required=True)
    
    vehiculo = Field(lambda: Vehiculo)

    def mutate(self, info, patente_vehiculo, anio_fabricacion, nombre_propietario, apellido_propietario, domicilio_propietario_calle, domicilio_propietario_numero, domicilio_propietario_ciudad, modelo, marca):
        vehiculo = VehiculoModel(patente_vehiculo=patente_vehiculo,
                                anio_fabricacion=anio_fabricacion,
                                nombre_propietario=nombre_propietario,
                                apellido_propietario=apellido_propietario,
                                domicilio_propietario_calle=domicilio_propietario_calle,
                                domicilio_propietario_numero=domicilio_propietario_numero,
                                domicilio_propietario_ciudad=domicilio_propietario_ciudad,
                                modelo=modelo,
                                marca=marca)

        db.session.add(vehiculo)
        db.session.commit()

        return CreateVehiculo(vehiculo=vehiculo)
    
class UpdateVehiculo(Mutation):
    class Arguments:
        patente_vehiculo = String(required=True)
        anio_fabricacion = Int()
        nombre_propietario = String()
        apellido_propietario = String()
        domicilio_propietario_calle = String()
        domicilio_propietario_numero = Int()
        domicilio_propietario_ciudad = String()
        modelo = String()
        marca = String()

    vehiculo = Field(lambda: Vehiculo)

    def mutate(self, info, patente_vehiculo, anio_fabricacion=None, nombre_propietario=None, apellido_propietario=None, domicilio_propietario_calle=None, domicilio_propietario_numero=None, domicilio_propietario_ciudad=None, modelo=None, marca=None):
        vehiculo = VehiculoModel.query.get(patente_vehiculo)
        if vehiculo:
            if anio_fabricacion:
                vehiculo.anio_fabricacion = anio_fabricacion
            if nombre_propietario is not None:
                vehiculo.nombre_propietario = nombre_propietario
            if apellido_propietario is not None:
                vehiculo.apellido_propietario = apellido_propietario
            if domicilio_propietario_calle is not None:
                vehiculo.domicilio_propietario_calle = domicilio_propietario_calle
            if domicilio_propietario_numero is not None:
                vehiculo.domicilio_propietario_numero = domicilio_propietario_numero
            if domicilio_propietario_ciudad is not None:
                vehiculo.domicilio_propietario_ciudad = domicilio_propietario_ciudad
            if modelo:
                vehiculo.modelo = modelo
            if marca:
                vehiculo.marca = marca
            db.session.add(vehiculo)
            db.session.commit()

        return UpdateVehiculo(vehiculo=vehiculo)

class DeleteVehiculo(Mutation):
    class Arguments:
        patente_vehiculo = String(required=True)

    vehiculo = Field(lambda: Vehiculo)

    def mutate(self, info, patente_vehiculo):
        vehiculo = VehiculoModel.query.get(patente_vehiculo)
        if vehiculo:
            db.session.delete(vehiculo)
            db.session.commit()

        return DeleteVehiculo(vehiculo=vehiculo)
    
class CreateRegistro(Mutation):
    class Arguments:
        numero_registro = Int(required=True)
        nombre = String(required=True)
        apellido = String(required=True)
        domicilio_calle = String(required=True)
        domicilio_numero = Int(required=True)
        domicilio_ciudad = String(required=True)
        edad = Int(required=False)
        fecha_emision = String(required=False)
        fecha_vencimiento = String(required=True)
    
    registro = Field(lambda: Registro)

    def mutate(self, info, numero_registro, nombre, apellido, domicilio_calle, domicilio_numero, domicilio_ciudad, edad=None, fecha_emision=None, fecha_vencimiento=None):
        registro = RegistroModel(numero_registro=numero_registro,
                                nombre=nombre,
                                apellido=apellido,
                                domicilio_calle=domicilio_calle,
                                domicilio_numero=domicilio_numero,
                                domicilio_ciudad=domicilio_ciudad,
                                edad=edad,
                                fecha_emision=fecha_emision,
                                fecha_vencimiento=fecha_vencimiento)

        db.session.add(registro)
        db.session.commit()

        return CreateRegistro(registro=registro)

class UpdateRegistro(Mutation):
    class Arguments:
        numero_registro = Int(required=True)
        nombre = String()
        apellido = String()
        domicilio_calle = String()
        domicilio_numero = Int()
        domicilio_ciudad = String()
        edad = Int()
        fecha_emision = String()
        fecha_vencimiento = String()

    registro = Field(lambda: Registro)

    def mutate(self, info, numero_registro, nombre=None, apellido=None, domicilio_calle=None, domicilio_numero=None, domicilio_ciudad=None, edad=None, fecha_emision=None, fecha_vencimiento=None):
        registro = RegistroModel.query.get(numero_registro)
        if registro:
            if nombre is not None:
                registro.nombre = nombre
            if apellido is not None:
                registro.apellido = apellido
            if domicilio_calle is not None:
                registro.domicilio_calle = domicilio_calle
            if domicilio_numero is not None:
                registro.domicilio_numero = domicilio_numero
            if domicilio_ciudad is not None:
                registro.domicilio_ciudad = domicilio_ciudad
            if edad:
                registro.edad = edad
            if fecha_emision:
                registro.fecha_emision = fecha_emision
            if fecha_vencimiento:
                registro.fecha_vencimiento = fecha_vencimiento
            db.session.add(registro)
            db.session.commit()

        return UpdateRegistro(registro=registro)

class DeleteRegistro(Mutation):
    class Arguments:
        numero_registro = Int(required=True)

    registro = Field(lambda: Registro)

    def mutate(self, info, numero_registro):
        registro = RegistroModel.query.get(numero_registro)
        if registro:
            db.session.delete(registro)
            db.session.commit()

        return DeleteRegistro(registro=registro)

class CreateUsuario(Mutation):
    class Arguments:
        nombre = String(required=True)
        contrasenia = String(required=True)
        email = String(required=True)

    usuario = Field(lambda: Usuario)

    def mutate(self, info, nombre, email, contrasenia):
        usuario = UsuarioModel(nombre=nombre, email=email, contrasenia=contrasenia)
        db.session.add(usuario)
        db.session.commit()

        return CreateUsuario(usuario=usuario)

class UpdateUsuario(Mutation):
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

        return UpdateUsuario(usuario=usuario)

class DeleteUsuario(Mutation):
    class Arguments:
        id = Int(required=True)

    usuario = Field(lambda: Usuario)

    def mutate(self, info, id):
        usuario = UsuarioModel.query.get(id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()

        return DeleteUsuario(usuario=usuario)

class Mutation(ObjectType):
    create_infraccion = CreateInfraccion.Field()
    update_infraccion = UpdateInfraccion.Field()
    delete_infraccion = DeleteInfraccion.Field()
    create_vehiculo = CreateVehiculo.Field()
    update_vehiculo = UpdateVehiculo.Field()
    delete_vehiculo = DeleteVehiculo.Field()
    create_registro = CreateRegistro.Field()
    update_registro = UpdateRegistro.Field()
    delete_registro = DeleteRegistro.Field()
    create_usuario = CreateUsuario.Field()
    update_usuario = UpdateUsuario.Field()
    delete_usuario = DeleteUsuario.Field()