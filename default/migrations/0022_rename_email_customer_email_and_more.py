# Generated by Django 5.0.1 on 2024-02-22 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0021_alter_product_description_alter_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='lastname',
            new_name='Keresztnév',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='location',
            new_name='Lakcím',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='phone',
            new_name='Telefonszám',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='firstname',
            new_name='Vezetéknév',
        ),
    ]
