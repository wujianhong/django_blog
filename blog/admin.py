from django.contrib import admin
from .models import Blog


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_time')
    search_fields = ('title', 'category', 'content', 'date_time')
    list_filter = ('date_time', )
    ordering = ('-date_time', )


admin.site.register(Blog, BlogAdmin)
