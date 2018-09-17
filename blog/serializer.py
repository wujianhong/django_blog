from rest_framework import serializers
from . import models


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Blog
        fields = ('title', 'category', 'date_time')
