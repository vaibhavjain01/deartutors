# Generated by Django 2.2.1 on 2019-05-07 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_auto_20190506_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sender_name', models.TextField(default='')),
                ('sender_email', models.TextField(default='')),
                ('subject', models.TextField(default='')),
                ('msg', models.TextField(default='')),
                ('msg_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('request_date', models.DateField()),
                ('request_time', models.TimeField()),
                ('request_duration', models.PositiveIntegerField()),
                ('service_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='service.Service')),
            ],
        ),
    ]
