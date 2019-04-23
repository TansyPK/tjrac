# Generated by Django 2.1 on 2019-04-23 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectTeacherOperations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selector_id', models.IntegerField()),
                ('teacher_id', models.IntegerField()),
                ('room', models.IntegerField()),
                ('status', models.IntegerField()),
                ('interview_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
