from django.urls import path

from . import views

app_name = 'supplier'
urlpatterns = [
    path('', views.index, name='supplier'),
    path('CreateSupplierPage', views.CreateSupplierPage, name='CreateSupplierPage'),
    path('CreateManufacturerPage', views.CreateManufacturerPage, name='CreateManufacturerPage'),
    path('CreateWarrantyPage', views.CreateWarrantyPage, name='CreateWarrantyPage'),
    path('CreateAgentCompanyPage', views.CreateAgentCompanyPage, name='CreateAgentCompanyPage'),
]