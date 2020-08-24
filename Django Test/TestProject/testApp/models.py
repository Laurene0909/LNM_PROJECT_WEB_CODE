from django.db import models

# Create your models here.
class SocDod(models.Model):
    SoC = models.CharField(max_length=100)
    DoD = models.CharField(max_length=100)
    timeStamp = models.CharField(max_length=100)

    
