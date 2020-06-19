from django.http import HttpResponseRedirect
from django.urls import path

from .views import show_stations

urlpatterns = [
    path('stations/', show_stations),
    path('', lambda x: HttpResponseRedirect('/stations/')),
]