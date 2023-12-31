# Generated by Django 4.2 on 2023-05-12 10:47

import course.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0049_alter_lesson_image1_alter_lesson_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='uploads/lesson_pdf', validators=[course.validators.validate_file_size, course.validators.validate_pdf_file_extension]),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads', validators=[course.validators.validate_file_size]),
        ),
    ]
