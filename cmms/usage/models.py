from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UsageRate(models.Model):
    inTimeStamp = models.DateTimeField(auto_now_add=True)
    deviceuser = models.ForeignKey(User, on_delete=models.CASCADE)
    Duration = models.DateTimeField(blank=True, null=True)
    outTimeStamp = models.DateTimeField(null=True, blank=True)
    deviceasset = models.ForeignKey('inventory.DeviceAsset', on_delete=models.CASCADE)

