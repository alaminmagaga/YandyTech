# Generated by Django 3.2.3 on 2022-11-11 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_alter_job_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='hire',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]