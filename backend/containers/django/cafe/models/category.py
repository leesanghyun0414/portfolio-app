from django.db import models
from treebeard.mp_tree import MP_Node

from ..helpers import category_serialize

from ..querysets import CategoryQuerySet
from .common_info import CommonInfo


class Category(CommonInfo, MP_Node):
    class Meta:
        db_table = "cafe_menu_category"

        verbose_name_plural = "カテゴリー"

    name = models.CharField(max_length=30)

    categories = CategoryQuerySet.as_manager()

    node_order_by = ["name"]

    @classmethod
    def get_category(cls):
        return category_serialize(cls.dump_bulk())

    def __str__(self):
        return self.name
