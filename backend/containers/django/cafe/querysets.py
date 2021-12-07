from django.db.models import QuerySet


class CategoryQuerySet(QuerySet):
    def leaf_categories(self):
        return self.filter(numchild=0)
