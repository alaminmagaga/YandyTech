# Generated by Django 4.1 on 2022-09-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0021_hire_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="hire",
            name="category",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
