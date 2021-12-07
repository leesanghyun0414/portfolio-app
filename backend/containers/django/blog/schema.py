"""
GraphQL API
"""
import graphene
from django.contrib.auth import get_user_model
from django.db import transaction
from graphene import ObjectType
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_auth import mutations
from graphql_auth.schema import MeQuery
from graphql_auth.schema import UserQuery

from blog import models


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Profile


class LikeType(DjangoObjectType):
    class Meta:
        model = models.Like


class PostType(DjangoObjectType):
    class Meta:
        model = models.Post


class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag


class PostBodyType(DjangoObjectType):
    class Meta:
        model = models.PostBody


class TagNode(DjangoObjectType):
    class Meta:
        model = models.Tag
        filter_fields = {"name": ["exact", "icontains"]}
        interfaces = (relay.Node,)


class AuthMutation(ObjectType):
    register = mutations.Register.Field()


class Query(MeQuery, UserQuery, ObjectType):
    all_posts = graphene.List(PostType)
    # all_tags = graphene.List(TagType)
    tag = relay.Node.Field(TagNode)
    all_tags = DjangoFilterConnectionField(TagNode)
    author_by_user = graphene.Field(AuthorType, username=graphene.String())
    post_by_author = graphene.List(PostType, username=graphene.String())
    post_by_tag = graphene.List(PostType, tag=graphene.String())
    total_like_count_by_post = graphene.Int(post_id=graphene.Int(required=True))
    total_like_count_by_user = graphene.Int(post_id=graphene.Int(required=True))
    all_liked_post_by_user = graphene.List(PostType, user_id=graphene.ID(required=True))
    post_body = graphene.Field(PostBodyType, post_id=graphene.ID(required=True))
    post_by_id = graphene.Field(PostType, post_id=graphene.ID(required=True))

    def resolve_post_by_id(root, info, post_id: graphene.ID):
        return models.Post.objects.get(id=post_id)

    def resolve_post_body(root, info, post_id: graphene.ID):
        return models.Post.objects.get(id=post_id).body

    def resolve_total_like_count_by_post(root, info, post_id: graphene.Int):
        post = models.Post.objects.prefetch_related("like").filter(id=post_id).get()
        return post.like.count()

    # def resolve_all_tags(root, info):
    #     return models.Tag.objects.all()

    def resolve_all_liked_post_by_user(root, info, user_id):
        return models.Post.objects.prefetch_related("like").filter(
            like__user_id=user_id
        )

    def resolve_all_posts(root, info):
        return (
            models.Post.objects.prefetch_related("tag").select_related("author").all()
        )

    def resolve_author_by_username(root, info, username):
        return models.Profile.objects.select_related("user").get(
            user__username=username
        )

    def resolve_post_by_author(root, info, username):
        return (
            models.Post.objects.prefetch_related("tag")
            .select_related("author")
            .filter(author__user__username=username)
        )

    def resolve_posts_by_tag(root, info, tag):
        return (
            models.Post.objects.prefetch_related("tag")
            .select_related("author")
            .filter(tag__name__iexact=tag)
        )


class LikePost(graphene.Mutation):
    is_liked = graphene.Boolean()
    user_id = graphene.ID()
    post_id = graphene.ID()

    class Arguments:
        post_id = graphene.ID()
        user_id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, user_id, post_id):
        like = models.Like.objects.filter(user_id=user_id, post_id=post_id)
        if like.exists():
            like.delete()
            return cls(is_liked=False, user_id=user_id, post_id=post_id)
        models.Like(user_id=user_id, post_id=post_id).save()
        return LikePost(is_liked=True, user_id=user_id, post_id=post_id)


class CreatePost(graphene.Mutation):
    body = graphene.String()
    post = graphene.Field(PostType)

    class Arguments:
        title = graphene.String()
        subtitle = graphene.String()
        text = graphene.String()
        username = graphene.String()

    @classmethod
    def mutate(cls, root, info, username, title, subtitle, text):
        author = models.Profile.objects.select_related("user").get(
            user__username=username
        )
        with transaction.atomic():
            post = models.Post(
                title=title,
                subtitle=subtitle,
                author=author,
            )
            post.save()

            post_body = models.PostBody(post_id=post.id, text=text)
            post_body.save()

        return cls(post=post, body=text)


class Mutation(AuthMutation, ObjectType):
    like_post = LikePost.Field()
    create_post = CreatePost.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
