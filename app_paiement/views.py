from django.shortcuts import render

# create you views here.

def index(request):
    return render(request,'index.html')