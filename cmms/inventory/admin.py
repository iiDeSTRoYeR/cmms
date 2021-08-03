from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
from supplier.models import Manufacturer
from .models import *



class ManufacturerAdmin(TranslationAdmin, admin.ModelAdmin):
    model = Manufacturer
    exclude = ('agentcompanies',)

class PhaseAdmin(TranslationAdmin):
    model = Phase

class DeviceAdmin(TranslationAdmin):
    model = Device

# Register your models here.
admin.site.register(DeviceStatus)
admin.site.register(DeviceClass)
admin.site.register(AccModel)
admin.site.register(Accessory)
admin.site.register(AccDetails)
admin.site.register(DeviceMaintType)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Model)
admin.site.register(Campus)
admin.site.register(College)
admin.site.register(Department)
#admin.site.register(Operator)
admin.site.register(LabRoom)
admin.site.register(DeviceAsset)
admin.site.register(BldgNo)
admin.site.register(Phase, PhaseAdmin)
admin.site.register(Frequency)
admin.site.register(Manufacturer, ManufacturerAdmin)








