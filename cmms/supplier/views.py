from django.shortcuts import render
from django.http import HttpResponse

def CreateSupplierPage(request):
    return HttpResponse('<h1>here suppliers <h1/>')
