# Generated by Django 4.1 on 2022-10-11 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0029_article"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article", old_name="sub_title", new_name="slug",
        ),
    ]
