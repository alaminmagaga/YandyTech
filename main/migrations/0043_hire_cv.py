# Generated by Django 4.1 on 2023-01-10 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0042_article_new_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="hire",
            name="cv",
            field=models.FileField(default=1, upload_to="cv/"),
            preserve_default=False,
        ),
    ]
