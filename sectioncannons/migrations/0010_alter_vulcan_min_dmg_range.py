# Generated by Django 5.0.1 on 2024-07-14 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectioncannons', '0009_alter_vulcan_barrel_spin_down_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulcan',
            name='min_dmg_range',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Дальность мин поражения'),
        ),
    ]
