# Generated by Django 2.1 on 2019-05-21 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0003_selectcommentoperations'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectteacheroperations',
            name='course_id',
            field=models.IntegerField(default=0),
        ),
    ]
