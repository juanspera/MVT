from django.shortcuts import render
from .models import Familia

# Create your views here.
def home(request):
    return render(request, 'home.html', context={})

def crear_familia(request):
    familia = Familia.objects.create(name ="Juan", edad=41, fecha_nac="1980-09-23")
    context = {'familia': familia}

    return render(request, 'home.html', context)

def ver_familia(request):
    familiares = Familia.objects.all()
    context = {'familia': familiares}

    return render(request, 'home.html', context)