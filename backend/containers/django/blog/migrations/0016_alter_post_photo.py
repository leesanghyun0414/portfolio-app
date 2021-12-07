# Generated by Django 3.2.5 on 2021-10-06 00:32

from django.db import migrations
from django.db import models

import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0015_post_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="photo",
            field=models.ImageField(blank=True, upload_to=blog.models.upload_path),
        ),
    ]
