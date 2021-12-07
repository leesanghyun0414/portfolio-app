from Django.DB import models

from blog import query_set

# class PostQuerySet(models.query.QuerySet):
#     def get_all_published_post(self) -> models.query.QuerySet:
#         return self.filter(published=True)


class PostManager(models.Manager):
    def get_queryset(self):
        return query_set.PostQuerySet(self.model, using=self._db)

    def get_all_published_post(self):
        return self.get_queryset().get_all_published_post()
