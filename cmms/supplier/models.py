from django.db import models

# Create your models here.
class Supplier(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.Name

class Manufacturer(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    agentcompanies = models.ManyToManyField('AgentCompany')
    def __str__(self):
        return self.Name

class AgentCompany(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    #manufacturers = models.ManyToManyField(Manufacturer)
    def __str__(self):
        return self.Name

class Warranty(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    agentcompany = models.ForeignKey(AgentCompany, null=True, on_delete=models.SET_NULL)
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)
    WarrantyValidation = models.BooleanField(default=True)
    WarrantyDate = models.DateField()
    WarrantyPDF = models.FileField(upload_to="WarrantyFiles/")
    def __str__(self):
        return self.Name





