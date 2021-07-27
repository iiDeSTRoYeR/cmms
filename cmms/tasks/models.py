from django.db import models
from datetime import datetime, timedelta
#from django.apps import apps
#Device = apps.get_model('inventory', 'Device')
from inventory.models import DeviceAsset


class JobOrder(models.Model):
    rate_scale = [
        ('Unacceptable', 1), ('Poor', 2), ('Fair', 3), ('Good', 4), ('Excellent', 5)
    ]
    Title = models.CharField(max_length=128)
    DeviceAsset = models.ForeignKey('inventory.DeviceAsset', on_delete=models.SET_NULL, null=True)
    OpenDate = models.DateTimeField(auto_now_add=True, blank=True)
    CloseDate = models.DateTimeField(blank=True)  # if blank then status is open
    ProblemDesc = models.TextField(max_length=500)
    Rating = models.IntegerField(null=True, blank=True, choices=rate_scale)
    Notes = models.TextField(null=True, blank=True)
    members = models.ManyToManyField('employees.Member', through='JobRole', through_fields=('joborder', 'member'))
    generalsps = models.ManyToManyField('spareparts.GeneralSP')

    def __str__(self):
        return self.Title

class PPM(models.Model):
    DeviceAsset = models.ForeignKey('inventory.DeviceAsset', on_delete=models.SET_NULL, null=True)
    CurrentPPM = models.DateTimeField(auto_now_add=True, blank=True)
    FuturePPM = models.DateTimeField(null=True, blank=True)  # from the Device Table
    members = models.ManyToManyField('employees.Member', through='PPMRole', through_fields=('ppm', 'member'))

    @staticmethod
    def ppmCycleVal(deviceasset):
        Query1 = DeviceAsset.objects.get(pk=deviceasset)
        return int(Query1.device.PPM_Cycle)

    def __str__(self):
        return str (self.CurrentPPM)

class roleName(models.Model):
    roles = [
        ('Leader', 'Leader'), ('Member','Member')
    ]
    name = models.CharField(max_length=50, choices=roles)

    def __str__(self):
        return self.name

class JobRole(models.Model):
    joborder = models.ForeignKey(JobOrder, on_delete=models.CASCADE)
    member = models.ForeignKey('employees.Member', on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(roleName, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Member " + str(self.member) + " <--> Joborder " + str(self.joborder) + "| role: " + str(self.role)

class PPMRole(models.Model):
    ppm = models.ForeignKey(PPM, on_delete=models.CASCADE)
    member = models.ForeignKey('employees.Member', on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(roleName, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Member " + str(self.member) + " <--> PPM " + str(self.ppm) + "| role: " + str(self.role)


'''
class Team(models.Model):
    #joborder_id = models.ForeignKey(JobOrder, on_delete=models.CASCADE)
    names = [
        ('A', 'A'), ('B', 'B'), ('C', 'C')
    ]
    Name = models.CharField(max_length=1, choices=names, null=True)
    member = models.ManyToManyField('employees.Member', through='MemRole', through_fields=('team', 'member'))

    def __str__(self):
        return self.Name
        
        
class MemRole(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    member = models.ForeignKey('employees.Member', on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(roleName, on_delete=models.SET_NULL, null=True)
    
    
    '''