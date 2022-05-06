import graphene
from home.schema import HomeQuery, Mutate
import accounts.schema


class Query(HomeQuery, accounts.schema.AccountsQuery, graphene.ObjectType):
    pass


class Mutation(Mutate, accounts.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
