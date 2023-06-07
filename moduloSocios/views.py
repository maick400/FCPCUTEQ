from django.shortcuts import render, redirect
from django.contrib import messages
from moduloSocios.forms import *

# Create your views here.
def crear_socio(request):
    
    pag_titulo = 'Crear Usuario'
    frm_crear = frm_crear_socio
    
    if request.method == 'GET':
        return render(request, 'socios/socio_crear.html', {'title':pag_titulo,'frm':frm_crear})
    
    
    if request.method  == 'POST':
        frm_crear = frm_crear_socio(request.POST)
        if frm_crear.is_valid():
            frm_crear.save()
            messages.success(request, 'Se ha generado corectamente el formulario')
            return redirect('core:home')
        else:
            messages.warning(request, 'Se ha generado un error desconocido')
            return render(request, 'socios/socio_crear.html', {'title':pag_titulo,'frm':frm_crear})


def modify(request):
    pass
