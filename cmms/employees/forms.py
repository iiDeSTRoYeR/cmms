from django import forms
from .models import *
from supplier.models import User
from django.utils.html import mark_safe
from modeltranslation.forms import TranslationModelForm
from django.utils.translation import gettext_lazy as _

