# Generated by Django 3.0.4 on 2020-03-09 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='Slug'),
        ),
    ]
