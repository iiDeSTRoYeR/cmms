from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *

def index(request):
    return HttpResponse('<h1>here suppliers </h1>')

def CreateSupplierPage(request):
    return HttpResponse('<h1>CreateSupplierPage-supplier </h1>')

def CreateManufacturerPage(request):
    return HttpResponse('<h1>CreateManufacturerPage-supplier </h1>')

def CreateWarrantyPage(request):
    return HttpResponse('<h1>CreateWarrantyPage-supplier </h1>')

def CreateAgentCompanyPage(request):
    return HttpResponse('<h1>CreateAgentCompanyPage-supplier </h1>')



