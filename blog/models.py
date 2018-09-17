from django.db import models

# Create your models here.
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True, max_length=1000)
    category = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'Blog'


class Context(models.Model):
    class Meta:
        verbose_name_plural = 'Context'
    context = models.CharField(max_length=1000)
    blog = models.ForeignKey(to='Blog', on_delete=models.CASCADE, related_name="blog_context")
    # def get_absolute_url(self):
    #     return reverse('blog:detail', kwargs={'slug', self.id})
