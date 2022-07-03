from graphene_django import DjangoObjectType
import graphene
from .models import *

class ProductSchema(DjangoObjectType):
    class Meta:
        model = Product
        fields = ['id', 'category', 'brand', 'price', 'quantity', 'imageurl']


class OrderSchema(DjangoObjectType):
    class Meta:
        model = Order
        fields = ['id', 'timestamp', 'placed', 'total_price', 'total_quantity', 'products']


class Query(graphene.ObjectType):
    order = graphene.List(OrderSchema)

    def resolve_order(root, info, **kwargs):
        return Order.objects.all()

schema = graphene.Schema(query=Query)