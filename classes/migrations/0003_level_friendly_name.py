# Generated by Django 3.2.6 on 2021-10-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20210928_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]