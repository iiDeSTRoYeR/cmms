from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
    path('manufacturer/', views.ManuListView.as_view(), name='manu_list'),
    path('manufacturer/create', views.ManuCreateView.as_view(), name='manu_create'),
]