from django.shortcuts import render
from django.views import View
from django.conf import settings

# Create your views here.

def index(request):
    return HttpResponse('Hello World')

