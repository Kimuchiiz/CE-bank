from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
# Create your models here.

class BankAccount(models.Model):
    user = models.ManyToManyField(User,blank=True)
    number = models.CharField(max_length=30, default='',unique = True)
    firstname = models.CharField(max_length=30, default='')
    surname = models.CharField(max_length=30, default='')
    personal_id = models.CharField(max_length=30, default='')
    pin = models.CharField(max_length=4, default='',validators=[MinLengthValidator(4)])
    balance = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2
        ) 

#class BankUser(models.Model):
#    user = models.OneToOneField(User,on_delete=models.CASCADE)
#    bank_account = models.ForeignKey(BankAccount,on_delete=models.CASCADE)
