# Generated by Django 4.0.3 on 2022-04-17 10:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_operatingsystems_platform_ram_alter_brand_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'verbose_name': 'Звезда', 'verbose_name_plural': 'Звезды'},
        ),
        migrations.AddField(
            model_name='reviews',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='ram',
            name='count',
            field=models.IntegerField(verbose_name='Количество ядер'),
        ),
        migrations.AlterField(
            model_name='ratingstar',
            name='value',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5, 'Кол-во звезд не больше 5')], verbose_name='Значение'),
        ),
    ]
