from django.urls import path

from . import views

app_name = 'usage'
urlpatterns = [
    path('', views.index, name='index'),
]