# Generated by Django 2.1 on 2019-05-21 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20190521_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 21, 13, 31, 36, 298746)),
        ),
        migrations.AlterField(
            model_name='course',
            name='interview_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 21, 13, 31, 36, 298721)),
        ),
    ]
