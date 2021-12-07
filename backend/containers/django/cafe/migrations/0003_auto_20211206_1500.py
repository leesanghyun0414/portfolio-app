# Generated by Django 3.2.5 on 2021-12-06 06:00

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("cafe", "0002_auto_20211116_1523"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "カテゴリー"},
        ),
        migrations.AlterModelOptions(
            name="drink",
            options={"verbose_name_plural": "Drink Options"},
        ),
        migrations.AlterModelOptions(
            name="food",
            options={"verbose_name_plural": "Food Options"},
        ),
        migrations.AlterModelOptions(
            name="menu",
            options={"verbose_name": "メニュー", "verbose_name_plural": "メニュー"},
        ),
        migrations.RemoveConstraint(
            model_name="drink",
            name="cafe_drink_item_menu_type_check",
        ),
        migrations.RemoveConstraint(
            model_name="menu",
            name="cafe_menu_menu_type_check",
        ),
        migrations.AlterField(
            model_name="drink",
            name="has_cold",
            field=models.BooleanField(default=False, verbose_name="Cold"),
        ),
        migrations.AlterField(
            model_name="drink",
            name="has_hot",
            field=models.BooleanField(default=False, verbose_name="Hot"),
        ),
        migrations.AlterField(
            model_name="menu",
            name="is_active",
            field=models.BooleanField(default=False, verbose_name="Release"),
        ),
        migrations.AddConstraint(
            model_name="drink",
            constraint=models.CheckConstraint(
                check=models.Q(("menu_type__exact", "DK")),
                name="cafe_drink_item_type_check",
            ),
        ),
        migrations.AddConstraint(
            model_name="drink",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("has_hot__exact", False), ("has_cold__exact", False), _negated=True
                ),
                name="cafe_drink_item_never_has_false_both_check",
            ),
        ),
        migrations.AddConstraint(
            model_name="drink",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("has_cold__exact", False), ("has_hot__exact", False), _negated=True
                ),
                name="cafe_drink_item_has_cold_and_has_hot_never_false_both_check",
            ),
        ),
        migrations.AddConstraint(
            model_name="menu",
            constraint=models.CheckConstraint(
                check=models.Q(("menu_type__in", ["DK", "FD"])),
                name="cafe_menu_type_check",
            ),
        ),
    ]
