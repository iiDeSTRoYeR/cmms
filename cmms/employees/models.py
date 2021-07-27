from django.db import models


class Member(models.Model):
    National_ID = models.IntegerField(null=False,unique=True, primary_key=True)
    Name = models.CharField(max_length=50,unique=True)
    DoB = models.DateField(default=None)
    PassportNo = models.IntegerField(null=False,unique=True)
    ExpSCE = models.DateField(default=None)
    ExpID = models.DateField(default=None)
    ExpPassPort = models.DateField(default=None)
    Qualification = models.TextField(max_length=500)
    Title = models.CharField(max_length=100)
    Experience = models.TextField(max_length=500)
    MobileNo = models.IntegerField(null=False,unique=True)
    Nationality = models.CharField(max_length=50,null=False)
    Salary = models.IntegerField(null=False)
    Lapses = models.IntegerField(default=None)
    Warnings = models.CharField(max_length=200)
    ID_PDF = models.FileField(null=False)              #need to define file structure
    Cert_PDF = models.FileField(null=False)            #need to define file structure
    CV_PDF = models.FileField(null=False)              #need to define file structure
    Contract_PDF = models.FileField(null=False)        #need to define file structure
    Effective_PDF = models.FileField(null=False)       #need to define file structure
    Passport_PDF = models.FileField(default=None)      #need to define file structure
    SCE_PDF = models.FileField(default=None)           #need to define file structure
    Experience_PDF = models.FileField(default=None)     #need to define file structure

    #joborders = models.ManyToManyField('tasks.JobOrder', through='tasks.JobRole', through_fields=('member','joborder'))
    #ppms = models.ManyToManyField('tasks.PPM', through='tasks.PPMRole', through_fields=('member','ppm'))

    def __str__(self):
        return str(self.Name)


class Vehicle(models.Model):
    VehicleType = models.CharField(max_length=50,null=False)
    Manufacturer = models.CharField(max_length=50,null=False)
    Model = models.CharField(max_length=50,null=False)
    YearMake = models.IntegerField(null=False)
    Plate = models.CharField(max_length=50,null=False)
    ExpRegistration = models.DateField(null=False)
    ExpInsurance = models.DateField(null=False)
    ExpInspection = models.DateField(null=False)
    Member = models.ForeignKey(Member,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.VehicleType


class ToolType(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class Tool(models.Model):
    ToolType = models.ForeignKey(ToolType,on_delete=models.SET_NULL, null=True)
    QTY =models.IntegerField(default=0)
    Price = models.DecimalField(decimal_places=2 ,max_digits=9)
    Member = models.ForeignKey(Member,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.ToolType


class StrikeDetail(models.Model):
    Name=models.CharField(max_length=200)
    Weight=models.IntegerField(null=False)

    def __str__(self):
        return self.Name


class Strike(models.Model):
    TimeStamp = models.DateField(default=None)
    Member = models.ForeignKey(Member,on_delete=models.SET_NULL,null=True)
    StrikeDetail = models.ForeignKey(StrikeDetail,on_delete=models.SET_NULL,null=True)
    StrikePic = models.FileField(default=None)         # need to define file structure

    def __str__(self):
        return self.StrikeDetail


class LocationsLog (models.Model):
    InTime = models.DateTimeField(auto_now_add=True)
    OutTime = models.DateTimeField(auto_now_add=True)
    Member = models.ForeignKey(Member, on_delete=models.SET_NULL,null=True)
    Lab= models.ForeignKey('inventory.LabRoom', on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.Lab






















