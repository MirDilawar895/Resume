from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("portfolio", views.portfolio, name="portfolio"),
    path('service', views.service, name='service'),
    path('resume', views.resume, name='resume'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('project', views.project, name='project'),
    path('content', views.content, name='content'),
    path('alting', views.alting, name='alting'),
    
    

]
