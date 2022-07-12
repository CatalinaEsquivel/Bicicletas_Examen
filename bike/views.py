from ast import Return
from email import message
from django.shortcuts import render, redirect, HttpResponse
from .models import Bicicleta
from .forms import BicicletaForm, CustomUserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login
from bike.Carrito import Carrito


# Create your views here.
def index(request):
    return render(request,'bicicleta/index.html')

def bicicletas(request):
    return render(request,'bicicleta/bicicletas.html')

def iniciosesion(request):
    return render(request,'bicicleta/iniciosesion.html')

def registro(request):
    return render(request,'bicicleta/registro.html')

def home(request):
    datos = {
        'bicicletas':Bicicleta.objects.all()
    }
    ListaBicicletas = Bicicleta.objects.all()
    datos = {'bicicletas':ListaBicicletas}
    return render(request, 'bicicleta/index.html',datos)

def form_bicicleta(request):
    form = BicicletaForm()
    return render(request, 'bicicleta/form_bicicleta.html',{'form':form})

def form_bicicleta(request):
    datos = {
        'form':BicicletaForm()
    } 
    if(request.method == 'POST'):
        bicicleta = BicicletaForm(request.POST, files=request.FILES)
        if bicicleta.is_valid():
            bicicleta.save()
            datos['mensaje'] = 'Guardados correctamente'
    return render(request, 'bicicleta/form_bicicleta.html', datos)

def form_mod_bicicleta(request, id):
    bicicleta = Bicicleta.objects.get(idBicicleta=id)
    
    datos = {
        'form':BicicletaForm(instance=bicicleta)
    }
    
    if request.method == 'POST':
        bicicleta = BicicletaForm(data = request.POST, instance = bicicleta, files=request.FILES)

        if bicicleta.is_valid():
            bicicleta.save() #modificar a la BD
            messages.success(request, "Modificado correctamente")
            datos['mensaje'] = 'Modificado correctamente'
        else:
            datos['mensaje'] = 'NO se modificó Bicicleta'
    
    return render(request, 'bicicleta/form_mod_bicicleta.html', datos)

def form_de_bicicleta(request, id):
    bicicleta = Bicicleta.objects.get(idBicicleta=id)
    bicicleta.delete()    
    messages.success(request, "Eliminado Correctamente")
    return redirect(to='home')

def register(request):
    data = {
        'form':CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado con éxito")
            return redirect(to="index")
        data["form"] = formulario
    return render(request, 'bicicleta/registration/register.html', data)

#carrito de compras
def tienda(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, 'bicicleta/tienda.html', {'bicicletas':bicicletas})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    bicicletas = Bicicleta.objects.get(idBicicleta=producto_id)
    carrito.agregar(bicicletas)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    bicicletas = Bicicleta.objects.get(idBicicleta=producto_id)
    carrito.eliminar(bicicletas)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    bicicletas = Bicicleta.objects.get(idBicicleta=producto_id)
    carrito.restar(bicicletas)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")