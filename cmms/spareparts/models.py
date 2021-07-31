from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class SpStatus(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class GeneralSP(models.Model):
    Name = models.CharField(max_length=50, unique=True, validators=[MinLengthValidator(3,'Name Must be 3 characters.')])
    Details = models.CharField(max_length=200)
    PurQTY = models.IntegerField(default=0)
    StbyQTY = models.IntegerField(default=0)
    InstallQTY = models.IntegerField(default=0)
    Purchase_Period = models.IntegerField(null=True, blank=True)
    GeneralSP_PDF = models.FileField(upload_to="spareparts/GeneralSP/")
    Price = models.DecimalField(decimal_places=2, max_digits=9)
    Notes = models.TextField(null=True, blank=True, max_length=500)
    spstatus = models.ForeignKey(SpStatus, on_delete=models.SET_NULL, null=True)
    #joborders = models.ManyToManyField('tasks.JobOrder')

    def __str__(self):
        return self.Name

#
class Sparepart(models.Model):
    Name = models.CharField(max_length=50, unique=True, validators=[MinLengthValidator(3,'Name Must be 3 characters.')])
    Details = models.TextField(max_length=500)
    PurQTY = models.IntegerField(default=0)
    StbyQTY = models.IntegerField(default=0)
    InstallQTY = models.IntegerField(default=0)
    #Purchase_Period = models.IntegerField(null=True, blank=True)
    SparePartPDF = models.FileField(upload_to="spareparts/SparePart/")
    Price = models.DecimalField(decimal_places=2, max_digits=9)
    Notes = models.TextField(null=True, blank=True, max_length=500)
    spstatus = models.ForeignKey(SpStatus, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey('inventory.Model', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Name
