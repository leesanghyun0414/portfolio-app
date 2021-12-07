from django.db import models
from treebeard.mp_tree import MP_Node

from ..querysets import CategoryQuerySet
from .common_info import CommonInfo


class Category(CommonInfo, MP_Node):
    class Meta:
        db_table = "cafe_menu_category"

        verbose_name_plural = "カテゴリー"

    name = models.CharField(max_length=30)

    categories = CategoryQuerySet.as_manager()

    node_order_by = ["name"]

    def __str__(self):
        return self.name
