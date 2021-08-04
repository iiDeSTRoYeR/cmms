from django import forms
from .models import *
from inventory.models import DeviceAsset
from django.utils.html import mark_safe

class AddNewWarrantyForm(forms.ModelForm):

    DeviceAssets=forms.ModelchoiceField(
        lable=mark_safe('<span style="font-style: italic;">DeviceAsset</span>'),
        queryset=DeviceAsset.objects.all(),
        required=True,
        empty_label=mark_safe('<span style="font-style: italic;color:#6c757d;">(Device Asset Number)</span>'),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style: italic;color:#6c757d;', 'list':'datalistOptions'}),)

    class Meta:
        model = Warranty
        fields = '__all__'

    Name = forms.CharField(
        required=True,
        label=_('Warranty Name'),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style:italic; color:#6c757d;'}),
    )
    Date = forms.DateField(
        widget=forms.SelectDateWidget('%m/%d/%y'),
        available=forms.BooleanField(label='Valid'),
    )

    # class GeeksForm(forms.Form):
    # Name =forms.CharField(
    # geeks_field=forms.FileField(label='Warranty File',
    # required=True,))


    supplier= forms.ModelchoiceField(
        lable=mark_safe('<span style="font-style: italic;">Supplier</span>'),
        required=True,
        label=_('Warranty Name'),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style:italic; color:#6c757d;'}),
    )

    Manufacturer = forms.ModelchoiceField(
        lable=mark_safe('<span style="font-style: italic;">Manufacturer</span>'),
        queryset=Manufacturer.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style: italic;color:#6c757d;', 'list': 'datalistOptions'}),)

    agentCompany = forms.ModelchoiceField(
        lable=mark_safe('<span style="font-style: italic;">agentCompany</span>'),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style: italic;color:#6c757d;','list': 'datalistOptions'}),)
