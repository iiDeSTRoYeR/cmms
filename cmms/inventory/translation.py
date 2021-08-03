from .models import *
from modeltranslation.translator import translator, TranslationOptions
from supplier.models import Manufacturer

class ManufacturerTranslationOptions(TranslationOptions):
    fields = ('Name',)

class PhaseTranslationOptions(TranslationOptions):
    fields = ('Value',)

class DeviceTranslationOptions(TranslationOptions):
    fields = ('Name', 'Brief_Function_Description')


translator.register(Manufacturer, ManufacturerTranslationOptions)
translator.register(Device, DeviceTranslationOptions)
translator.register(Phase, PhaseTranslationOptions)


