# Generated by Django 3.2.6 on 2021-09-02 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='artist',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category'),
        ),
    ]
