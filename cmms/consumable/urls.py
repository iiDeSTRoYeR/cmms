from django.urls import path

from . import views

app_name = 'consumable'
urlpatterns = [
    path('main/', views.ConsumableMainView, name='main'),
    path('consumable/', views.ConsumableListView.as_view(), name='Consumable_list'),
    path('consumable/create', views.ConsumableCreateView.as_view(), name='Consumable_create'),
    path('consumable/<int:pk>/update', views.ConsumableUpdateView.as_view(), name='Consumable_update'),
    path('consumable/<int:pk>', views.ConsumableDetailView.as_view(), name='Consumable_detail'),
    path('consumable/<int:pk>/delete', views.ConsumableDeleteView.as_view(), name='Consumable_delete'),
    path('consumable/<int:pk>/model', views.ConsumableCreateView.as_view(), name='Consumable_model_create'),
    path('model/<int:pk>/delete', views.ModelDeleteView.as_view(), name='Consumable_model_delete'),
    path('model/<int:pk>/update', views.ModelUpdateView.as_view(), name='Consumable_model_update'),
    path('model/<int:pk>', views.ModelDetailView.as_view(), name='Consumable_model_detail'),
]