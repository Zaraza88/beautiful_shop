# Generated by Django 4.0.3 on 2022-04-18 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_reviews_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'ordering': ['-date'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
