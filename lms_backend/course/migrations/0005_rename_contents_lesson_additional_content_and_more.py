# Generated by Django 4.2 on 2023-04-17 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_course_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='contents',
            new_name='additional_content',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='long_description',
            new_name='text_area',
        ),
    ]
