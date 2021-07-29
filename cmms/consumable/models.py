from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from datetime import datetime


class CostClass (models.Model):
    x = [
        ('محروقات','محروقات'),('ايجار','ايجار'),('مواصلات','مواصلات'),('مستهلكات','مستهلكات'),
        ('مصروفات أخرى','مصروفات أخرى')
    ]
    #محروقات,ايجار,مواصلات,مستهلكات,مصروفات اخرى
    Title = models.CharField(max_length=50, choices=x)

    def __str__(self):
        return self.Title


class CostType (models.Model):
    Name = models.CharField(
        max_length=50,
        unique=True,
        validators=[MinLengthValidator(4, "CostType must be greater than 4 characters")]
    )
    CostClass = models.ForeignKey(CostClass, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.Name


class Consumable (models.Model):
    Price = models.DecimalField(decimal_places=2, max_digits=9, default=0)
    CostType = models.ForeignKey(CostType, on_delete=models.SET_NULL,null=True)
    Member = models.ForeignKey('employees.Member', on_delete=models.SET_NULL,null=True)
    DateofBill = models.DateField(null=True)
    Billpdf = models.FileField(null=True, upload_to="bills/")

    def save(self, *args, **kwargs):
        if self.DateofBill is None:
            self.DateofBill = datetime.now()
        super().save(*args, **kwargs)


    def __str__(self):
        return "Cost Type " + str(self.CostType) + " price is:" + str(self.Price)


def fun(x):
    return x



