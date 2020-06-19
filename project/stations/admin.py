from django.contrib import admin

# Register your models here.

from .models import Station, Route

class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'latitude', 'longitude')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)

class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)


admin.site.register(Station, StationAdmin)
admin.site.register(Route, RouteAdmin)