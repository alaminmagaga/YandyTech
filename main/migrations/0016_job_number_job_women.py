# Generated by Django 4.1 on 2022-09-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0015_job"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="number",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="job",
            name="women",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
