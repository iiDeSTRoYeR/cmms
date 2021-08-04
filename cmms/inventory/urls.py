from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
    path('manufacturer/', views.ManuListView.as_view(), name='manu_list'),
    path('manufacturer/create', views.ManuCreateView.as_view(), name='manu_create'),
    path('manufacturer/<int:pk>/update', views.ManuUpdateView.as_view(), name='manu_update'),
    path('manufacturer/<int:pk>', views.ManuDetailView.as_view(), name='manu_detail'),
    path('manufacturer/<int:pk>/delete', views.ManuDeleteView.as_view(), name='manu_delete'),
    path('manufacturer/<int:pk>/model', views.ModelCreateView.as_view(), name='manu_model_create'),
    path('model/<int:pk>/delete', views.ModelDeleteView.as_view(), name='manu_model_delete'),
    path('model/<int:pk>/update', views.ModelUpdateView.as_view(), name='manu_model_update'),
    path('model/<int:pk>', views.ModelDetailView.as_view(), name='model_detail'),
]