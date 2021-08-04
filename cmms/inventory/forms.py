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
