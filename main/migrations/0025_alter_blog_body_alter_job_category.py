# Generated by Django 4.1 on 2022-09-24 21:44

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0024_rename_blogcategory_hirecategory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="body",
            field=ckeditor.fields.RichTextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="category",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
