# Generated by Django 3.2.6 on 2021-09-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]