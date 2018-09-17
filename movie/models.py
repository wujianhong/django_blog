from django.db import models


# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=1000)
    schedule = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Movie"
