# Generated by Django 4.2.9 on 2024-02-18 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0020_alter_topic_leiras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=80),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
