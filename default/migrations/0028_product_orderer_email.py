# Generated by Django 4.2.9 on 2024-02-28 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0027_alter_product_kategoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='orderer_email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
