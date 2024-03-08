from django.contrib import admin
from app_paiement.models.paiement import *
from app_paiement.models.frais import *
from app_paiement.models.eleve import *
from app_paiement.models.classe import *

# Register your models here.

admin.site.register(paiement)
admin.site.register( Frais)
admin.site.register(Eleve)
admin.site.register(Classe)