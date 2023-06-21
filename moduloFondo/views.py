from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from moduloFondo.forms.form_FND_tipo_descuento  import *
from moduloFondo.forms.form_FND_socios  import *
from moduloFondo.forms.form_FND_parametros_sys  import *
from moduloFondo.forms.form_FND_cargo_empleado  import *

from django.core.paginator import Paginator


#-------------------------- FND_TIPO_DESCUENTO -----------------------#
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
    all_parametros = Model_FND_Parametros_sys.objects.all()
    formulario = frm_parametros_sys()
    return render(request, 'fondo/parametros/parametros_ver.html', {'title': pag_titulo, 'all_parametros': formulario})

#EDITAR PARAMETROS DEL SISTEMA
@permission_required('moduloFondo.change_model_fnd_parametros_sys')
def editar_parametros(request, pk):
    parametro = get_object_or_404(Model_FND_Parametros_sys, pk=pk)
    form = frm_parametros_sys(instance=parametro)
    pag_titulo = 'Editar parametros del sistema'
    if request.method == 'POST':
        form = frm_parametros_sys(request.POST, instance=parametro)
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

