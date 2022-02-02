# Generated by Django 4.0.1 on 2022-02-01 06:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
