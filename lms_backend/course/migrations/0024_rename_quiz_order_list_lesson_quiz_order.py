# Generated by Django 4.2 on 2023-04-29 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0023_remove_lesson_quiz_order_list_lesson_quiz_order_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='quiz_order_list',
            new_name='quiz_order',
        ),
    ]
