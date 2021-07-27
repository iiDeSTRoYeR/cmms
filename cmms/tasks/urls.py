from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.PPMCreate.as_view(), name ='ppm_create'),
]