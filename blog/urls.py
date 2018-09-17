
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.DirectoryView.as_view(), name='index'),
    path("<int:pk>/", views.ContentView.as_view(), name='detail'),
]
