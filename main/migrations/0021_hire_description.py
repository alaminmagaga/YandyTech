# Generated by Django 4.1 on 2022-09-24 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0020_hire_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="hire",
            name="description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
