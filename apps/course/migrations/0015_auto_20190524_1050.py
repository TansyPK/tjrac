# Generated by Django 2.1 on 2019-05-24 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_auto_20190524_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 24, 10, 50, 17, 217911)),
        ),
        migrations.AlterField(
            model_name='course',
            name='interview_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 24, 10, 50, 17, 217911)),
        ),
    ]
