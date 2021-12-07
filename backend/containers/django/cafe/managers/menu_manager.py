from django.db import models

from ..models.category import Category


class DrinkMenuProxyManager(models.Manager):
    def get_queryset(self):
        drink_root_node: Category = Category.categories.get(name="Drink")
        return (
            super()
            .get_queryset()
            .filter(category__path__contains=f"{drink_root_node.path}")
        )
