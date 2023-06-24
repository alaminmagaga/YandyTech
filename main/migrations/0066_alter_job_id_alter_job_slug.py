# Generated by Django 4.2 on 2023-04-22 23:24

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0065_alter_job_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="job",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=models.AutoField(primary_key=True, serialize=False),
                editable=False,
                null=True,
                populate_from="position",
                unique=True,
            ),
        ),
    ]