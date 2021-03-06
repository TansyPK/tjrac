# Generated by Django 2.1 on 2019-04-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0002_selectteacheroperations'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectCommentOperations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.IntegerField()),
                ('owner', models.IntegerField()),
                ('content', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
