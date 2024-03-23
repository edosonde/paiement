from django.shortcuts import render
from app_paiement.models.frais import *
from django.shortcuts import redirect
from app_paiement.models.eleve import *

# create you views here.

def index(request):
    return render(request,'index.html')

def ajouterFrais(request):
    return render(request,'ajouterFrais.html')

def ajouterclasse(request):
    return render(request,'ajouterclasse.html')

def ffrais(request):
    frais = Frais.objects.all()
   # frais = Frais.objects.all().count()
    

    ctx = {"frais": frais,
           "nbrf": len(frais)
    }

    return render(request,'frais.html',ctx)
    
def dash(request):
    return render(request,'dashboard.html')

def deleteFrais(request,id):
  
    fr = Frais.objects.get(pk=id)
    fr.delete()
      
    return redirect('/frais/')

def fclasse(request):
    classe = Classe.objects.all()
    

    ctx = {"classe": classe,
           "nbrc": len(classe)
    }

    return render(request,'classe.html',ctx)


def deleteclasse(request,id):
  
    fc = Classe.objects.get(pk=id)
    fc.delete()
      
    return redirect('/classe/')  

    
def addfrais(request):

    message = None
    if request.method == 'POST':
        codefrais = request.POST["codefrais"]
        libfrais = request.POST["libfrais"]

        rs_frais = Frais.objects.filter(codeFrais=codefrais)

        if len(rs_frais)>0:
            message ="ce code frais existe"
        else:
            frai = Frais(

                codeFrais = codefrais,
                libelle = libfrais,
            )

            frai.save()
            message = "frais enregistre avec succés"

    ctx ={
        'message':message
    }
    return render(request,'ajouterFrais.html',ctx)



def addclasse(request):

    message = None
    if request.method == 'POST':
        codeclass = request.POST["codeclass"]
        libelleclass = request.POST["libelleclass"]

        rs_class = Classe.objects.filter(codeclass=codeclass)

        if len(rs_class)>0:
            message ="ce code classe existe"
        else:
            cls = Classe(

                codeclass = codeclass,
                libelleclass = libelleclass,
            )

            cls.save()
            message = "classe enregistre avec succés"

    ctx ={
        'message':message
    }
    return render(request,'ajouterclasse.html',ctx)


def feleve(request):
    return render(request,'eleve.html')