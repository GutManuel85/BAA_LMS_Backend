# Generated by Django 4.2 on 2023-05-09 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0043_freetextquiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='free_text_quiz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.freetextquiz'),
        ),
    ]
