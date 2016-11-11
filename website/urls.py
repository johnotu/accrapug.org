from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='homepage'),
    url(r'^about$', views.AboutPageView.as_view(), name='aboutpage'),
    url(r'^projects$', views.ProjectsPageView.as_view(), name='projectspage')

]
