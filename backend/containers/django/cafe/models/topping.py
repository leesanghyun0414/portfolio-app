"""
Drink Topping Model.
"""
from django.db import models

from cafe.models.common_info import CommonInfo


class Topping(CommonInfo, models.Model):
    class Meta:
        db_table = "cafe_topping"
        verbose_name = "トッピング"
        verbose_name_plural = "トッピング"

    topping_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=30, name="description", null=False)
    constant_addition = models.IntegerField(null=False, default=50, name="Addition Fee")

    def __str__(self):
        return str(self.description)
