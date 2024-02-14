# Generated by Django 4.2.9 on 2024-02-14 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0013_topic_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='orderer_location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='orderer_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='orderer_phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]