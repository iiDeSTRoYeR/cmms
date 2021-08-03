from django import forms
from .models import *
from inventory.models import DeviceAsset
from django.utils.html import mark_safe


class Add_Device_Warranty(forms.ModelForm):
    DeviceAsset = forms.ModelchoiceField(
        lable=mark_safe('<span style="font-style: italic;">DeviceAsset</span>'),
        queryset=DeviceAsset.objects.all(),
        required=True,
        empty_label=mark_safe('<span style="font-style: italic;color:#6c757d;">(Device Asset Number)</span>'),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style: italic;color:#6c757d;', 'list': 'datalistOptions'})

    )


class Warranty(forms.ModelForm):
    Name = forms.CharField(
        label='Manufacturer Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Samsung, Toshiba, etc...'})

    Date =

    Valid =

    WarrantyPDF =

    )

class Companies(forms.ModelForm):
    supplier = forms.ModelchoiceField(
            lable=mark_safe('<span style="font-style: italic;">Supplier</span>'),
            queryset=supplier.objects.all(),
            required=True,
            empty_label=mark_safe('<span style="font-style: italic;color:#6c757d;"'),
            widget = forms.Select(attrs={'class': 'form-control', 'style': 'font-style: italic;color:#6c757d;', 'list': 'datalistOptions'})

    Manufacturer = forms.ModelchoiceField(
            lable=mark_safe('<span style="font-style: italic;">Manufacturer</span>'),
            queryset=Manufacturer.objects.all(),
            required=True,
            empty_label=mark_safe('<span style="font-style: italic;color:#6c757d;'),
            widget = forms.Select(attrs={'class': 'form-control', 'style': 'font-style: italic;color:#6c757d;', 'list': 'datalistOptions'})

    agentCompany = forms.ModelchoiceField(
            lable=mark_safe('<span style="font-style: italic;">agentCompany</span>'),
            queryset=agentCompany.objects.all(),
            required=True,
            empty_label=mark_safe('<span style="font-style: italic;color:#6c757d;"'),
            widget = forms.Select(
            attrs={'class': 'form-control', 'style': 'font-style: italic;color:#6c757d;', 'list': 'datalistOptions'})