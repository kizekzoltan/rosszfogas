# Generated by Django 5.0.1 on 2024-03-13 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("default", "0031_customer_banned_ad_customer_banned_forum"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="leiras",
            field=models.CharField(
                blank=True,
                default="Ehhez a témához nem tartozik leírás",
                max_length=150,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="topic",
            name="title",
            field=models.CharField(max_length=80, null=True),
        ),
    ]
