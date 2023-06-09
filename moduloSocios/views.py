from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from moduloSocios.forms.forms  import *
from django.db.models import Q




@login_required
@permission_required('moduloSocios.crear_socio_prms')
# Create your views here.
def crear_socio(request):
    
    pag_titulo = 'Crear Usuario'
    
    frm_crear = frm_crear_socio
    filtros = Frm_filtros_busqueda
    socios = Socio.objects.all()

    
    if request.method == 'GET':
        return render(request, 'socios/socio_crear.html',
                       {'title':pag_titulo,'frm':frm_crear, 
                        'filtros':filtros ,'socios':socios})
    
    
    if request.method  == 'POST':
        frm_crear = frm_crear_socio(request.POST)
        if frm_crear.is_valid():
            frm_crear.save()
            messages.success(request, 'Se ha generado corectamente el formulario')
            return redirect('core:home')
        else:
            messages.warning(request, 'Se ha generado un error desconocido')
            messages.warning(request, 'Se ha generado un error desconocido')
            messages.warning(request, 'Se ha generado un error desconocido')
            messages.warning(request, 'Se ha generado un error desconocido')
            messages.warning(request, 'Se ha generado un error desconocido')
            messages.warning(request, 'Se ha generado un error desconocido')
            messages.warning(request, 'Se ha generado un error desconocido')
            messages.warning(request, 'Se ha generado un error desconocido')
            messages.warning(request, 'Se ha generado un error desconocido')
            return render(request, 'socios/socio_crear.html', {'title':pag_titulo,'frm':frm_crear})


def modify(request):
    pass

def buscar_socio(request):
    if request.method == 'POST':
        cedula = request.POST.get("cedula")
    
        socios = Socio.objects.all().filter( Q(cedula__icontains= cedula) | Q(nombres__icontains=cedula) )
        return render (request, 'socios/tables/seleccionar-socio-tabla.html', 
                       { 
                        'socios':socios
                        } )
    else:
        pass
    