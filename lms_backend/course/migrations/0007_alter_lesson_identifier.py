# Generated by Django 4.2 on 2023-04-17 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_lesson_identifier_alter_lesson_additional_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='identifier',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]