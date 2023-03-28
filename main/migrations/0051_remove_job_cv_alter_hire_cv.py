# Generated by Django 4.1 on 2023-01-21 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0050_remove_hire_cv_upload_hire_cv"),
    ]

    operations = [
        migrations.RemoveField(model_name="job", name="cv",),
        migrations.AlterField(
            model_name="hire",
            name="cv",
            field=models.FileField(blank=True, null=True, upload_to="cv/"),
        ),
    ]