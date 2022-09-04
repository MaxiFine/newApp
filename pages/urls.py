from django.urls import path
from .views import AboutPage, HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPage.as_view(), name='about'),
]