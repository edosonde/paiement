from django.shortcuts import render
from app_paiement.models.frais import *

# create you views here.

def index(request):
    return render(request,'index.html')

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
    if request.methode == 'POST':
        fr = Frais.objects.get(pk=id)
        Fr.delete()
        return HttpResponseRedirect('/frais/')
    else:
        return HttpResponseRedirect('/frais/')
