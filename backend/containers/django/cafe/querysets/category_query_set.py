from django.db.models import QuerySet
from treebeard.mp_tree import MP_NodeQuerySet


class CategoryQuerySet(MP_NodeQuerySet):
    def leaf_categories(self):
        return self.filter(numchild=0)


class FoodProxyQuerySet(MP_NodeQuerySet):
    pass


class DrinkProxyQuerySet(MP_NodeQuerySet):
    pass
