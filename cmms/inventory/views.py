from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView, CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy, reverse

from .models import *
from .forms import *
from supplier.models import Manufacturer

class ManuCreateView(LoginRequiredMixin, View):
    template_name = 'inventory/manu_form.html'
    success_url = reverse_lazy('inventory:manu_list')

    def get(self, request):
        form = ManuForm()
        ctx = {'form' : form}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = ManuForm(request.POST)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
        form.save()
        return redirect(self.success_url)


class ManuListView(ListView):
    model = Manufacturer
    template_name = 'inventory/manu_list.html'


class ManuDetailView(DetailView):
    model = Manufacturer
    template_name = 'inventory/manu_detail.html'

    def get(self, request, pk):
        x = Manufacturer.objects.get(id=pk)
        models = Model.objects.filter(manufacturer=x).order_by('Name')
        model_manu = ModelManu()
        context = { 'manufacturer' : x, 'models': models, 'model_manu': model_manu }
        return render(request, self.template_name, context)

class ModelCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        m = get_object_or_404(Manufacturer, id=pk)

        model = Model(
            Name=request.POST['model'], Voltage=request.POST['voltage'],
            Amperage=request.POST['amperage'], phase_id=request.POST['phase'],
            frequency_id=request.POST['frequency'], device_id=request.POST['device'],
            manufacturer=m)

        model.save()

        return redirect(reverse('inventory:manu_detail', args=[pk]))

class ModelDeleteView(LoginRequiredMixin, DeleteView):
    model = Model
    template_name = 'inventory/model_delete.html'
    success_url = reverse_lazy('inventory:manufacturer')

    def get_success_url(self):
        manufacturer = self.object.manufacturer
        return reverse('inventory:manu_detail', args=[manufacturer.id])


class ModelDetailView(DetailView):
    model = Model
    template_name = 'inventory/model_detail.html'
