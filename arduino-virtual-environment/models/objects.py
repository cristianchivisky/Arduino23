from graphene_sqlalchemy import (
    SQLAlchemyObjectType
)
'''from graphene import (
    # Int
    String
)'''
from models.vehiculo import Vehiculo as VehiculoModel
from models.infraccion import Infraccion as InfraccionModel
from models.registro import Registro as RegistroModel


class Vehiculo(SQLAlchemyObjectType):
    class Meta:
        model = VehiculoModel

class Registro(SQLAlchemyObjectType):
    class Meta:
        model = RegistroModel

class Infraccion(SQLAlchemyObjectType):
    class Meta:
        model = InfraccionModel
