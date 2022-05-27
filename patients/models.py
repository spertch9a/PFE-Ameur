from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Patient(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    telephon = models.CharField(max_length=255)

    def  __str__(self) -> str:
        return self.nom


class Image(models.Model):
    prediction =  models.CharField(max_length=255) 
    image = models.ImageField(upload_to="images/")
    patient = models.ForeignKey(Patient, on_delete= models.CASCADE, related_name='images')

    def  __str__(self) -> str:
        return self.prediction   


