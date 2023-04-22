# Generated by Django 4.2 on 2023-04-22 23:26

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0067_alter_job_id_alter_job_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default="this is a house",
                editable=False,
                null=True,
                populate_from="position",
                unique=True,
            ),
        ),
    ]
