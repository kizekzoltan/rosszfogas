# Generated by Django 4.2.9 on 2024-02-18 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0016_topic_leiras_alter_comment_content_alter_topic_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='leiras',
            field=models.CharField(default='', max_length=75, null=True),
        ),
    ]
