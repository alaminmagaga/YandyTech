# Generated by Django 4.1 on 2022-09-24 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_scholarship_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="scholarship", old_name="image", new_name="header_image",
        ),
    ]
