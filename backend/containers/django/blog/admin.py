from django.contrib import admin

from blog.models import Post
from blog.models import PostBody
from blog.models import Profile
from blog.models import Tag


class PostBodyInline(admin.TabularInline):
    model = PostBody


# Register your models here.

# @admin.register(Profile)
# class ProfileAmin(admin.ModelAdmin):
#     model = Profile
#
#
# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     model = Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [PostBodyInline]
    list_display = (
        "id",
        "title",
        "subtitle",
        "publish_date",
        "published",
    )

    list_filter = (
        "published",
        "publish_date",
    )

    list_editable = (
        "title",
        "subtitle",
        "publish_date",
        "published",
    )

    date_hierarchy = "publish_date"
    save_on_top = True
