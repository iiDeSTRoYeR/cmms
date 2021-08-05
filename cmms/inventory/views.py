from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DeleteView, CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login

from .models import *
from .forms import *
from supplier.models import Manufacturer
from home.owner import UserAccessMixin

# >>>>>>>>>>>>>>>>>>>>>>>> M A N U F A C T U R E R ----  START >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class ManuCreateView(LoginRequiredMixin, UserAccessMixin, View):
    permission_required = 'manufacturer.add_manufacturer'
    template_name = 'inventory/manu_form.html'
    success_url = reverse_lazy('inventory:manu_list')

    def get(self, request):
        form = ManuForm()
        ctx = {'form': form}
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
        context = {'manufacturer': x, 'models': models, 'model_manu': model_manu}
        return render(request, self.template_name, context)


class ModelCreateView(LoginRequiredMixin, UserAccessMixin, View):
    permission_required = 'model.add_model'
    def post(self, request, pk):
        m = get_object_or_404(Manufacturer, id=pk)

        model = Model(
            Name=request.POST['Name'], Voltage=request.POST['Voltage'],
            Amperage=request.POST['Amperage'], phase_id=request.POST['phase'],
            frequency_id=request.POST['frequency'], device_id=request.POST['device'],
            manufacturer=m)

        model.save()

        return redirect(reverse('inventory:manu_detail', args=[pk]))


class ModelDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    permission_required = 'model.delete_model'
    model = Model
    template_name = 'inventory/model_delete.html'
    #success_url = reverse_lazy('inventory:manufacturer')

    def get_success_url(self):
        manufacturer = self.object.manufacturer
        return reverse('inventory:manu_detail', args=[manufacturer.id])

class ModelDetailView(DetailView):
    model = Model
    template_name = 'inventory/model_detail.html'

class ManuDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    model = Manufacturer
    template_name = 'inventory/manu_delete.html'
    success_url = reverse_lazy('inventory:manu_list')

    permission_required = 'manufacturer.delete_manufacturer'

class ManuUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    template_name = 'inventory/manu_form.html'
    model = Manufacturer
    form_class = ManuForm
    permission_required = 'manufacturer.change_manufacturer'

    def get_success_url(self):
        manufacturer = self.object
        return reverse('inventory:manu_detail', args=[manufacturer.id])

class ModelUpdateView(LoginRequiredMixin,UserAccessMixin, UpdateView):
    template_name = 'inventory/model_form.html'
    model = Model
    form_class = ModelManu
    permission_required = 'model.change_model'

    def get_success_url(self):
        return reverse('inventory:model_detail', args=[self.object.id])


# >>>>>>>>>>>>>>>>>>>>>>>> M A N U F A C T U R E R ----  END >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# >>>>>>>>>>>>>>>>>>>>>>>> A C C E S S O R I E S  ----  START >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
