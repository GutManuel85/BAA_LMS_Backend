# Generated by Django 4.2 on 2023-04-17 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_alter_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
