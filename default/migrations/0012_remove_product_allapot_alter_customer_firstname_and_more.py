# Generated by Django 4.2.9 on 2024-02-13 14:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0011_customer_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='allapot',
        ),
        migrations.AlterField(
            model_name='customer',
            name='firstname',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lastname',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='location',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='', max_length=12, null=True, validators=[django.core.validators.RegexValidator(code='ervenytelen_szam', message='A telefonszám csak számokat, illetve + karaktert tartalmazhat', regex='^[\\d()+-]*$')]),
        ),
    ]
