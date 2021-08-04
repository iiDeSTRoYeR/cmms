from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# from cmms.supplier.models import *
# from cmms.spareparts.models import *
#
# Create your models here.
# هنا مهم نحط ال choices




class AccModel(models.Model):
    Name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.Name


class Accessory(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    accmodel = models.ForeignKey(AccModel, on_delete=models.CASCADE)
    #devices = models.ManyToManyField('Device')

    def __str__(self):
        return self.Name


class AccDetails(models.Model):
    Description = models.TextField(max_length=500)
    SerialNo = models.CharField(max_length=50, unique=True)
    accessory = models.OneToOneField(Accessory, on_delete=models.CASCADE)

    def __str__(self):
        return self.Description

class DeviceStatus(models.Model):
    x = [('Operational', 'Operational'), ('Malfunctioning', 'Malfunctioning')]
    Name = models.CharField(max_length=50, unique=True, choices=x)
    Condition = models.TextField(max_length=300)  # Only mandatory when Malfunctioning

    def __str__(self):
        return self.Name

class DeviceMaintType(models.Model):
    x = [
        ('Biomedical', 'Biomedical'), ('Electrical', 'Electrical'), ('Electronic', 'Electronic'),
        ('Mechanical', 'Mechanical'), ('Electromechanical', 'Electromechanical')
    ]
    Name = models.CharField(max_length=50, choices=x, unique=True)

    def __str__(self):
        return self.Name


class DeviceClass(models.Model):
    x = [
        ('A', 'A'), ('B', 'B'), ('C', 'C')
    ]
    Name = models.CharField(max_length=10, unique=True, choices=x)

    def __str__(self):
        return self.Name


class Device(models.Model):
    Name = models.CharField(
        max_length=50, unique=True, validators=[MinLengthValidator(3, "Minimum Length of a device's name is 3 letters")]
                            )
    PPM_Cycle = models.IntegerField(null=True, blank=True, default=180)
    Brief_Function_Description = models.TextField(max_length=300)
    accessories = models.ManyToManyField(Accessory, blank=True)
    deviceclass = models.ForeignKey(DeviceClass, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Name

class Frequency(models.Model):
    x = [
        ('60', 60), ('50', 50), ('60/50', '60/50'),
        ('DC', 'DC')
    ]
    Value = models.CharField(max_length=5, unique=True, choices=x)

    def __str__(self):
        return str(self.Value)


class Phase(models.Model):
    Value = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return str(self.Value)

class Model(models.Model):
    Name = models.CharField(
        max_length=50, validators=[MinLengthValidator(3, "Minimum Length of a Model's name is 3 letters")]
                            )
    Voltage = models.DecimalField(max_digits=8, decimal_places=2)
    Amperage = models.DecimalField(max_digits=6, decimal_places=2)
    phase = models.ForeignKey('Phase', on_delete=models.SET_NULL, null=True)
    frequency = models.ForeignKey('Frequency', on_delete=models.SET_NULL, null=True)
    manufacturer = models.ForeignKey('supplier.Manufacturer', null=True, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering =['Name']
    def __str__(self):
        return self.Name


class Campus(models.Model):
    Name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Name


class College(models.Model):
    Name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.Name

class Department(models.Model):
    Name = models.CharField(max_length=128, unique=True)
    college = models.ForeignKey(College, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Name
'''
class Operator(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    Phone_Number = models.IntegerField(

        default=None)
'''
class BldgNo(models.Model):
    Number = models.IntegerField()
    GPSCoor = models.CharField(max_length=100)

    def __str__(self):
        return "Building Number: " + str(self.Number)


class LabRoom(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    Department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    #Operator = models.ForeignKey(Operator, on_delete=models.SET_NULL, null=True)
    FloorNo = models.IntegerField()
    Operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    campus = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True)
    blgdno = models.ForeignKey(BldgNo, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return "Lab Number: " + str(self.Name)


class DeviceAsset(models.Model):
    Asset_No = models.IntegerField(primary_key=True, unique=True, blank=True)
    Serial_Number = models.CharField(max_length=50)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    lab = models.ForeignKey(LabRoom, null=True, on_delete=models.SET_NULL, blank=True)
    warranty = models.OneToOneField('supplier.Warranty', null=True, on_delete=models.SET_NULL, blank=True)
    DevicePic = models.FileField("Devices/pictures/")  # need to define file structure
    DownTime = models.DateTimeField(null=True, blank=True)  # joborder.dateopen - joborder.dateclosed
    DeviceStatus = models.ForeignKey(DeviceStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.Asset_No)