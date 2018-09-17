from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView
)
from .models import Blog
from . import serializer
from rest_framework import viewsets


# Create your views here.
#
# def index(request):
#     return render(request, 'index.html')


class DirectoryView(ListView):
    model = Blog
    # context_object_name = "blog"
    template_name = 'index.html'
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ContentView(DetailView):
    model = Blog
    context_object_name = "blog_content"
    template_name = "detail.html"

    # slug_field = 'slug'

    def get_queryset(self):
        qs = super(ContentView, self).get_queryset()
        return qs.filter(pk=self.kwargs['pk'])


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = serializer.BlogSerializer
