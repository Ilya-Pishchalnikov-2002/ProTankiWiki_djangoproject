# Generated by Django 5.0.1 on 2024-07-20 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sectionranks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Название')),
                ('slug_name', models.SlugField(blank=True, max_length=20)),
                ('image_icon', models.ImageField(upload_to='Paints', verbose_name='Иконка в гараже')),
                ('image_view', models.ImageField(upload_to='Paints', verbose_name='Вид на танке')),
                ('cost', models.IntegerField(verbose_name='Стоимость')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание в гараже')),
                ('have_resist', models.BooleanField(verbose_name='Имеет защиту от пушек')),
                ('resist_smoky', models.SmallIntegerField(blank=True, null=True, verbose_name='Зашита от Смоки')),
                ('resist_firebird', models.SmallIntegerField(blank=True, null=True, verbose_name='Зашита от Огнемёта')),
                ('resist_twins', models.SmallIntegerField(blank=True, null=True, verbose_name='Зашита от Твинса')),
                ('resist_hammer', models.SmallIntegerField(blank=True, null=True, verbose_name='Зашита от Молота')),
                ('resist_railgun', models.SmallIntegerField(blank=True, null=True, verbose_name='Зашита от Рельсы')),
                ('resist_isida', models.SmallIntegerField(blank=True, null=True, verbose_name='Зашита от Изиды')),
                ('resist_vulcan', models.SmallIntegerField(blank=True, null=True, verbose_name='Зашита от Вулкана')),
                ('resist_thunder', models.SmallIntegerField(blank=True, null=True, verbose_name='Зашита от Грома')),
                ('resist_freeze', models.SmallIntegerField(blank=True, null=True, verbose_name='Зашита от Фриза')),
                ('resist_ricochet', models.SmallIntegerField(blank=True, null=True, verbose_name='Зашита от Рикошета')),
                ('resist_shaft', models.SmallIntegerField(blank=True, null=True, verbose_name='Зашита от Шафта')),
                ('resist_mines', models.SmallIntegerField(blank=True, null=True, verbose_name='Зашита от мин')),
                ('resist_all', models.SmallIntegerField(blank=True, null=True, verbose_name='Зашита от всех пушек и мин')),
                ('rank_required', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sectionranks.rank', verbose_name='Требуемое звание')),
            ],
            options={
                'verbose_name': 'Краска',
                'verbose_name_plural': 'Краски',
            },
        ),
    ]
