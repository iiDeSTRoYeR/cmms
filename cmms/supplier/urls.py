from django.urls import path

from . import views

app_name = 'supplier'
urlpatterns = [
    path('', views.index, name='index'),
    path('CreateSupplierPage', views.CreateSupplierPage, name='CreateSupplierPage'),
]