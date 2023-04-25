# Generated by Django 4.2 on 2023-04-22 19:06

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0063_remove_article_new_slug_alter_article_slug_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=None,
                editable=False,
                null=True,
                populate_from="position",
                unique=True,
            ),
        ),
    ]
