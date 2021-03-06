# Generated by Django 2.2.10 on 2020-06-19 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PathToCSV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FilePathField(match='“*\\.csv$', max_length=255, path='/home/taisa/PycharmProjects/dj-10-8/application', recursive=True, verbose_name='Путь к CSV-файлу')),
            ],
            options={
                'verbose_name': 'Путь к CSV-файлу',
                'verbose_name_plural': 'Путь к CSV-файлу',
            },
        ),
        migrations.CreateModel(
            name='TableColumns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('width', models.IntegerField(verbose_name='Ширина')),
                ('number', models.IntegerField(verbose_name='Порядковый номер')),
            ],
            options={
                'verbose_name': 'Поле таблицы',
                'verbose_name_plural': 'Поля таблицы',
            },
        ),
    ]
