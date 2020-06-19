from django.db import models

import os

# Create your models here.

class TableColumns(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    width = models.IntegerField(verbose_name='Ширина')
    number = models.IntegerField(verbose_name='Порядковый номер')

    class Meta:
        verbose_name = 'Поле таблицы'
        verbose_name_plural = 'Поля таблицы'

    def __str__(self):
        return self.name


class PathToCSV(models.Model):
    start_path = os.path.dirname(os.path.dirname(__file__))
    path = models.FilePathField(path=start_path, match='“*\.csv$', recursive=True, max_length=255, verbose_name='Путь к CSV-файлу')

    class Meta:
        verbose_name = 'Путь к CSV-файлу'
        verbose_name_plural = 'Путь к CSV-файлу'

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.pk = 1
        self.path = path
        self.save()

    def __str__(self):
        return str(self.path)
