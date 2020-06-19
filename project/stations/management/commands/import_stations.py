import csv, os

from django.core.management.base import BaseCommand
from stations.models import Station, Route
from django.conf import settings


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, 'moscow_bus_stations.csv'), 'r', encoding='cp1251') as csvfile:
            station_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(station_reader)

            for line in station_reader:
                # TODO: Добавьте сохранение модели

                station = Station()
                station.latitude = float(line[3])
                station.longitude = float(line[2])
                station.name = line[1]
                station.save()

                for route in line[7].split('; '):
                    name_route, _ = Route.objects.get_or_create(name=route)
                    station.routes.add(name_route)

        print('Done')
