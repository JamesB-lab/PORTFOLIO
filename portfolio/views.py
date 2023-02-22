from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from .models import Post


class LandingPageView(TemplateView):
    template_name = 'landing.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class CVPageView(TemplateView):
    template_name = 'cv.html'


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
