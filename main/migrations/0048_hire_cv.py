# Generated by Django 4.1 on 2023-01-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0047_remove_hire_cv"),
    ]

    operations = [
        migrations.AddField(
            model_name="hire",
            name="cv",
            field=models.FileField(blank=True, null=True, upload_to="cv/"),
        ),
    ]
