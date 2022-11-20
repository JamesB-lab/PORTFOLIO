from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView, TemplateView

from .email import EmailForm
from .models import Post


class LandingPageView(TemplateView):
    template_name = 'landing.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class CVPageView(FormView):
    template_name = 'cv.html'
    form_class = EmailForm
    success_url = reverse_lazy('cv')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
