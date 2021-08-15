from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DeleteView, CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError
from django.forms.models import model_to_dict
from django.template.loader import render_to_string
from django.views.generic.base import TemplateView

from .models import *
from .forms import *
from supplier.models import Manufacturer
from home.owner import UserAccessMixin


def InventoryMainView(request):
    return render(request, 'inventory/main.html', {})


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
    # success_url = reverse_lazy('inventory:accmodel_detail')
    form_class = AccDetailForm
    model = AccDetail

    # fields = '__all__'
    def get_success_url(self):
        accmodel = self.object.accmodel
        return reverse('inventory:accmodel_detail', args=[accmodel.id])


class AccDetailDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    permission_required = 'accdetail.delete_accdetail'
    model = AccDetail
    template_name = 'inventory/accdetail_delete.html'

    def get_success_url(self):
        accmodel = self.object.accmodel
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

    def post(self, request, pk):
        am = get_object_or_404(AccModel, id=pk)
        accdetail = AccDetail(
            SerialNo=request.POST['SerialNo'], accessory=am.accessory, accmodel=am)
        accdetail.save()
        return redirect(reverse('inventory:accmodel_detail', args=[pk]))


# >>>>>>>>>>>>>>>>>>>>>>>> A C C E S S O R I E S  ----  END >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# >>>>>>>>>>>>>>>>>>>>>>>> P L A C E S  ----  START >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def PlacesMainView(request):
    return render(request, 'inventory/places_main.html', {})

@method_decorator(csrf_exempt, name='dispatch')
class load_departments(View):
    template_name = 'inventory/dept_list.html'

    def the_get(self, request, college_id, deptform):
        dept = Department.objects.filter(college=college_id).order_by('deptName')
        ctx = {'dept': dept, 'deptform': deptform}
        return render(request, self.template_name, ctx)

    def get(self, request):
        college_id = request.GET.get('college_id')
        deptform = DepartmentForm()
        return self.the_get(request, college_id, deptform)

    def post(self, request):
        college_id = request.POST.get('college_id')
        deptform = DepartmentForm(request.POST)
        print(request.POST)
        if deptform.is_valid():
            department1 = Department()
            department1.deptName = deptform.cleaned_data['deptName']
            department1.college_id = college_id
            department1.save()

            deptform = DepartmentForm()  # clears the form

        return self.the_get(request, college_id, deptform)


@method_decorator(csrf_exempt, name='dispatch')
class CollegeListCreateView(View):
    template_name = 'inventory/college_list.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        data = dict()
        print(request.POST)
        if request.POST == {}:
            collegeform = CollegeForm()
        else:
            collegeform = CollegeForm(request.POST)
            if collegeform.is_valid():
                college = College()
                college.Name = collegeform.cleaned_data['Name']
                college.save()

                data['form_is_valid'] = True
            else:
                data['form_is_valid'] = False

        ctx = {'form': collegeform}

        data['html_form'] = render_to_string(
            'inventory/college_create.html',
            ctx,
            request=request)

        data['last_id'] = College.objects.last().id
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class DepartmentUpdateView(LoginRequiredMixin, UserAccessMixin, View):
    permission_required = 'department.change_department'
    template_name = 'inventory/dept_update.html'

    def get(self, request, pk):
        dept = get_object_or_404(Department, pk=pk)
        deptUpdateForm = DepartmentUpdateForm(instance=dept)
        ctx = {'deptUpdateForm': deptUpdateForm}
        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        data = dict()
        dept = get_object_or_404(Department, pk=pk)
        deptUpdateForm = DepartmentUpdateForm(request.POST, instance=dept)
        print(request.POST)
        if deptUpdateForm.is_valid():
            deptUpdateForm.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False

        ctx = {'deptUpdateForm': deptUpdateForm}

        data['html_updateform'] = render_to_string(
            self.template_name,
            ctx,
            request=request
        )

        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class DepartmentDeleteView(LoginRequiredMixin, UserAccessMixin, View):
    permission_required = 'department.delete_department'
    template_name = 'inventory/dept_del.html'

    def get(self, request, pk):
        dept = get_object_or_404(Department, pk=pk)
        print(dept)
        ctx = {'dept': dept}
        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        dept = get_object_or_404(Department, pk=pk)
        dept.delete()
        return HttpResponse('')

class CollegeDropdownView(View):
    template_name = "inventory/college_list_dropdown.html"

    def get(self, request):
        college_list = College.objects.order_by('Name')
        ctx = {'college_list': college_list}
        return render(request, self.template_name, ctx)


# >>>>>>>>>>>>>>>>>>>>>>>> P L A C E S  ----  END >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# >>>>>>>>>>>>>>>>>>>>>>>> D E V I C E  ----  START >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class DeviceCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    permission_required = 'device.add_device'
    template_name = 'inventory/device_form.html'
    success_url = reverse_lazy('inventory:device_list')
    form_class = DeviceForm
    model = Device
