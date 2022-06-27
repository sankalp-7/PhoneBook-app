from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class contactform(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^[0-9]{10}$')
    phone= models.CharField(validators=[phone_regex], max_length=10) 
    