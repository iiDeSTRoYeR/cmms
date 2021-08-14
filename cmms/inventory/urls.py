from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'inventory'
urlpatterns = [
    path('main/', views.InventoryMainView, name='main'),
    path('manufacturer/', views.ManuListView.as_view(), name='manu_list'),
    path('manufacturer/create', views.ManuCreateView.as_view(), name='manu_create'),
    path('manufacturer/<int:pk>/update', views.ManuUpdateView.as_view(), name='manu_update'),
    path('manufacturer/<int:pk>', views.ManuDetailView.as_view(), name='manu_detail'),
    path('manufacturer/<int:pk>/delete', views.ManuDeleteView.as_view(), name='manu_delete'),
    path('manufacturer/<int:pk>/model', views.ModelCreateView.as_view(), name='manu_model_create'),
    path('model/<int:pk>/delete', views.ModelDeleteView.as_view(), name='manu_model_delete'),
    path('model/<int:pk>/update', views.ModelUpdateView.as_view(), name='manu_model_update'),
    path('model/<int:pk>', views.ModelDetailView.as_view(), name='model_detail'),

    path('accessory/', views.AccessoryListView.as_view(), name='acc_list'),
    path('accessory/create', views.AccessoryCreateView.as_view(), name='acc_create'),
    path('accessory/<int:pk>/update', views.AccessoryUpdateView.as_view(), name='acc_update'),
    path('accessory/<int:pk>', views.AccessoryDetailView.as_view(), name='acc_detail'),
    path('accessory/<int:pk>/delete', views.AccessoryDeleteView.as_view(), name='acc_delete'),
    path('accessory/<int:pk>/model', views.AccModelCreateView.as_view(), name='accmodel_create'),
    path('accmodel/<int:pk>/delete', views.AccModelDeleteView.as_view(), name='accmodel_delete'),
    path('accmodel/<int:pk>/update', views.AccModelUpdateView.as_view(), name='accmodel_update'),
    path('accmodel/<int:pk>', views.AccModelDetailView.as_view(), name='accmodel_detail'),

    path('accdetail/create', views.AccDetailCreateView.as_view(), name='accdetail_create'),
    path('accdetail/<int:pk>/delete', views.AccDetailDeleteView.as_view(), name='accdetail_delete'),
    path('accdetail/<int:pk>/update', views.AccDetailUpdateView.as_view(), name='accdetail_update'),

    path('places/', views.PlacesMainView, name='places_main'),
    path('places/college', views.CollegeListCreateView.as_view(), name='college_list'),
    path('ajax/load-dept/', views.load_departments.as_view(), name='ajax_load_dept'),
    path('ajax/<int:pk>/edit-dept', views.DepartmentUpdateView.as_view(), name='ajax_edit_dept'),
    path('ajax/<int:pk>/delete-dept', views.DepartmentDeleteView.as_view(), name='ajax_delete_dept'),
    path('places/college/dropdown', views.CollegeDropdownView.as_view(), name='col_drop'),
]