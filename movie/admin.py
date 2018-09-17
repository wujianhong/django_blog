from django.contrib import admin
from . import models


# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'schedule')
    search_fields = ('name',)
    list_editable = ('schedule',)


admin.site.register(models.Movie, MovieAdmin)
