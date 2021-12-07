"""
Drink Size model.
Drink Size dependencies to DrinkSizeType.
see also cafe.types.DrinkSize
"""
from django.db import models

from ..types import DrinkSizeType
from .common_info import CommonInfo


class Size(CommonInfo, models.Model):
    class Meta:
        db_table = "cafe_size"
        verbose_name = "サイズ"
        verbose_name_plural = "サイズ"

    size_id = models.AutoField(primary_key=True)
    description = models.CharField(
        max_length=20,
        null=False,
        verbose_name="Name",
        choices=DrinkSizeType.choices,
        unique=True,
    )
    constant_addition = models.IntegerField(null=False, default=30)

    def __str__(self):
        return str(self.description)
