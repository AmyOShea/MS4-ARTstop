# Generated by Django 3.2.6 on 2021-09-26 17:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('video', models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('video_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.level')),
            ],
            options={
                'verbose_name_plural': 'Classes',
            },
        ),
    ]