# Generated by Django 4.0.3 on 2022-04-21 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_reviews_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operatingsystems',
            options={'verbose_name': 'Операционная система', 'verbose_name_plural': 'Операционные системы'},
        ),
        migrations.AlterModelOptions(
            name='platform',
            options={'verbose_name': 'Платформа', 'verbose_name_plural': 'Платформы'},
        ),
        migrations.AlterModelOptions(
            name='ram',
            options={'verbose_name': 'Озу', 'verbose_name_plural': 'Озу'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='ram',
            name='count',
            field=models.IntegerField(verbose_name='Оперативная память'),
        ),
    ]
