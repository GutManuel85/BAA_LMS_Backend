# Generated by Django 4.2 on 2023-05-07 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0037_alter_correctanswerquiz_correctanswer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correctanswerquiz',
            name='correctAnswer',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='correctanswerquiz',
            name='wrongAnswer1',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='correctanswerquiz',
            name='wrongAnswer2',
            field=models.TextField(max_length=300),
        ),
    ]