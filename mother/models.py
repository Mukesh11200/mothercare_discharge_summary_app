from django.db import models

# Create your models here.
class dischargepatient(models.Model):
    patientname = models.CharField(max_length=250)
    age = models.IntegerField()
    sex = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    
    
    def __str__(self):
        return self.patientname