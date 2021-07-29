from django.db import models
from datetime import datetime, timedelta
#from django.apps import apps
#Device = apps.get_model('inventory', 'Device')
from django.core.validators import MinLengthValidator
from inventory.models import DeviceAsset
from datetime import datetime
from django.contrib.auth.models import User


class JobOrder(models.Model):
    rate_scale = [
        ('Unacceptable', 1), ('Poor', 2), ('Fair', 3), ('Good', 4), ('Excellent', 5)
    ]
    Title = models.CharField(max_length=128, validators=[MinLengthValidator(10,'Name Must be 10 characters.')])
    deviceasset = models.ForeignKey('inventory.DeviceAsset', on_delete=models.SET_NULL, null=True)
    OpenDate = models.DateTimeField(null=True, blank=True)
    CloseDate = models.DateTimeField(blank=True, null=True)  # if blank then status is open
    ProblemDesc = models.TextField(max_length=500, validators=[MinLengthValidator(20,'Name Must be 20 characters.')])
    Rating = models.IntegerField(null=True, blank=True, choices=rate_scale)
    Notes = models.TextField(null=True, blank=True)
    #members = models.ManyToManyField('employees.Member', through='JobRole', through_fields=('joborder', 'member'))
    members = models.ManyToManyField(User, through='JobRole', through_fields=('joborder', 'member'))
    generalsps = models.ManyToManyField('spareparts.GeneralSP')

    def save(self, *args, **kwargs):
        if self.OpenDate is None:
            self.OpenDate = datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Title

class PPM(models.Model):
    deviceAsset = models.ForeignKey('inventory.DeviceAsset', on_delete=models.SET_NULL, null=True)
    CurrentPPM = models.DateTimeField(blank=True, null=True)
    FuturePPM = models.DateTimeField(null=True, blank=True)  # from the Device Table
    #members = models.ManyToManyField('employees.Member', through='PPMRole', through_fields=('ppm', 'member'))
    members = models.ManyToManyField(User, through='PPMRole', through_fields=('ppm', 'member'))
    def save(self, *args, **kwargs):
        if self.CurrentPPM is None:
            self.CurrentPPM = datetime.now()
        super().save(*args, **kwargs)
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
    Name = models.CharField(max_length=50, choices=roles)

    def __str__(self):
        return self.Name

class JobRole(models.Model):
    joborder = models.ForeignKey(JobOrder, on_delete=models.CASCADE)
    #member = models.ForeignKey('employees.Member', on_delete=models.SET_NULL, null=True)
    member = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(roleName, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Member " + str(self.member) + " <--> Joborder " + str(self.joborder) + "| role: " + str(self.role)

class PPMRole(models.Model):
    ppm = models.ForeignKey(PPM, on_delete=models.CASCADE)
    #member = models.ForeignKey('employees.Member', on_delete=models.SET_NULL, null=True)
    member = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
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