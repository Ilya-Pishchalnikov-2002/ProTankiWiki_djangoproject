# Generated by Django 5.0.1 on 2024-07-05 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectioncannons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cannon',
            name='slug_name',
            field=models.SlugField(blank=True, max_length=10, unique=True),
        ),
    ]
