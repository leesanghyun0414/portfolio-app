from django.db.models import Manager

from .querysets import CategoryQuerySet


class CategoryManager(Manager):
    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def leaf_categories(self):
        self.get_queryset().leaf_categories()
