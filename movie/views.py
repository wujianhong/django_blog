from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets
from . import models
from . import serializer


# Create your views here.

class MovieView(ListView):
    model = models.Movie
    template_name = 'movie.html'


class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializer.MovieSerializer
