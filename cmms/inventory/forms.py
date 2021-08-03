from django import forms
from .models import *
from supplier.models import Manufacturer, AgentCompany
from django.utils.html import mark_safe
from modeltranslation.forms import TranslationModelForm
from django.utils.translation import gettext_lazy as _

class ManuForm(TranslationModelForm):
    Name = forms.CharField(
        required=True, label=_('Manufacturer Name'),
        widget=forms.TextInput(attrs={'placeholder': _('Samsung, Toshiba, etc...')})
    )

    agentcompanies = forms.ModelChoiceField(queryset=AgentCompany.objects.all(),
        required=False,
        label=_('Agent Companies'),
        empty_label=_('(Select an agent company if available)'),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style:italic; color:#6c757d;'})
    )

    class Meta:
        model = Manufacturer
        fields = '__all__'

class ModelManu(forms.Form):
    model = forms.CharField(
        label=_('Model Name'),
        required=True, max_length=50, min_length=3, strip=True,
        widget=forms.TextInput(attrs={'placeholder': 'MD-500, SA-775544, etc...'})
    )
    voltage = forms.DecimalField(
        label=_('Voltage (V)'),
        max_digits=8, decimal_places=2,
        required=True, widget=forms.NumberInput(attrs={'placeholder': '220'})
    )
    amperage = forms.DecimalField(
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


