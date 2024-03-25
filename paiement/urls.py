"""
URL configuration for paiement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_paiement.views import *
from app_paiement.views import *
from app_paiement.views import Eleve
from app_paiement.views import Paiement

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',index,name="index"),
    path('frais/',ffrais,name="ffrais"),
    path('',dash,name="dash"),
    path('deleteFrais/<str:id>/',deleteFrais, name="deleteFrais"),
    path('classe/',fclasse,name="fclasse"),
    path('ajouterFrais/',ajouterFrais,name="ajouterFrais"),
    path('ajouterclasse/',ajouterclasse,name="ajouterclasse"),
    path('addfrais/',addfrais,name="addfrais"),
    path('addclasse/',addclasse,name="addclasse"),
    path('deleteclasse/<str:id>/',deleteclasse, name="deleteclasse"),
    path('eleve/',feleve,name="feleve"),
    path('paiement/',fpaiement,name="fpaiement"),
    path('deleteeleve/<str:id>/',deleteeleve, name="deleteeleve"),
    path('deletepaiement/<str:id>/',deletepaiement, name="deletepaiement"),
    

   
   
      
]
