from django.shortcuts import render, redirect
from django.db import connection

def home(request):
    return render(request,'Productos/home.html')

def producto_insertar(request):
    if request.method=='POST':
        if(
            request.POST.get('codigo')
            and request.POST.get('descripcion')
            and request.POST.get('presentacion')
            and request.POST.get('valor_unitario')
            and request.POST.get('stock')
            and request.POST.get('activo')
        ):
            cursor_producto=connection.cursor()
            codigo=request.POST.get('codigo')
            descripcion=request.POST.get('descripcion')
            presentacion=request.POST.get('presentacion')
            valor_unitario=request.POST.get('valor_unitario')
            stock=request.POST.get('stock')
            activo=request.POST.get('activo')
            cursor_producto.execute("call insertarProducto('"+codigo+"','"+descripcion+"','"+presentacion+"','"+valor_unitario+"','"+stock+"','"+activo+"')")
            return redirect('mostrar')

    else:
        return render(request,'Productos/insertar.html')
    
def producto_listar(request):
    listado_producto=connection.cursor()
    listado_producto.execute("call verProductos()")
    return render(request, 'Productos/mostrar.html',{'listado_producto' : listado_producto})

def render_mision(request):
    return render (request,'Productos/mision.html')

def render_vision(request):
    return render(request,'Productos/vision.html')

