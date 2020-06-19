# Create your views here.

import csv, os

from django.shortcuts import render
from django.conf import settings
from .models import TableColumns, PathToCSV

# CSV_FILENAME = 'phones.csv'
# COLUMNS = [
#     {'name': 'id', 'width': 1},
#     {'name': 'name', 'width': 3},
#     {'name': 'price', 'width': 2},
#     {'name': 'release_date', 'width': 2},
#     {'name': 'lte_exists', 'width': 1},
# ]


def table_view(request):
    path = PathToCSV.objects.get(pk=1).get_path()
    path = path.split('/')[-1]
    # print(os.path.join(settings.BASE_DIR, path))
    table_columns = TableColumns.objects.order_by('number')
    # print(table_columns)

    header = {}
    for col in table_columns:
        header[col.number] = col.name
    # print(header)

    template = 'table.html'
    with open(os.path.join(settings.BASE_DIR, path), 'rt') as csv_file:
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        next(table_reader, None)

        for table_row in table_reader:
            row = {header.get(idx) or 'col{:03d}'.format(idx): value
                   for idx, value in enumerate(table_row)}
            table.append(row)

        context = {
            'columns': table_columns,
            # 'columns': COLUMNS,
            'table': table,
            'csv_file': path
        }
        result = render(request, template, context)
    return result

