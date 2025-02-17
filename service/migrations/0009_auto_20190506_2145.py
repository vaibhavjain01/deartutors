# Generated by Django 2.2.1 on 2019-05-07 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_brand_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutus',
            old_name='description',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='desc',
            new_name='long_desc',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='short_description',
            field=models.TextField(default='abc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='short_desc',
            field=models.TextField(default='acs'),
            preserve_default=False,
        ),
    ]
