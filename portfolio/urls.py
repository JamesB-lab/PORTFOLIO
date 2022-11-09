from django.urls import path
from .views import BlogListView, BlogDetailView, LandingPageView, AboutPageView, CVPageView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('portfolio/', BlogListView.as_view(), name='portfolio'),
    path('', LandingPageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('cv/', CVPageView.as_view(), name='cv'),
]
