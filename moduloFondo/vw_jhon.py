from moduloFondo.forms.form_FND_solicitudes_generales import *
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.db.models import Q
from moduloFondo.model.model_FND_solicitudes_generales import *
from django.core.paginator import Paginator


#************************ solicitudes generales *********************
#CREAR SOLICITUDES GENERALES
def crear_solicitudes_generales(request):
    pag_titulo="Registrar solicitudes generales"
    frm_crear=frm_Fnd_solicitudes_generales

    if request.method == 'GET':
        return render(request, 'fondo/solicitudes_generales/solicitud_crear.html', {'title':pag_titulo,'frm':frm_crear})
    if request.method == 'POST':
        frm_crear=frm_Fnd_solicitudes_generales(request.POST,request.FILES)
        if frm_crear.is_valid():
            frm_crear.save()
            messages.success(request, 'Se ha generado corectamente el formulario')
            return redirect('core:home')
        else:
            return render(request, 'fondo/solicitudes_generales/solicitud_crear.html', {'title':pag_titulo,'frm':frm_crear})
        

#EDITAR SOLICITUDES GENERALES
def editar_solicitudes_generales(request,pk):
    solicitud_general = get_object_or_404(Model_FND_solicitudes_generales, pk=pk)
    form = frm_Fnd_solicitudes_generales(instance=solicitud_general)
    pag_titulo = 'Editar solicitud general'
    if request.method == 'POST':
        frm_actualizar=frm_Fnd_solicitudes_generales(request.POST,request.FILES,instance=solicitud_general)
        if frm_actualizar.is_valid():
            frm_actualizar.save()
            messages.success(request, 'Se ha generado corectamente el formulario')
            return redirect('core:home')
        else:
            print("holaaaaaaaaaaa")
            return render(request, 'fondo/solicitudes_generales/solicitud_editar.html', 
            {'form': form, 'solicitud_general': solicitud_general, 'pk': pk,'title': pag_titulo})   
    else:
        return render(request, 'fondo/solicitudes_generales/solicitud_editar.html', 
        {'form': form, 'solicitud_general': solicitud_general, 'pk': pk,'title': pag_titulo}) 



# LISTA DE OPERADORAS TELEFONICAS
#@permission_required('moduloFondo.view_model_fnd_operadora_telf')
def listar_solicitudes_generales(request):
    pag_titulo = 'Lista solicitudes generales'
    solicitud_general = Model_FND_solicitudes_generales.objects.all()
    paginator = Paginator(solicitud_general, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "fondo/solicitudes_generales/solicitud_lista.html", {'title': pag_titulo, 'pagina_paginator': page_obj})

  


  #AJAX PARA ACTUALIZAR LA BARRA DE BÚSQUEDA
def buscar_solicitud(request):    
  
    search_term = ''
    if 'search_term' in request.POST:
        search_term = request.POST['search_term']

    solicitud_general = Model_FND_solicitudes_generales.objects.filter(Q(documento__icontains=search_term)).order_by('id_solicitud_general')

    paginator = Paginator(solicitud_general, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'fondo/solicitudes_generales/solicitud_buscar.html', {'pagina_paginator': page_obj})
#FIN AJAX PARA ACTUALIZAR LA BARRA DE BÚSQUEDA