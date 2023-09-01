# Generated by Django 4.2 on 2023-05-07 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0033_lesson_youtube_video_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='correctanswerquiz',
            name='identifier',
        ),
        migrations.RemoveField(
            model_name='sortingquiz',
            name='identifier',
        ),
        migrations.AlterField(
            model_name='sortingquiz',
            name='element1',
            field=models.TextField(blank=True, default='element1', max_length=300),
        ),
        migrations.AlterField(
            model_name='sortingquiz',
            name='element2',
            field=models.TextField(blank=True, default='element2', max_length=300),
        ),
        migrations.AlterField(
            model_name='sortingquiz',
            name='element3',
            field=models.TextField(blank=True, default='element3', max_length=300),
        ),
    ]
