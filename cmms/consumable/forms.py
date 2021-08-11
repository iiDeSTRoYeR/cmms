from django import forms
from .models import *
from employees.models import Member
from django.utils.html import mark_safe
from modeltranslation.forms import TranslationModelForm
from django.utils.translation import gettext_lazy as _

class ConsumableForm(forms.ModelForm):
        Price = forms.DecimalField(
            label=_('Price'),
            required=True, decimal_places=2, max_digits=9,
            widget=forms.NumberInput(attrs={'placeholder': _('€,$,SAR')}))

        Member = forms.ModelChoiceField(
            label=_('Member Name'),
            queryset=Member.objects.all(),
            required=True,
            widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style:italic;'}))



        DateofBill = forms.DateTimeField(
        label=_('Date of Bill'),
        input_formats=['%d/%m/%Y %H:%M'],
        required=True,
        widget=forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input','data-target': '#datetimepicker1',}))


        Billpdf = forms.FileField(
        label=_('Bill PDF'),
        required=True,)

        CostClass = forms.ModelChoiceField(
        label=_('Cost Class'),
        queryset=CostClass.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-style:italic;'}))

        CostType = forms.CharField(
        label=_('Cost Type'),
        required=True,
        widget=forms.TextInput(attrs={'placeholder': _('Gasoline, gas, food, etc...')}))

        class Meta:
            model = Consumable
            fields = ['Price', 'Member', 'DateofBill', 'Billpdf',]




