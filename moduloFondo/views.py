from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.db.models import Q


from moduloFondo.forms.form_FND_tipo_descuento  import *
from moduloFondo.forms.form_FND_socios  import *
from moduloFondo.forms.form_FND_parametros_sys  import *
from moduloFondo.forms.form_FND_cargo_empleado  import *
from moduloFondo.forms.form_FND_operadora_telf  import *

from moduloFondo.forms.form_FND_Provincia  import *

from moduloFondo.model.Model_FND_provincia import *



from django.core.paginator import Paginator


#------------------------------------------------- FND_TIPO_DESCUENTO -------------------------------------------------#
# CREAR TIPO DE DESCUENTO
@login_required

#Se debe cambiar el permiso para que sea el de crear socio
@permission_required('moduloFondo.add_model_fnd_tipo_descuento')
def crear_tipo_descuento(request):
    pag_titulo = 'Crear tipo de descuento'
    frm_crear = frm_tipo_descuento
    if request.method == 'GET':
        return render(request, 'fondo/tipo_descuento/tipo_descuento_crear.html', {'title':pag_titulo,'frm':frm_crear})
    if request.method  == 'POST':
        frm_crear = frm_tipo_descuento(request.POST)
        if frm_crear.is_valid():
            frm_crear.save()
            messages.success(request, 'Se ha generado corectamente el formulario')
            return redirect('core:home')
        else:
            messages.warning(request, 'Se ha generado un error desconocido')
            return render(request, 'fondo/tipo_descuento/tipo_descuento_crear.html', {'title':pag_titulo,'frm':frm_crear})

       
# LISTA DE TIPO DE DESCUENTO
#Se debe cambiar el permiso para que sea el de listar los tipos de descuentos
@permission_required('moduloFondo.view_model_fnd_tipo_descuento')
def listar_tipo_descuento(request):
    pag_titulo = 'Listar tipos de descuento'
    tipos_descuento = Model_FND_tipo_descuento.objects.all()
    paginator = Paginator(tipos_descuento, 10)  # Mostrar 10 elementos por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'fondo/tipo_descuento/tipo_descuento_lista.html', {'title': pag_titulo, 'tipos_descuento': page_obj})




# EDITAR DE TIPO DE DESCUENTO


#Se debe cambiar el permiso para que sea el de editar los tipos de descuentos
@permission_required('moduloFondo.change_model_fnd_tipo_descuento')
def editar_tipo_descuento(request, pk):
    tipo_descuento = get_object_or_404(Model_FND_tipo_descuento, pk=pk)
    form = frm_tipo_descuento(instance=tipo_descuento)
    pag_titulo = 'Editar tipo de descuento'
    if request.method == 'POST':
        form = frm_tipo_descuento(request.POST, instance=tipo_descuento)
        if form.is_valid():
            form.save()
            # Redirecciona a alguna página de éxito o muestra un mensaje de éxito
            return render(request, 'fondo/tipo_descuento/tipo_descuento_lista.html', {'form': form})
    else:
      
        return render(request, 'fondo/tipo_descuento/tipo_descuento_modificar.html', {'form': form, 'tipo_descuento': tipo_descuento, 'pk': pk,'title': pag_titulo})
    


# CREAR SOCIO
@permission_required('moduloFondo.add_model_fnd_socio')
def crear_socio(request):
    pag_titulo = 'Registrar socio'
    frm_crear = frm_socio
    if request.method == 'GET':
        return render(request, 'fondo/socio/socio_crear.html', {'title':pag_titulo,'frm':frm_crear})
    if request.method  == 'POST':
        frm_crear = frm_socio(request.POST)
        if frm_crear.is_valid():
            frm_crear.save()
            messages.success(request, 'Se ha generado corectamente el formulario')
            return redirect('core:home')
        else:
            messages.warning(request, 'Se ha generado un error desconocido')
            return render(request, 'fondo/socio/socio_crear.html', {'title':pag_titulo,'frm':frm_crear})
        
# LISTA DE SOCIOS      
@permission_required('moduloFondo.view_model_fnd_socio')
def listar_socio(request):
    pag_titulo = 'Lista de socios'
    socios = Model_FND_socio.objects.all()
    paginator = Paginator(socios, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'fondo/socio/socio_lista.html', {'title': pag_titulo, 'socios_list': page_obj})


