from .models import *
from modeltranslation.translator import translator, TranslationOptions
from supplier.models import Manufacturer

class PhaseTranslationOptions(TranslationOptions):
    fields = ('Value',)

class DeviceTranslationOptions(TranslationOptions):
    fields = ('Name', 'Brief_Function_Description')

class AccessoryTranslationOptions(TranslationOptions):
    fields = ('Name', 'Description')


translator.register(Device, DeviceTranslationOptions)
translator.register(Phase, PhaseTranslationOptions)
translator.register(Accessory, AccessoryTranslationOptions)


