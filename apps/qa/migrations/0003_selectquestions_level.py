# Generated by Django 2.1 on 2019-04-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20190423_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectquestions',
            name='level',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]