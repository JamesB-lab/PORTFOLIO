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
        skills_param = self.request.GET.get('skills')
        skills = []
        if skills_param is not None:
            skills = skills_param.split(',')
        skills_filter = {}
        model_props = self.model.__dict__.keys()
        for skill in skills:
            skill_prop = f'skill_{skill}'
            if skill_prop in model_props:
                skills_filter[skill_prop] = True
        return super().get_queryset().filter(active=True,**skills_filter).order_by('-created_at')


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
