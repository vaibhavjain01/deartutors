# Generated by Django 2.2.1 on 2019-05-07 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_auto_20190506_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='facebook_url',
            field=models.URLField(default='na@na.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brand',
            name='linkedin_url',
            field=models.URLField(default='na@na.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brand',
            name='twitter_url',
            field=models.URLField(default='na@na.com'),
            preserve_default=False,
        ),
    ]
