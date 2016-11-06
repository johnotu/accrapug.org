from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    """docstring for HomePageView"""
    template_name = 'home.html'
