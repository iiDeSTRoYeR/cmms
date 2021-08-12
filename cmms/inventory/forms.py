from django import forms
from .models import *
from supplier.models import Manufacturer, AgentCompany
from django.utils.html import mark_safe
from modeltranslation.forms import TranslationModelForm
from django.utils.translation import gettext_lazy as _

class ManuForm(forms.ModelForm):
    Name = forms.CharField(
        required=True, label=_('Manufacturer Name'),
        widget=forms.TextInput(attrs={'placeholder': _('Samsung, Toshiba, etc...')})
    )

    agentcompanies = forms.ModelMultipleChoiceField(queryset=AgentCompany.objects.all(),
        required=False,
        label=_('Agent Companies'),
        #widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style:italic; color:#6c757d;'})
        widget=forms.CheckboxSelectMultiple()  #https://stackoverflow.com/questions/24031461/drop-down-with-checkboxes-in-django-form       to create dropdown checkboxes
    )
    class Meta:
        model = Manufacturer
        fields = ['Name', 'agentcompanies']

class ModelManu(forms.ModelForm):
    Name = forms.CharField(
        label=_('Model Name'),
        required=True, max_length=50, min_length=3, strip=True,
        widget=forms.TextInput(attrs={'placeholder': 'MD-500, SA-775544, etc...'})
    )
    Voltage = forms.DecimalField(
        label=_('Voltage (V)'),
        max_digits=8, decimal_places=2,
        required=True, widget=forms.NumberInput(attrs={'placeholder': '220'})
    )
    Amperage = forms.DecimalField(
        label=_('Amperage (A)'),
        max_digits=8, decimal_places=2,
        required=True, widget=forms.NumberInput(attrs={'placeholder': '5'})
    )
    phase = forms.ModelChoiceField(
        label=_('Phase'),
        queryset=Phase.objects.all(),
        required=True,
        empty_label= _('(Single Phase, Three Phase, etc...)'),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style:italic;'})
    )
    frequency = forms.ModelChoiceField(
        label=_('Frequency (Hz)'),
        queryset=Frequency.objects.all(),
        required=True,
        empty_label=_('(50, 60, 50/60, etc...)'),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style:italic;'})
    )
    device = forms.ModelChoiceField(
        label=_('General Device Name'),
        queryset=Device.objects.all(),
        required=True,
        empty_label=_('(Refrigerator, Computer, CBC, X-Ray, etc...)'),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style:italic;'})
    )

    class Meta:
        model = Model
        fields = ['Name', 'Voltage', 'Amperage', 'phase', 'frequency', 'device']

# >>>>>>>>>>>>>>>>>>>>>>>> M A N U F A C T U R E R ----  END >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# >>>>>>>>>>>>>>>>>>>>>>>> A C C E S S O R I E S  ----  START >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class AccForm(forms.ModelForm):
    Name = forms.CharField(
        required=True, label=_('Accessory General Name'),
        widget=forms.TextInput(attrs={'placeholder': _('Mouse, Screen, Probe, etc...')})
    )
    Description = forms.CharField(
        required=True, label=_('Accessory Description'),
        widget=forms.Textarea(attrs={'placeholder': _('Function and description of accessory')})
    )

    class Meta:
        model = Accessory
        fields = ['Name', 'Description']

class ModelAcc(forms.ModelForm):
    Name = forms.CharField(
        label=_("Accessory's Model Name"),
        required=True, max_length=50, min_length=3, strip=True,
        widget=forms.TextInput(attrs={'placeholder': 'LG-500, SA-775544, etc...'})
    )

    class Meta:
        model = AccModel
        fields = ['Name']

class AccDetailForm(forms.ModelForm):
    SerialNo = forms.CharField(
        label=_("Accessory's Serial Number"),
        required=True, max_length=100, min_length=3, strip=True,
        widget=forms.TextInput(attrs={'placeholder': 'LG-500, SA-775544, etc...'})
    )

    accessory = forms.ModelChoiceField(
        queryset=Accessory.objects.all(),
        label=_("Accessory's General Name"),
        required=True,
        empty_label=_('(Select a general accessory to which the serial number belongs to)'),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style:italic;'})
    )


    class Meta:
        model = AccDetail
        fields = '__all__'

'''
    def __init__(self,*args, **kwargs):
        super(AccDetailForm,self).__init__(*args, **kwargs)
        self.fields['accmodel'].empty_label = 'TEST'
'''
# >>>>>>>>>>>>>>>>>>>>>>>> A C C E S S O R I E S  ----  END >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# >>>>>>>>>>>>>>>>>>>>>>>> C O L L E G E S  ----  START >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class CollegeForm(forms.ModelForm):
    Name = forms.CharField(
        required=True, label=_('College Name'),
        widget=forms.TextInput(attrs={'placeholder': _('College of Engineering, College of Computers & Information, etc...')})
    )

    class Meta:
        model = College
        fields = '__all__'


class DepartmentForm(forms.Form):
    deptName = forms.CharField(
        required=True, label=_('Department Name'),
        widget=forms.TextInput(attrs={'placeholder': _('Electrical Engineering, Biology, etc...')})
    )
    # class Meta:
    #     model = Department
    #     fields = ['Name']



# >>>>>>>>>>>>>>>>>>>>>>>> D E V I C E S  ----  START >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class DeviceForm(forms.ModelForm):
    Name = forms.CharField(
        required=True, label=_('General Device Name'),
        widget=forms.TextInput(attrs={'placeholder': _('Refrigerator, Computer, etc...')})
    )

    PPM_Cycle = forms.IntegerField(
        required=True, label=_('PPM Cycle'),
    )
    Brief_Function_Description = forms.CharField(
        required=True, label=_("Device's brief function description"),
        widget=forms.Textarea(attrs={'placeholder': _('"e.g. Used for storing samples at low temperatures..."')})
    )
    accessories = forms.ModelMultipleChoiceField(queryset=Accessory.objects.all(),
        required=False,
        label=_('Accessories'),
        #widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style:italic; color:#6c757d;'})
        widget=forms.CheckboxSelectMultiple()  #https://stackoverflow.com/questions/24031461/drop-down-with-checkboxes-in-django-form       to create dropdown checkboxes
    )
    class Meta:
        model = Device
        fields = ['Name', 'PPM_Cycle', 'Brief_Function_Description', 'accessories']
