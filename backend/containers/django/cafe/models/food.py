from django.db import models

from ..types import MenuType
from .common_info import CommonInfo
from .menu import Menu


class Food(CommonInfo, models.Model):
    class Meta:
        db_table = "cafe_food_item"
        verbose_name_plural = "Food Options"

        constraints = [
            models.UniqueConstraint(
                fields=["menu", "menu_type"], name="unique_food_menu"
            ),
            models.CheckConstraint(
                check=models.Q(menu_type__exact=MenuType.FOOD),
                name=f"{db_table}_food_type_check",
            ),
        ]
        verbose_name_plural = "Food Options"

    menu = models.OneToOneField(
        Menu,
        primary_key=True,
        to_field="menu_id",
        null=False,
        on_delete=models.CASCADE,
        related_name="food_id",
        db_column="menu_id",
    )

    menu_type = models.ForeignKey(
        Menu,
        db_column="menu_type",
        to_field="menu_type",
        null=False,
        on_delete=models.CASCADE,
        related_name="food_type",
        default=MenuType.FOOD,
    )
