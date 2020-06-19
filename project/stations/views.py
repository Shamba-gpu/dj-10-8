from django.shortcuts import render, get_object_or_404
from django.db.models import Avg

from .models import Route, Station
# Create your views here.

def show_stations(request):
    context = {}
    name_route = request.GET.get('route')
    # print(name_route)

    all_routes = Route.objects.all()
    context['routes'] = all_routes

    if name_route:
        selected_route = get_object_or_404(Route, name=name_route)
        stations = selected_route.stations.all()
        context['stations'] = stations
        context['center'] = {
            'x': stations.aggregate(Avg('longitude'))['longitude__avg'],
            'y': stations.aggregate(Avg('latitude'))['latitude__avg']}

    return render(request, 'stations.html', context)