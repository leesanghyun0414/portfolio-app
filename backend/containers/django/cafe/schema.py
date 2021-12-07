# import graphene
# from graphene import ObjectType, String, Field
# from graphene import relay
# from graphene_django import DjangoObjectType
# from graphene_django.filter import DjangoFilterConnectionField
# from graphql_auth import mutations
# from graphql_auth.schema import MeQuery
# from graphql_auth.schema import UserQuery
#
# from cafe import models
#
#
# class MenuType(DjangoObjectType):
#     path = Field(String)
#
#     class Meta:
#         model = models.Menu
#         fields = ("id", "name", "calorie", "image", "price")
#
#
# class Query(ObjectType):
#     menu_path = graphene.Field(MenuType, menu_id=graphene.ID(required=True))
#     all_menu = graphene.List(MenuType)
#
#     def resolve_all_menu(root, info):
#         return models.Menu.objects.select_related("category").all()
#
#     def resolve_menu_path(parent, info, menu_id):
#         img = models.Menu.objects.get(pk=menu_id)
#         img.image = info.context.build_absolute_uri(img.image)
#         image = info.context.build_absolute_uri(img.image)
#         return img
#
#
# schema = graphene.Schema(query=Query)
