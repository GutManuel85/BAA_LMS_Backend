# Generated by Django 4.2 on 2023-04-22 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0014_delete_quizorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('identifier', models.CharField(max_length=30, unique=True)),
                ('text_area', models.TextField(blank=True, null=True)),
                ('element1', models.TextField(blank=True, max_length=300, null=True)),
                ('element2', models.TextField(blank=True, max_length=300, null=True)),
                ('element3', models.TextField(blank=True, max_length=300, null=True)),
                ('element4', models.TextField(blank=True, max_length=300, null=True)),
                ('element5', models.TextField(blank=True, max_length=300, null=True)),
                ('element6', models.TextField(blank=True, max_length=300, null=True)),
                ('element7', models.TextField(blank=True, max_length=300, null=True)),
                ('element8', models.TextField(blank=True, max_length=300, null=True)),
                ('element9', models.TextField(blank=True, max_length=300, null=True)),
                ('element10', models.TextField(blank=True, max_length=300, null=True)),
                ('element11', models.TextField(blank=True, max_length=300, null=True)),
                ('element12', models.TextField(blank=True, max_length=300, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('review', 'Review'), ('published', 'Published')], default='draft', max_length=30)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quiz_order', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]