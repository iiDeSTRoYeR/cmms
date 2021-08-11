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
from employees.models import Member
from home.owner import UserAccessMixin

# Create your views here.

def ConsumableMainView(request):
    return render(request, 'consumable/main.html', {})


class ConsumableCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    permission_required = 'consumable.add_consumable'
    template_name = 'consumable/Consumable_form.html'
    success_url = reverse_lazy('consumable:Consumable_list')
    form_class = ConsumableForm
    model = Consumable


class ConsumableListView(ListView):
    model = Consumable
    template_name = 'consumable/Consumable_list.html'


class ConsumableDetailView(DetailView):
    model = Consumable
    template_name = 'consumable/Consumable_detail.html'

    def get(self, request, pk):
        x = Consumable.objects.get(id=pk)
        Consumable_models =Consumable.objects.filter(Consumable=x).order_by('Cost Class')
        model_Consumable = Consumable()
        context = {'consumable': x, 'Consumable_models': Consumable_models, 'model_Consumable': model_Consumable}
        return render(request, self.template_name, context)

    class ConsumableListView(ListView):
        model = Consumable
        template_name = 'consumable/Consumable_list.html'

class ConsumableDetailView(DetailView):
    model = Consumable
    template_name = 'consumable/Consumable_detail.html'

    def get(self, request, pk):
        x = Consumable.objects.get(id=pk)
        Consumablemodels = Consumable.objects.filter(Consumable=x).order_by('Cost Class')
        model_Consumable = Consumable()
        context = {'Consumable': x, 'Consumablemodels': Consumablemodels, 'model_Consumable': model_Consumable}
        return render(request, self.template_name, context)

class ConsumableDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    model = Consumable
    template_name = 'consumable/Consumable_delete.html'
    success_url = reverse_lazy('consumable:Consumable_list')



class ConsumableUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    template_name = 'consumable/Consumable_form.html'
    model = Consumable
    form_class = ConsumableForm
    permission_required = 'Consumable.change_Consumable'


    def get_success_url(self):
        return reverse('consumable:Consumable_detail', args=[self.object.id])


class ModelCreateView(LoginRequiredMixin, UserAccessMixin, View):
    permission_required = 'model.add_model'

    def post(self, request, pk):
        m = get_object_or_404(Consumable, id=pk)
        model = Consumable(
            Name=request.POST['price'], Member_id=request.POST['Member'],
            DateofBill=request.POST['Date of Bill'], Billpdf=request.POST['Bill PDF'],
            CostClass_id=request.POST['Cost Class'], CostType_id=request.POST['Cost Type'],
            consumable=C)

        model.save()

        return redirect(reverse('consumable:Consumable_detail', args=[pk]))


class ModelDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    permission_required = 'model.delete_model'
    model = Consumable
    template_name = 'consumable/modelCon_delete.html'

    # success_url = reverse_lazy('inventory:manufacturer')

    def get_success_url(self):
        consumable = self.object.consumable
        return reverse('consumable:Consumable_detail', args=[Consumable.id])


class ModelDetailView(DetailView):
    model = Consumable
    template_name = 'consumable/modelCon_detail.html'

class ModelUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    template_name = 'consumable/modelCon_form.html'
    model = Consumable
    form_class = Consumable
    permission_required = 'model.change_model'

    def get_success_url(self):
        return reverse('consumable:model_detail', args=[self.object.id])
