from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *

def index(request):
    return HttpResponse('<h1>here suppliers </h1>')

def CreateSupplierPage(request):
    return HttpResponse('<h1>CreateSupplierPage-supplier </h1>')