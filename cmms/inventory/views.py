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




