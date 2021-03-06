# Generated by Django 4.0.3 on 2022-04-26 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100, verbose_name='Тема')),
                ('message', models.TextField(max_length=3000, verbose_name='Сообщение')),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
