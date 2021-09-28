# Generated by Django 3.2.6 on 2021-09-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_artist_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='fb_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='ig_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='linkedin_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='website_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]