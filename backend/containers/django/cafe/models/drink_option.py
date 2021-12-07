from django.db import models

from cafe.models.common_info import CommonInfo


class Option(CommonInfo, models.Model):
    class Meta:
        db_table = "cafe_option"
