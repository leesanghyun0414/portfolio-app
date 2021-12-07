# Generated by Django 3.2.5 on 2021-11-16 06:16

import django.db.models.deletion
import django.db.models.manager
from django.db import migrations
from django.db import models

import cafe.helpers.path_helper


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("path", models.CharField(max_length=255, unique=True)),
                ("depth", models.PositiveIntegerField()),
                ("numchild", models.PositiveIntegerField(default=0)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=30)),
            ],
            options={
                "db_table": "cafe_menu_category",
            },
            managers=[
                ("categories", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                ("menu_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                (
                    "menu_type",
                    models.CharField(
                        choices=[("DK", "Drink"), ("FD", "Food")],
                        max_length=2,
                        unique=True,
                    ),
                ),
                ("calorie", models.PositiveSmallIntegerField()),
                ("price", models.PositiveSmallIntegerField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to=cafe.helpers.path_helper.upload_path
                    ),
                ),
                ("is_active", models.BooleanField(default=False)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="menu",
                        to="cafe.category",
                    ),
                ),
            ],
            options={
                "db_table": "cafe_menu",
            },
        ),
        migrations.CreateModel(
            name="Drink",
            fields=[
                (
                    "menu",
                    models.OneToOneField(
                        db_column="menu_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="drink_id",
                        serialize=False,
                        to="cafe.menu",
                    ),
                ),
                ("has_cold", models.BooleanField()),
                ("has_hot", models.BooleanField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "cafe_drink_item",
            },
        ),
        migrations.CreateModel(
            name="Food",
            fields=[
                (
                    "menu",
                    models.OneToOneField(
                        db_column="menu_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="food_id",
                        serialize=False,
                        to="cafe.menu",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "cafe_food_item",
            },
        ),
        migrations.AddConstraint(
            model_name="menu",
            constraint=models.UniqueConstraint(
                fields=("menu_id", "menu_type"), name="unique_menu"
            ),
        ),
        migrations.AddConstraint(
            model_name="menu",
            constraint=models.CheckConstraint(
                check=models.Q(("menu_type__in", ["DK", "FD"])),
                name="cafe_menu_menu_type_check",
            ),
        ),
        migrations.AddField(
            model_name="food",
            name="menu_type",
            field=models.ForeignKey(
                db_column="menu_type",
                default="FD",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="food_type",
                to="cafe.menu",
                to_field="menu_type",
            ),
        ),
        migrations.AddField(
            model_name="drink",
            name="menu_type",
            field=models.ForeignKey(
                db_column="menu_type",
                default="DK",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="drink_type",
                to="cafe.menu",
                to_field="menu_type",
            ),
        ),
        migrations.AddConstraint(
            model_name="food",
            constraint=models.UniqueConstraint(
                fields=("menu", "menu_type"), name="unique_food_menu"
            ),
        ),
        migrations.AddConstraint(
            model_name="food",
            constraint=models.CheckConstraint(
                check=models.Q(("menu_type__exact", "FD")),
                name="cafe_food_item_food_type_check",
            ),
        ),
        migrations.AddConstraint(
            model_name="drink",
            constraint=models.UniqueConstraint(
                fields=("menu", "menu_type"), name="unique_drink_menu"
            ),
        ),
        migrations.AddConstraint(
            model_name="drink",
            constraint=models.CheckConstraint(
                check=models.Q(("menu_type__exact", "DK")),
                name="cafe_drink_item_menu_type_check",
            ),
        ),
    ]
