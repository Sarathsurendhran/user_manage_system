# Generated by Django 5.1.4 on 2025-01-09 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ]
