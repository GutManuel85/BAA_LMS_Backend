# Generated by Django 4.2 on 2023-05-12 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0053_multiplechoicequiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='multiple_choice_quiz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.multiplechoicequiz'),
        ),
    ]
