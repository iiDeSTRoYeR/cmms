from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import PPM
from django.urls import reverse_lazy
from datetime import datetime, timedelta



# Create your views here.
def index(request):
    return HttpResponse('Hello World')


class PPMCreate(CreateView,PPM):
    model = PPM
    fields = ['DeviceAsset']
    success_url = reverse_lazy ('tasks:index')


    def form_valid(self, form):
        object = form.save(commit=False)
        ppmval = self.ppmCycleVal(object.DeviceAsset_id)
        object.FuturePPM = datetime.now() + timedelta(days=ppmval)
        object.save()
        return super(PPMCreate, self).form_valid(form)

