from django.urls import path
from . import views

app_name = 'consumable'
urlpatterns = [
    path('', views.index, name='index'),
]