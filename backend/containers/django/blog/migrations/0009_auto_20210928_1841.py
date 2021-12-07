# Generated by Django 3.2.7 on 2021-09-28 09:41

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_post_total_like"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="total_like",
        ),
        migrations.AlterField(
            model_name="like",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="blog.post"
            ),
        ),
        migrations.AlterField(
            model_name="like",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="blog.profile"
            ),
        ),
        migrations.AddConstraint(
            model_name="like",
            constraint=models.UniqueConstraint(
                fields=("user", "post"), name="unique_like"
            ),
        ),
    ]
