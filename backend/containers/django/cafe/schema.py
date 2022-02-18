import graphene
from graphene import Field
from graphene import ObjectType
from graphene import String
from graphene import relay
from graphene.types.generic import GenericScalar
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_auth import mutations
from graphql_auth.schema import MeQuery
from graphql_auth.schema import UserQuery

from .models import *


class MenuType(DjangoObjectType):
    class Meta:
        model = Menu
        fields = (
            "id",
            "name",
            "calorie",
            "image",
            "price",
            "category",
            "drink_type",
            "food_type",
        )


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "path", "numchild")


class Query(ObjectType):
    menu_path = graphene.Field(MenuType, menu_id=graphene.ID(required=True))
    all_menu = graphene.List(MenuType)
    all_category = GenericScalar()
    menu_by_category_id = graphene.List(
        MenuType, category_id=graphene.ID(required=True)
    )
    menu_by_id = graphene.Field(
        MenuType,
        menu_id=graphene.ID(required=True),
        is_released=graphene.Boolean(default_value=True),
    )

    def resolve_menu_by_category_id(root, info, category_id):
        return Menu.objects.select_related("category").filter(category=category_id)

    def resolve_menu_by_id(root, info, menu_id: graphene.ID(), is_active):
        return Menu.objects.get(pk=menu_id, is_active=is_active)

    def resolve_all_category(root, info):
        return Category.get_category()

    def resolve_all_menu(root, info):
        return Menu.objects.select_related("category").all()

    def resolve_menu_path(parent, info, menu_id):
        img = Menu.objects.get(pk=menu_id)
        img.image = info.context.build_absolute_uri(img.image)
        image = info.context.build_absolute_uri(img.image)
        return img


schema = graphene.Schema(query=Query)
