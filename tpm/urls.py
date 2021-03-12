from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('computer/', views.computer, name='computer'),
    path('electrical/', views.electrical, name='electrical'),
    path('mechanical/', views.mechanical, name='mechanical'),
    path('biomedical/', views.biomedical, name='biomedical'),
]
