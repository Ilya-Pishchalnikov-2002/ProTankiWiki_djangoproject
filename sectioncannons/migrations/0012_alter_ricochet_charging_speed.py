# Generated by Django 5.0.1 on 2024-07-15 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectioncannons', '0011_alter_ricochet_min_dmg_range_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ricochet',
            name='charging_speed',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Перезарядка всего баллона'),
        ),
    ]
