# Generated by Django 3.2.3 on 2022-12-16 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_auto_20221215_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(default='YandyTech', max_length=1000),
        ),
    ]