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
class ManuCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    permission_required = 'manufacturer.add_manufacturer'
    template_name = 'inventory/manu_form.html'
    success_url = reverse_lazy('inventory:manu_list')
    form_class = ManuForm
    model = Manufacturer


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

    # success_url = reverse_lazy('inventory:manufacturer')

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
        return reverse('inventory:manu_detail', args=[self.object.id])


class ModelUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    template_name = 'inventory/model_form.html'
    model = Model
    form_class = ModelManu
    permission_required = 'model.change_model'

    def get_success_url(self):
        return reverse('inventory:model_detail', args=[self.object.id])


# >>>>>>>>>>>>>>>>>>>>>>>> M A N U F A C T U R E R ----  END >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# >>>>>>>>>>>>>>>>>>>>>>>> A C C E S S O R I E S  ----  START >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class AccessoryCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    permission_required = 'accessory.add_accessory'
    template_name = 'inventory/acc_form.html'
    success_url = reverse_lazy('inventory:acc_list')
    form_class = AccForm
    model = Accessory


class AccessoryListView(ListView):
    model = Accessory
    template_name = 'inventory/acc_list.html'


class AccessoryDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    model = Accessory
    template_name = 'inventory/acc_delete.html'
    success_url = reverse_lazy('inventory:acc_list')

    permission_required = 'accessory.delete_accessory'


class AccessoryDetailView(DetailView):
    model = Accessory
    template_name = 'inventory/acc_detail.html'

    def get(self, request, pk):
        x = Accessory.objects.get(id=pk)
        accmodels = AccModel.objects.filter(accessory=x).order_by('Name')
        model_acc = ModelAcc()
        context = {'accessory': x, 'accmodels': accmodels, 'model_acc': model_acc}
        return render(request, self.template_name, context)


class AccessoryUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    template_name = 'inventory/acc_form.html'
    model = Accessory
    form_class = AccForm
    permission_required = 'accessory.change_accessory'

    def get_success_url(self):
        return reverse('inventory:acc_detail', args=[self.object.id])


class AccModelCreateView(LoginRequiredMixin, UserAccessMixin, View):
    permission_required = 'accmodel.add_accmodel'

    def post(self, request, pk):
        a = get_object_or_404(Accessory, id=pk)

        accmodel = AccModel(
            Name=request.POST['Name'], accessory=a)

        accmodel.save()

        return redirect(reverse('inventory:acc_detail', args=[pk]))


class AccModelDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    permission_required = 'accmodel.delete_accmodel'
    model = AccModel
    template_name = 'inventory/accmodel_delete.html'

    def get_success_url(self):
        accessory = self.object.accessory
        return reverse('inventory:acc_detail', args=[accessory.id])


class AccModelUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    template_name = 'inventory/accmodel_form.html'
    model = AccModel
    form_class = ModelAcc
    permission_required = 'accmodel.change_accmodel'

    def get_success_url(self):
        accessory = self.object.accessory
        return reverse('inventory:acc_detail', args=[accessory.id])


class AccModelDetailView(View):
    template_name = 'inventory/accmodel_detail.html'

    def get(self, request, pk):
        x = AccModel.objects.get(id=pk)
        accdetails = AccDetail.objects.filter(accessory=x.accessory).filter(accmodel=x).order_by('SerialNo')
        context = {'accmodel': x, 'accdetails': accdetails}
        return render(request, self.template_name, context)


class AccDetailCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    permission_required = 'accdetail.add_accdetail'
    template_name = 'inventory/accdetail_form.html'
    #success_url = reverse_lazy('inventory:accmodel_detail')
    form_class = AccDetailForm
    model = AccDetail
    #fields = '__all__'
    def get_success_url(self):
        accmodel=self.object.accmodel
        return reverse('inventory:accmodel_detail', args=[accmodel.id])


class AccDetailDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    permission_required = 'accdetail.delete_accdetail'
    model = AccDetail
    template_name = 'inventory/accdetail_delete.html'

    def get_success_url(self):
        accmodel=self.object.accmodel
        return reverse('inventory:accmodel_detail', args=[accmodel.id])

class AccDetailUpdateView(LoginRequiredMixin, UserAccessMixin, View):
    permission_required = 'accdetail.add_accdetail'
    permission_required = 'accdetail.change_accdetail'

    template_name = 'inventory/accdetail_form.html'

    def get(self, request, pk):
        accmodel = AccModel.objects.get(id=pk)
        form = AccDetailForm(initial={'accessory': accmodel.accessory.id, 'accmodel': accmodel.id})
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

# >>>>>>>>>>>>>>>>>>>>>>>> A C C E S S O R I E S  ----  END >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# >>>>>>>>>>>>>>>>>>>>>>>> D E V I C E  ----  START >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class DeviceCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    permission_required = 'device.add_device'
    template_name = 'inventory/device_form.html'
    success_url = reverse_lazy('inventory:device_list')
    form_class = DeviceForm
    model = Device