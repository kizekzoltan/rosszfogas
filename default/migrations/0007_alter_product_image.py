# Generated by Django 4.2.9 on 2024-02-11 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='default/images/'),
        ),
    ]
