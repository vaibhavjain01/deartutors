# Generated by Django 2.2.1 on 2019-05-07 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_auto_20190506_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='facebook_url',
            field=models.URLField(default='na@na.com'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='linkedin_url',
            field=models.URLField(default='na@na.com'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='twitter_url',
            field=models.URLField(default='na@na.com'),
        ),
        migrations.AlterField(
            model_name='service',
            name='self_webpage_link',
            field=models.URLField(default='na@na.com'),
        ),
    ]
