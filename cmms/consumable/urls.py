from django.urls import path

from . import views

app_name = 'consumable'
urlpatterns = [
    path('main/', views.consumableMainView, name='main'),
    path('CostClass/', views.CostClassListView.as_view(), name='CostClass_list'),
    path('CostClass/create', views.CostClassCreateView.as_view(), name='CostClass_create'),
    path('CostClass/<int:pk>/update', views.CostClassUpdateView.as_view(), name='CostClass_update'),
    path('CostClass/<int:pk>', views.CostClassDetailView.as_view(), name='CostClass_detail'),
    path('CostClass/<int:pk>/delete', views.CostClassDeleteView.as_view(), name='CostClass_delete'),
    path('CostClass/<int:pk>/Consumable', views.ConsumableCreateView.as_view(), name='CostClass_Consumable_create'),
    path('Consumable/<int:pk>/delete', views.ConsumableDeleteView.as_view(), name='CostClass_Consumable_delete'),
    path('Consumable/<int:pk>/update', views.ConsumableUpdateView.as_view(), name='CostClass_Consumable_update'),
    path('Consumable/<int:pk>', views.ConsumableDetailView.as_view(), name='Consumable_detail'),
]