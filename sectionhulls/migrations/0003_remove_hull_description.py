# Generated by Django 5.0.1 on 2024-08-11 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sectionhulls', '0002_dictator_hornet_hunter_mammoth_titan_vasp_viking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hull',
            name='description',
        ),
    ]
