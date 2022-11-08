from django.views.generic import ListView, DetailView, TemplateView
from .models import Post

from django.shortcuts import render

class LandingPageView(TemplateView):
    template_name = 'landing.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class CVPageView(TemplateView):
    template_name = 'cv.html'


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
