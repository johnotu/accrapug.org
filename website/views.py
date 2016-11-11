from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    """docstring for HomePageView"""
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ProjectsPageView(TemplateView):
    template_name = 'projects.html'