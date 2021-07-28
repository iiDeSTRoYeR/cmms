from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator
from django.contrib.auth.models import User
from datetime import datetime

class Nationality (models.Model):
    x = [
        ('Saudi', 'Saudi'), ('Egyptian', 'Egyptian'), ('Sudanese', 'Sudanese'), ('Indian', 'Indian'), ('Pakistani', 'Pakistani')
    ]
    Name = models.CharField(max_length=20, unique=True, choices=x)

    def __str__(self):
        return self.Name

class JobTitle (models.Model):
    x = [
        ('Engineer','Engineer'), ('Technician', 'Technician'), ('Labor', 'Labor'), ('Administrator', 'Administrator')
    ]
    Name = models.CharField(max_length=100, choices=x, unique=True)

    def __str__(self):
        return self.Name

class Member(models.Model):
    National_ID = models.BigIntegerField(
        unique=True, primary_key=True,
        validators=[MinValueValidator(1000000000,'Please Enter 10 Numbers.'), MaxValueValidator(9999999999, 'Please Enter Less than 10 Numbers.')]

    )
    Name = models.CharField(max_length=50, validators=[MinLengthValidator(4,'Name Must be 4 characters.')])
    DoB = models.DateField()
    nationality = models.ForeignKey(Nationality, on_delete=models.SET_NULL, null=True)
    PassportNo = models.CharField(max_length=20, unique=True, null=True)
    ExpSCE = models.DateField(null=True, blank=True)
    ExpID = models.DateField(null=True)         #Saudis don't have exp for ID
    ExpPassport = models.DateField(null=True)    #Saudis don't have exp for Passport
    Qualification = models.CharField(max_length=200)
    jobtitle = models.ForeignKey(JobTitle, on_delete=models.SET_NULL, null=True)
    Experience = models.IntegerField()
    MobileNo = models.IntegerField(
        unique=True,
        validators=[MinValueValidator(500000000, 'Please Enter 10 Numbers.'),
                    MaxValueValidator(599999999, 'Please Enter Less than 10 Numbers.')]
    )
    Salary = models.DecimalField(max_digits=9, decimal_places=2)
    Lapses = models.IntegerField(default=None, null=True, blank=True)
    Warnings = models.IntegerField(default=None, null=True, blank=True)
    ID_PDF = models.FileField(upload_to="employees/id/")
    Cert_PDF = models.FileField(upload_to="employees/Certs")
    CV_PDF = models.FileField(upload_to="employees/CVs")
    Contract_PDF = models.FileField(upload_to="employees/Contracts")
    Effective_PDF = models.FileField(upload_to="employees/Effectives")
    Passport_PDF = models.FileField(upload_to="employees/Passports", null=True, default=None)
    SCE_PDF = models.FileField(upload_to="employees/SCEs", null=True, default=None)
    Experience_PDF = models.FileField(upload_to="employees/Experiences", null=True, default=None)

    #joborders = models.ManyToManyField('tasks.JobOrder', through='tasks.JobRole', through_fields=('member','joborder'))
    #ppms = models.ManyToManyField('tasks.PPM', through='tasks.PPMRole', through_fields=('member','ppm'))

    def __str__(self):
        return str(self.Name)


class Vehicle(models.Model):
    x = [
        ('Sedan', 'Sedan'), ('Truck', 'Truck')
    ]
    VehicleType = models.CharField(max_length=50, default='Sedan', choices=x)
    Manufacturer = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    YearMake = models.IntegerField()
    Plate = models.CharField(max_length=50)
    ExpRegistration = models.DateField()
    ExpInsurance = models.DateField()
    ExpInspection = models.DateField()
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return self.VehicleType


class ToolType(models.Model):
    Name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(4, "Tool minimum length is 4 characters")],
        unique=True
    )

    def __str__(self):
        return self.Name


class Tool(models.Model):
    tooltype = models.ForeignKey(ToolType, on_delete=models.CASCADE, default=None)
    QTY = models.IntegerField(default=1)
    Price = models.DecimalField(decimal_places=2 ,max_digits=9)
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Tool Type: " + str(self.ToolType)


class StrikeDetail(models.Model):
    Name = models.CharField(
        max_length=200, unique=True,
    )
    Weight = models.IntegerField(default=1)

    def __str__(self):
        return self.Name


class Strike(models.Model):
    TimeStamp = models.DateTimeField(blank=True, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, default=None)
    strikedetail = models.ForeignKey(StrikeDetail, on_delete=models.CASCADE, default=None)
    StrikePic = models.FileField(upload_to="strikes/%Y/%m/%d")         # need to define file structure

    def save(self, *args, **kwargs):
        if self.TimeStamp is None:
            self.TimeStamp = datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.StrikeDetail


class LocationsLog (models.Model):
    InTime = models.DateTimeField(auto_now_add=True)
    OutTime = models.DateTimeField(auto_now=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, default=None)
    lab = models.ForeignKey('inventory.LabRoom', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "Log of " + str(self.member) + "<-->" + str(self.lab)






















