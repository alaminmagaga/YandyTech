# Generated by Django 4.1 on 2022-09-24 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0023_blogcategory"),
    ]

    operations = [
        migrations.RenameModel(old_name="BlogCategory", new_name="HireCategory",),
    ]
