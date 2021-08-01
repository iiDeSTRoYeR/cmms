from django import forms
from .models import *
from supplier.models import Manufacturer

class ManuForm(forms.ModelForm):

    Name = forms.CharField(
        required=True, label='Manufacturer Name',
        widget=forms.TextInput(attrs={'placeholder': 'Samsung, Toshiba, etc...'})
    )

    class Meta:
        model = Manufacturer
        fields = ['Name']