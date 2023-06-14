from graphene import Schema

from models.query import Query
from models.mutation import Mutation

schema = Schema(query=Query, mutation=Mutation)