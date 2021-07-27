from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=50, unique = True)
    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    agentcompanies = models.ManyToManyField('AgentCompany')
    def __str__(self):
        return self.name

class AgentCompany(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    manufacturers = models.ManyToManyField(Manufacturer)
    def __str__(self):
        return self.name

class Warranty(models.Model):
    name = models.CharField(max_length=50, unique=True)
    agentCompany = models.ForeignKey(AgentCompany, null = True, on_delete= models.SET_NULL)
    supplier = models.ForeignKey(Supplier, null = True, on_delete= models.SET_NULL)
    warrantyValidation = models.BooleanField(default= True)
    warrantyDate = models.DateField()
    warrantyPDF = models.FileField(upload_to= "WarrantyFiles") #-> أناقش اسم الملف وشكله
    def __str__(self):
        return self.name





