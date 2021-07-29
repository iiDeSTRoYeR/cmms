from django.db import models


# from cmms.supplier.models import *
# from cmms.spareparts.models import *
#
# Create your models here.
# هنا مهم نحط ال choices
class DeviceStatus(models.Model):
    x = [('Operational', 'Operational'), ('Malfunctioning', 'Malfunctioning')]
    name = models.CharField(max_length=50, unique=True, choices=x)
    condition = models.CharField(max_length=200)  # Only mandotory when Malfunctioning

    def __str__(self):
        return self.name


class DeviceClass(models.Model):
    x = [
        ('A', 'A'), ('B', 'B'), ('C', 'C')
    ]
    name = models.CharField(max_length=10, unique=True, choices=x)

    def __str__(self):
        return self.name


class AccModel(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Accessory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    AccModel_id = models.ForeignKey(AccModel, on_delete=models.CASCADE)
    devices = models.ManyToManyField('Device')

    def __str__(self):
        return self.name


class AccDetails(models.Model):
    Description = models.CharField(max_length=500)
    SerialNo = models.IntegerField()
    accessory = models.OneToOneField(Accessory, on_delete=models.CASCADE)

    def __str__(self):
        return self.Description


class DeviceMainType(models.Model):
    x = []
    name = models.CharField(max_length=50, choices=x)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=50, unique=True)
    PPM_Cycle = models.IntegerField(null=True, blank=True)
    BriefFunctionDes = models.TextField()
    accessories = models.ManyToManyField(Accessory)
    Device_class = models.ForeignKey(DeviceClass, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=50, unique=True)
    manufacturer = models.ForeignKey('supplier.Manufacturer', null=True, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, null=True, on_delete=models.SET_NULL)
    frequency = models.IntegerField()
    voltage = models.DecimalField(max_digits=8, decimal_places=3)
    amperage = models.DecimalField(max_digits=6, decimal_places=3)
    phase = models.IntegerField()

    def __str__(self):
        return self.name


class Campus(models.Model):
    name = models.CharField(max_length=100, unique=True)
    device = models.ForeignKey(Device, null=True, on_delete=models.SET_NULL)


class College(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    college = models.ForeignKey(College, null=True, on_delete=models.SET_NULL)


class Operator(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    Phone_Number = models.IntegerField(default=None)


class LabRoom(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    Department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    Operator = models.ForeignKey(Operator, on_delete=models.SET_NULL, null=True)
    campus = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True)
    BlgdNo = models.IntegerField()
    FloorNo = models.IntegerField()
    GPSCoor = models.CharField(max_length=100)


class DeviceAsset(models.Model):
    Asset_No = models.IntegerField(primary_key=True, unique=True, blank=True)
    Serial_Number = models.CharField(max_length=50)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    lab = models.ForeignKey(LabRoom, null=True, on_delete=models.SET_NULL, blank=True)
    warranty = models.OneToOneField('supplier.Warranty', null=True, on_delete=models.SET_NULL, blank=True)
    DevicePic = models.FileField()  # need to define file structure
    DownTime = models.DateTimeField(null=True, blank=True)  # joborder.dateopen - joborder.dateclosed
    DeviceStatus = models.ForeignKey(DeviceStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        #space
        #space++
        return str(self.Asset_No)
