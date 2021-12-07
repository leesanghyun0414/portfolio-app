import os

from django.conf import settings
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.user.get_username()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


def upload_path(instance, filename):

    return os.path.join(
        "images",
        f"{instance.__class__.__name__.lower()}",
        f"user_{instance.author.user.id}",
        f"post_{instance.id}",
        filename,
    )


class Post(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tag = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    photo = models.ImageField(blank=True, upload_to=upload_path)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.id is None:
            uploaded_file = self.photo
            self.photo = None
            super().save(*args, **kwargs)
            self.photo = uploaded_file
            if "force_insert" in kwargs:
                kwargs.pop("force_insert")

        super().save(*args, **kwargs)


class PostBody(models.Model):
    class Meta:
        db_table = "blog_post_body"

    post = models.OneToOneField(Post, related_name="body", on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Like(models.Model):

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="like")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="like")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "post"], name="unique_like")
        ]
        db_table = "blog_post_like"

    def __str__(self):
        return str(self.post)
