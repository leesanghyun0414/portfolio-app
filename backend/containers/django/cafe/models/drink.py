"""
Drink menu Model
"""
from django.db import models

from cafe.types import MenuType

from .common_info import CommonInfo
from .menu import Menu
from .size import Size


class Drink(CommonInfo, models.Model):
    class Meta:

        db_table = "cafe_drink_item"

        constraints = [
            models.UniqueConstraint(
                fields=["menu", "menu_type"], name="unique_drink_menu"
            ),
            models.CheckConstraint(
                check=models.Q(menu_type__exact=MenuType.DRINK),
                name=f"{db_table}_type_check",
            ),
            models.CheckConstraint(
                check=~(
                    models.Q(has_hot__exact=False) & models.Q(has_cold__exact=False)
                ),
                name=f"{db_table}_never_has_false_both_check",
            ),
            models.CheckConstraint(
                check=~(
                    models.Q(has_cold__exact=False) & models.Q(has_hot__exact=False)
                ),
                name=f"{db_table}_has_cold_and_has_hot_never_false_both_check",
            ),
        ]
        verbose_name_plural = "Drink Options"

        verbose_name = "Drink Option"

    menu = models.OneToOneField(
        Menu,
        primary_key=True,
        to_field="menu_id",
        null=False,
        on_delete=models.CASCADE,
        related_name="drink_id",
        db_column="menu_id",
    )

    menu_type = models.ForeignKey(
        Menu,
        to_field="menu_type",
        null=False,
        on_delete=models.CASCADE,
        related_name="drink_type",
        default=MenuType.DRINK,
        db_column="menu_type",
    )
    size = models.ManyToManyField(Size, related_name="size", blank=True)
    has_cold = models.BooleanField(null=False, verbose_name="Cold", default=False)
    has_hot = models.BooleanField(null=False, verbose_name="Hot", default=False)

    def __str__(self):
        return self.menu.name
