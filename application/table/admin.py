from django.contrib import admin

# Register your models here.

from .models import TableColumns, PathToCSV

class ColumnsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'width', 'number')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    ordering = ('number',)

admin.site.register(TableColumns, ColumnsAdmin)
admin.site.register(PathToCSV)