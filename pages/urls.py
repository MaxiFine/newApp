from django.urls import path
from .views import AboutPage, HomePageView


urlpatterns = [
    # about page
    path('about/', AboutPage.as_view(), name='about'),

    # home page
    path('', HomePageView.as_view(), name='home'),
    
]