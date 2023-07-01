from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.db.models import Q
from django.core.paginator import Paginator


from moduloFondo.forms.form_FND_modulo import *
from moduloFondo.model.model_FND_modulo import *

#--------------------------------------------------- FND_MODULOS ---------------------------------------------------#
#LISTAR MODULOS
@permission_required('moduloFondo.view_model_fnd_modulo')
def listar_modulos(request):
    pag_titulo = 'Lista de módulos'
    modulo = Model_FND_modulo.objects.all()

    paginator = Paginator(modulo, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, urls_modulo['listar'], {'title': pag_titulo, 'pagina_paginator': page_obj})
#FIN LISTAR MODULOS


#AGREGAR MÓDULO
@permission_required('moduloFondo.add_model_fnd_modulo') #type: ignore
def agregar_modulo(request):
    pag_titulo = 'Registrar módulo'
    frm_crear = Frm_Modulo

    if request.method == 'GET':
        return render(request, urls_modulo['crear'], {'title':pag_titulo,'frm':frm_crear})
    if request.method  == 'POST':
        frm_crear = Frm_Modulo(request.POST, request.FILES)
        print( Frm_Modulo(request.POST, request.FILES))
        if frm_crear.is_valid():
            frm_crear.save()
            messages.success(request, 'Se ha generado corectamente el formulario')
            return redirect('fondo:listar_modulo')
        else:
            messages.warning(request, 'Se ha generado un error desconocido')
            return render(request, urls_modulo['crear'], {'title':pag_titulo,'frm':frm_crear})
#FIN AGREGAR MÓDULO

#EDITAR MÓDULO
def editar_modulo(request, pk):
    modulo = get_object_or_404(Model_FND_modulo, pk=pk)
    form = Frm_Modulo(instance=modulo)
    pag_titulo = 'Editar módulo'
    if request.method == 'POST':
        form = Frm_Modulo(request.POST, instance=modulo)
        if form.is_valid():
            form.save()
            messages.success(request,"Se ha editado correctamente el tipo de fondo")
            
            # Redirecciona a alguna página de éxito o muestra un mensaje de éxito
            return redirect("fondo:listar_modulo")
        else:
            return render(request, urls_modulo["editar"], 
                      {'form': form, 'tipo_fondo': modulo, 'pk': pk,'title': pag_titulo})
    else:  
        return render(request, urls_modulo["editar"], 
                      {'form': form, 'tipo_fondo': modulo, 'pk': pk,'title': pag_titulo})
    
#FIN EDITAR MÓDULO

#BUSCAR MÓDULO AJAX HTMX
def buscar_modulo(request):
    search_term = ''
    if 'search_term' in request.POST:
        search_term = request.POST['search_term']

    tipo_fondo = Model_FND_modulo.objects.filter(
        Q(id_modulo__icontains=search_term) |
        Q(nombre_modulo__icontains=search_term)
    )

    paginator = Paginator(tipo_fondo, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, urls_modulo["buscar"], {'pagina_paginator': page_obj})

#FIN DE BUSCAR MÓDULO AJAX HTMX