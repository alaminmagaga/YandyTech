# Generated by Django 4.1 on 2022-09-24 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_scholarship_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scholarship",
            name="title",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
