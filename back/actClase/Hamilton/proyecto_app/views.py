from django.shortcuts import render, redirect
from proyecto_app.models import Persona
# Create your views here.

def home(request):
    return render(request,'home.html')

def registrar_persona(request):
    if request.method == 'POST':#Preguntar si el formulario uso el metodo POST
        if (request.POST.get('tipo_doc') and request.POST.get('documento') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('telefono') and request.POST.get('genero')): 
            persona = Persona()
            persona.tipo_doc=request.POST.get('tipo_doc')
            persona.documento=request.POST.get('documento')
            persona.nombre=request.POST.get('nombre')
            persona.apellido=request.POST.get('apellido')
            persona.telefono=request.POST.get('telefono')
            persona.genero=request.POST.get('genero')
            persona.save()
            return redirect('home')
    else:
        return render(request,'persona/registrar.html')
        
        
        # return render(request,'persona/registrar.html')