# EDITAR SOCIO
@permission_required('moduloFondo.change_model_fnd_socio')
def editar_socio(request, pk):
    socio = get_object_or_404(Model_FND_socio, pk=pk)
    form = frm_socio(instance=socio)
    pag_titulo = 'Editar socio'
    if request.method == 'POST':
        form = frm_socio(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            # Redirecciona a alguna página de éxito o muestra un mensaje de éxito
            return render(request, 'fondo/socio/socio_lista.html', {'form': form})
    else:  
        return render(request, 'fondo/socio/socio_editar.html', {'form': form, 'socio': socio, 'pk': pk,'title': pag_titulo})
    

# PARAMETROS DEL SISTEMA

#SE SUPONE QUE LOS PARAMETROS SE CREAR UNA VEZ Y SOLO SE PODRAN MODIFICAR.

#VISULIZAR PARAMETROS DEL SISTEMA

@permission_required('moduloFondo.view_model_fnd_parametros_sys')
def ver_parametros(request):
    pag_titulo = 'Parametros del sistema'
    formulario = Frm_Fnd_Parametros_Sys
    return render(request, 'fondo/parametros/parametros_ver.html', {'title': pag_titulo, 'frm': formulario})

#EDITAR PARAMETROS DEL SISTEMA
@permission_required('moduloFondo.change_model_fnd_parametros_sys')
def editar_parametros(request, pk):
    parametro = get_object_or_404(Model_FND_Parametros_sys, pk=pk)
    form = Frm_Fnd_Parametros_Sys(instance=parametro)
    pag_titulo = 'Editar parametros del sistema'
    if request.method == 'POST':
        form = Frm_Fnd_Parametros_Sys(request.POST, instance=parametro)
        if form.is_valid():
            form.save()
            # Redirecciona a alguna página de éxito o muestra un mensaje de éxito
            return render(request, 'fondo/parametros/parametros_ver.html', {'form': form})
    else:  
        return render(request, 'fondo/parametros/parametros_editar.html', {'form': form, 'parametro': parametro, 'pk': pk,'title': pag_titulo})


# CREAR CARGO DE EMPLEADO
@permission_required('moduloFondo.add_model_fnd_empleado_cargo')
def crear_cargo_empleado(request):
    pag_titulo = 'Registrar cargo de empleado'
    frm_crear = frm_cargo_empleado
    if request.method == 'GET':
        return render(request, 'fondo/cargo_empleado/cargo_empleado_crear.html', {'title':pag_titulo,'frm':frm_crear})
    if request.method  == 'POST':
        frm_crear = frm_cargo_empleado(request.POST)
        if frm_crear.is_valid():
            frm_crear.save()
            messages.success(request, 'Se ha generado corectamente el formulario')
            return redirect('core:home')
        else:
            messages.warning(request, 'Se ha generado un error desconocido')
            return render(request, 'fondo/cargo_empleado/cargo_empleado_crear.html', {'title':pag_titulo,'frm':frm_crear})

# LISTA DE CARGOS DE EMPLEADO
@permission_required('moduloFondo.view_model_fnd_empleado_cargo')
def listar_cargo_empleado(request):
    pag_titulo = 'Lista de cargos de empleados'
    cargos_empleado = Model_FND_Empleado_Cargo.objects.all()
    paginator = Paginator(cargos_empleado, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'fondo/cargo_empleado/cargo_empleado_lista.html', {'title': pag_titulo, 'cargos_empleado_list': page_obj})

# EDITAR CARGO DE EMPLEADO
@permission_required('moduloFondo.change_model_fnd_empleado_cargo')
def editar_cargo_empleado(request, pk):
    cargo_empleado = get_object_or_404(Model_FND_Empleado_Cargo, pk=pk)
    form = frm_cargo_empleado(instance=cargo_empleado)
    pag_titulo = 'Editar cargo de empleado'
    if request.method == 'POST':
        form = frm_cargo_empleado(request.POST, instance=cargo_empleado)
        if form.is_valid():
            form.save()
            # Redirecciona a alguna página de éxito o muestra un mensaje de éxito
            return render(request, 'fondo/cargo_empleado/cargo_empleado_lista.html', {'form': form})
        else:
            return render(request, 'fondo/cargo_empleado/cargo_empleado_editar.html', 
                      {'form': form, 'cargo_empleado': cargo_empleado, 'pk': pk,'title': pag_titulo})
    else:  
        return render(request, 'fondo/cargo_empleado/cargo_empleado_editar.html', 
                      {'form': form, 'cargo_empleado': cargo_empleado, 'pk': pk,'title': pag_titulo})
    

# CREAR OPERADORA TELEFONICA
@permission_required('moduloFondo.add_model_fnd_operadora_telf')
def crear_operadora_telefonica(request):
    pag_titulo = 'Registrar operadora telefonica'
    frm_crear = frm_operadora
    if request.method == 'GET':
        return render(request, 'fondo/operadora/operadora_crear.html', {'title':pag_titulo,'frm':frm_crear})
    if request.method  == 'POST':
        frm_crear = frm_operadora(request.POST)
        if frm_crear.is_valid():
            frm_crear.save()
            messages.success(request, 'Se ha generado corectamente el formulario')
            return redirect('core:home')
        else:
            messages.warning(request, 'Se ha generado un error desconocido')
            return render(request, 'fondo/operadora/operadora_crear.html', {'title':pag_titulo,'frm':frm_crear})
        
# LISTA DE OPERADORAS TELEFONICAS
@permission_required('moduloFondo.view_model_fnd_operadora_telf')
def listar_operadora_telefonica(request):
    pag_titulo = 'Lista de operadoras telefonicas'
    operadoras = Model_FND_operadora_telf.objects.all()
    paginator = Paginator(operadoras, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'fondo/operadora/operadora_lista.html', {'title': pag_titulo, 'operadoras_list': page_obj})

# EDITAR OPERADORA TELEFONICA
@permission_required('moduloFondo.change_model_fnd_operadora_telf')
def editar_operadora_telefonica(request, pk):
    operadora = get_object_or_404(Model_FND_operadora_telf, pk=pk)
    form = frm_operadora(instance=operadora)
    pag_titulo = 'Editar operadora telefonica'
    if request.method == 'POST':
        form = frm_operadora(request.POST, instance=operadora)
        if form.is_valid():
            form.save()
            # Redirecciona a alguna página de éxito o muestra un mensaje de éxito
            return render(request, 'fondo/operadora/operadora_lista.html', {'form': form})
        else:
            return render(request, 'fondo/operadora/operadora_editar.html', 
                      {'form': form, 'operadora': operadora, 'pk': pk,'title': pag_titulo})
    else:  
        return render(request, 'fondo/operadora/operadora_editar.html', 
                      {'form': form, 'operadora': operadora, 'pk': pk,'title': pag_titulo})
    


#--------------------------------------------------- FND_PROVINCIA ---------------------------------------------------#

#LISTAR PROVINCIA
@permission_required('moduloFondo.add_model_fnd_provincia')
def listar_provincias(request):
    pag_titulo = 'Lista de provincias'
    provincias = Model_FND_provincia.objects.all()

    paginator = Paginator(provincias, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, urls_provincia['listar'], {'title': pag_titulo, 'pagina_paginator': page_obj})
#FIN LISTAR PROVINCIA

#AGREGAR PROVINCIA
def agregar_provincia(request):
    pag_titulo = 'Registrar provincia'
    frm_crear = Frm_Provincia

    if request.method == 'GET':
        return render(request, 'fondo/provincia/provincia_crear.html', {'title':pag_titulo,'frm':frm_crear})
    if request.method  == 'POST':
        frm_crear = Frm_Provincia(request.POST)
        if frm_crear.is_valid():
            frm_crear.save()
            messages.success(request, 'Se ha generado corectamente el formulario')
            return redirect('fondo:listar_provincias')
        else:
            messages.warning(request, 'Se ha generado un error desconocido')
            return render(request, 'fondo/provincia/provincia_crear.html', {'title':pag_titulo,'frm':frm_crear})
#FIN AGREGAR PROVINCIA

#EDITAR PROVINCIA
def editar_provincia(request, pk):
    provincia = get_object_or_404(Model_FND_provincia, pk=pk)
    form = Frm_Provincia(instance=provincia)
    pag_titulo = 'Editar provincia'
    if request.method == 'POST':
        form = Frm_Provincia(request.POST, instance=provincia)
        if form.is_valid():
            form.save()
            # Redirecciona a alguna página de éxito o muestra un mensaje de éxito
            return redirect(request, 'fondo/provincia/provincia_ver.html', {'form': form})
        else:
            return render(request, 'fondo/provincia/provincia_editar.html', 
                      {'form': form, 'pk': pk,'title': pag_titulo})
    else:  
        return render(request, 'fondo/provincia/provincia_editar.html', 
                      {'form': form, 'pk': pk,'title': pag_titulo})
#FIN EDITAR PROVINCIA
 
#AJAX PARA ACTUALIZAR LA BARRA DE BÚSQUEDA
def buscar_provincia(request):    
  
    search_term = ''
    if 'search_term' in request.POST:
        search_term = request.POST['search_term']

    provincias = Model_FND_provincia.objects.filter(Q(codigo__icontains=search_term) | Q(provincia__icontains=search_term)).order_by('codigo')

    paginator = Paginator(provincias, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'fondo/provincia/provincia_busqueda.html', {'pagina_paginator': page_obj})
#FIN AJAX PARA ACTUALIZAR LA BARRA DE BÚSQUEDA