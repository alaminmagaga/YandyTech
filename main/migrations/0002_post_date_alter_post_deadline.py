# Generated by Django 4.1 on 2022-09-24 10:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="deadline",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
