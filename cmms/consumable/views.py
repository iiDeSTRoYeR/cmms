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

class CostClassCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    permission_required = 'costclass.add_costclass'
    template_name = 'consumable/CostClass_form.html'
    success_url = reverse_lazy('consumable:CostClass_list')
    form_class = CostClass
    model = CostClass


class CostClassListView(ListView):
    model = CostClass
    template_name = 'consumable/CostClass_list.html'


class CostClassDetailView(DetailView):
    model = CostClass
    template_name = 'consumable/CostClass_detail.html'

    def get(self, request, pk):
        x = CostClass.objects.get(id=pk)
        models = Consumable.objects.filter(CostClass=x).order_by('Title')
        model_CostClass = Consumable()
        context = {'CostClass': x, 'models': models, 'model_CostClass': model_CostClass}
        return render(request, self.template_name, context)


class ConsumableCreateView(LoginRequiredMixin, UserAccessMixin, View):
    permission_required = 'consumable.add_consumable'

    def post(self, request, pk):
        c = get_object_or_404(Consumable, id=pk)
        consumable = Consumable(
            Price =request.POST['Price'], DateofBill=request.POST['Date of Bill'],
            Billpdf=request.POST['Bill PDF'], Member_id=request.POST['Member'],
            CostType_id=request.POST['Cost Type'], consumable=c)

        consumable.save()

        return redirect(reverse('consumable:Consumable_detail', args=[pk]))


class ConsumableDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    permission_required = 'consumable.delete_consumable'
    model = Consumable
    template_name = 'consumable/modelCon_delete.html'

    # success_url = reverse_lazy('consumable:CostClass')

    def get_success_url(self):
        CostClass = self.object.CostClass
        return reverse('consumable:CostClass_detail', args=[CostClass.id])


class ConsumableDetailView(DetailView):
    model = Consumable
    template_name = 'consumable/modelCon_detail.html'


class CostClassDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    model = CostClass
    template_name = 'consumable/CostClass_delete.html'
    success_url = reverse_lazy('consumable:CostClass_list')

    permission_required = 'costclass.delete_costclass'


class CostClassUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    template_name = 'consumable/CostClass_form.html'
    model = CostClass
    form_class = CostClassForm
    permission_required = 'costclass.change_costclass'

    def get_success_url(self):
        return reverse('consumable:CostClass_detail', args=[self.object.id])


class ConsumableUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    template_name = 'consumable/modelCon_form.html'
    model = Consumable
    form_class = ConsumableForm
    permission_required = 'consumable.change_consumable'

    def get_success_url(self):
        return reverse('consumable:consumable_detail', args=[self.object.id])

