# Generated by Django 4.2 on 2023-05-08 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0038_alter_correctanswerquiz_correctanswer_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['my_order'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
