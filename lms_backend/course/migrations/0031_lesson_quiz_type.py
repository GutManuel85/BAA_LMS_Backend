# Generated by Django 4.2 on 2023-04-30 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0030_remove_lesson_quiz_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='quiz_type',
            field=models.CharField(choices=[('no_quiz', 'No quiz'), ('sorting_quiz', 'Sorting quiz'), ('correct_answer_quiz', 'Correct answer quiz')], default='no_quiz', max_length=30),
        ),
    ]
