# Generated by Django 4.2 on 2023-04-16 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='course',
            name='created_at',
        ),
        migrations.AddField(
            model_name='lesson',
            name='contents',
            field=models.ManyToManyField(to='course.content'),
        ),
    ]