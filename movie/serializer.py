from rest_framework import serializers
from . import models


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Movie
        fields = ('id', 'name', 'schedule')
