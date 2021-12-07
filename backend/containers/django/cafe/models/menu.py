from django.db import models

from ..helpers.path_helper import upload_path
from ..managers.menu_manager import DrinkMenuProxyManager
from ..types import MenuType
from .category import Category
from .common_info import CommonInfo


class Menu(CommonInfo, models.Model):
    class Meta:
        db_table = "cafe_menu"
        constraints = [
            models.UniqueConstraint(
                fields=["menu_id", "menu_type"], name="unique_menu"
            ),
            models.CheckConstraint(
                check=models.Q(menu_type__in=MenuType.values),
                name=f"{db_table}_type_check",
            ),
        ]
        verbose_name_plural = "メニュー"
        verbose_name = "メニュー"

    def image_tag(self):
        from django.utils.html import mark_safe

        try:
            return mark_safe(
                f'<img src="{self.image.url}" width="100px" height"100px"/>'
            )
        except ValueError:
            return mark_safe(f'<img src="None" width="100px" height"100px"/>')

    image_tag.short_description = "Image"

    menu_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    menu_type = models.CharField(
        max_length=2, choices=MenuType.choices, null=False, unique=True
    )
    calorie = models.PositiveSmallIntegerField(null=False)
    price = models.PositiveSmallIntegerField(null=False)
    image = models.ImageField(upload_to=upload_path, blank=True)
    category = models.ForeignKey(
        Category,
        related_name="menu",
        on_delete=models.PROTECT,
    )
    is_active = models.BooleanField(null=False, default=False, verbose_name="Release")

    def __str__(self):
        return self.name
