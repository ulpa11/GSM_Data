from django.db import models

# Create your models here.
class GSM(models.Model):
    d1=models.CharField(max_length=200)
    d2=models.CharField(max_length=200)
