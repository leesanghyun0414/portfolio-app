from django.db.models.query import QuerySet


class PostQuerySet(QuerySet):
    def get_all_published_post(self) -> QuerySet:
        return self.filter(published=True)
