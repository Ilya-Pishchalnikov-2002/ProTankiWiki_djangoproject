# Generated by Django 5.0.1 on 2024-08-11 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectionranks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='slug_name',
            field=models.SlugField(blank=True, max_length=20),
        ),
    ]
