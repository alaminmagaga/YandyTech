# Generated by Django 4.1 on 2022-09-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_fellowship"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
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
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("website", models.CharField(blank=True, max_length=255, null=True)),
                ("eventdate", models.CharField(blank=True, max_length=255, null=True)),
                ("deadline", models.CharField(blank=True, max_length=255, null=True)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
