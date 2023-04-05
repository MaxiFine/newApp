from django.views.generic import TemplateView


class AboutPage(TemplateView):
    template_name = 'about.html'
    

class HomePageView(TemplateView):
    template_name = 'home.html'


