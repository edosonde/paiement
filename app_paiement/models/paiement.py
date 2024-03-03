from django.db import models
from app_paiement.models.frais import *
from app_paiement.models.eleve import *

class paiement(models.Model):
    codeFrais = models.ForeignKey(Frais,on_delete=models.CASCADE)
    eleve = models.ForeignKey(Eleve,on_delete=models.CASCADE)
    datepaie = models.CharField(max_length=20)
    montant = models.CharField(max_length=10)
