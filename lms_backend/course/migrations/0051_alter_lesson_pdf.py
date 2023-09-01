# Generated by Django 4.2 on 2023-05-12 12:50

import course.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0050_lesson_pdf_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='uploads/lesson_pdf', validators=[course.validators.validate_pdf_file_size, course.validators.validate_pdf_file_extension]),
        ),
    ]
