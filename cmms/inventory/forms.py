from django import forms
from .models import *
from supplier.models import Manufacturer, AgentCompany
from django.utils.html import mark_safe

class ManuForm(forms.ModelForm):

    Name = forms.CharField(
        required=True, label='Manufacturer Name',
        widget=forms.TextInput(attrs={'placeholder': 'Samsung, Toshiba, etc...'})
    )

    agentcompanies = forms.ModelChoiceField(queryset=AgentCompany.objects.all(),
        required=False,
        label='Agent Companies',
        empty_label='(Select an agent company if available)',
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style:italic; color:#6c757d;'})
    )

    class Meta:
        model = Manufacturer
        fields = '__all__'

class ModelManu(forms.Form):
    model = forms.CharField(
        label='Model Name',
        required=True, max_length=50, min_length=3, strip=True,
        widget=forms.TextInput(attrs={'placeholder': 'MD-500, SA-775544, etc...'})
    )
    voltage = forms.DecimalField(
        label='Voltage (V)',
        max_digits=8, decimal_places=2,
        required=True, widget=forms.NumberInput(attrs={'placeholder': '220'})
    )
    amperage = forms.DecimalField(
        label='Amperage (A)',
        max_digits=8, decimal_places=2,
        required=True, widget=forms.NumberInput(attrs={'placeholder': '5'})
    )
    phase = forms.ModelChoiceField(
        label=mark_safe('<span style=" font-style: italic;">Phase</span>'),
        queryset=Phase.objects.all(),
        required=True,
        empty_label=mark_safe('<span style="font-style: italic; color:#6c757d;"> (Single Phase, Three Phase, etc...) </span>'),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style:italic; color:#6c757d;', 'list': 'datalistOptions'})
    )
    frequency = forms.ModelChoiceField(
        label='Frequency (Hz)',
        queryset=Frequency.objects.all(),
        required=True,
        empty_label='(50, 60, 50/60, etc...)',
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style:italic; color:#6c757d;'})
    )
    device = forms.ModelChoiceField(
        label='General Device Name',
        queryset=Device.objects.all(),
        required=True,
        empty_label='(Refrigerator, Computer, CBC, X-Ray, etc...)',
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style:italic; color:#6c757d;'})
    )


