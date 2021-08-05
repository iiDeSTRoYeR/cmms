from django.urls import path
from . import views

app_name = 'supplier'
urlpatterns = [
    path('CreateSupplierPage', views.CreateSupplierPage, name='CreateSupplierPage'),
]