# Generated by Django 4.1 on 2023-01-21 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0045_job_cv_alter_hire_image"),
    ]

    operations = [
        migrations.RemoveField(model_name="hire", name="image",),
        migrations.AlterField(
            model_name="hire",
            name="cv",
            field=models.FileField(default="chevening.png", upload_to="cv/"),
        ),
    ]
