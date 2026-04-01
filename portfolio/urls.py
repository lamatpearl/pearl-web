from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'), # Note the Capital 'S' to match your base.html
    path('education/', views.education, name='education'),
    path('contact/', views.contact, name='contact'),
]