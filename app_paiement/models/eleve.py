from django.db import models
from app_paiement.models.classe import *

class Eleve(models.Model):
    matricule = models.CharField(max_length=20,primary_key=True)
    noms = models.CharField(max_length=30)
    adresse = models.CharField(max_length=30)
    tel = models.CharField(max_length=15)
    codeclass = models.ForeignKey(Classe,on_delete=models.CASCADE)
