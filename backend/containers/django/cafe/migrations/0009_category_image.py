# Generated by Django 3.2.5 on 2022-02-23 02:02

import cafe.helpers.path_helper
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0008_rename_name_topping_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to=cafe.helpers.path_helper.upload_path),
        ),
    ]