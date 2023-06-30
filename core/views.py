from django.shortcuts import render, redirect
# control de usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from core.tools.get_field import Core_Tabla

#--------------------------MÓDELOS DE TABLAS DINÁMICAS-----------------------------------
from core.tools.tablas_struct.CORE_Tabla_estructura import *

from core.model.Model_CORE_tabla import *
from core.forms.Form_CORE_tabla import *

from core.model.Model_CORE_campos import *
from core.forms.Form_CORE_campos import *

from core.model.Model_CORE_valores import *
from core.forms.Form_CORE_valores import *


# Create your views here.
def iniciar_sesion(request):
    page_title = 'Iniciar sesión'
    



    # print(tabla_provincias.datos)
    


    
    # print(tabla_provincias.print_consulta())

    
    if request.method == 'POST':
        # Vemos si el usuario existe 
        user =  authenticate(request, username=request.POST['user'], password=request.POST['pass'])
        if user is  None:
            # si no existe retornamos con un error o mensaje 
            return render(request,'core/signin.html',{'title':page_title,'error': 'Credenciales incorrectas'})
        else:
            # si existe lo logeamos 
            login(request, user) 
            return redirect('core:home')

    # verifica si el usuario esta iniciado sesión, en caso de estarlo, lo redirige al "home", caso contrario, renderiza "Iniciar sesion"
    if not request.user.is_authenticated:
        return render(request, 'core/signin.html', {'title':page_title})
    else:
        return redirect('core:home')
    
    
def cerrar_sesion(request):
    # funcion interna de django que cierra sesion 
    logout(request)
    return redirect('core:signin')

@login_required
def inicio(request):
    page_title = 'Inicio'
    return render(request,"core/home.html",{'title':page_title})

# def get_table(request):
#     tabla = Core_Tabla('Tipo de fondo complementario (FCPC)')
#     print(tabla.filas_tabla)
#     return render(request, 'core/tablas_parametros/get_tabla.html', {'tabla':tabla})


#------------------------------------------------TABLAS DINÁMICAS DEL SISTEMA ------------------------------------------------#

#MOSTRAR LA LISTA DE TABLAS CREADAS
def listar_tablas(request):
    page_title = 'Tablas del sistema'
    tablas = Model_CORE_tabla.objects.all()
    
    
    frm_crear = Form_CORE_tabla

    if request.method == 'GET':
        return render(request,"core/tablas_parametros/tablas_listar.html",{'title':page_title, 'tablas': tablas, 'frm': frm_crear})
    if request.method == 'POST':
        frm_crear = Form_CORE_tabla(request.POST)
        if(frm_crear.is_valid()):
            frm_crear.save()
            return render(request,"core/tablas_parametros/tablas_listar.html",{'title':page_title, 'tablas': tablas, 'frm': frm_crear})
        else:
            return render(request,"core/tablas_parametros/tablas_listar.html",{'title':page_title, 'tablas': tablas, 'frm': frm_crear})


#FUNCIÓN PARA VISUALIZAR LOS CAMPOS QUE TIENE UNA TABLA Y AGREGAR NUEVOS
def ver_detalle_tabla(request, pk):
    page_title = 'Tablas del sistema'
    tabla = Model_CORE_tabla.objects.get(id_tabla = pk)
    campos = Model_CORE_campos.objects.filter(id_tabla_id = pk)
    
    if(request.method == 'GET'):    
        return render(request,"core/tablas_parametros/tabla_detalle.html",{'title':page_title, 'tabla': tabla, 'campos': campos})
    if request.method  == 'POST':
        campos = request.POST.getlist("nombre_campo")
        
        for i in range(len(campos)):
            campo_crear  = Model_CORE_campos.objects.create(nombre_campo = campos[i], id_tabla_id = request.POST.get("id_tabla"))
   
        tabla = Model_CORE_tabla.objects.get(id_tabla = pk)
        campos = Model_CORE_campos.objects.filter(id_tabla_id = pk)
        return render(request,"core/tablas_parametros/tabla_detalle.html",{'title':page_title, 'tabla': tabla, 'campos': campos})    

def ver_detalle_campo_tabla(request, pk):
    page_title = 'Tablas del sistema'
    campos = Model_CORE_campos.objects.filter(id_campo = pk)
    valores = Model_CORE_valores.objects.filter(id_campo_id = pk)
    
    if(request.method == 'GET'):    
        return render(request,"core/tablas_parametros/campo_tabla_detalle.html",{'title':page_title, 'campos': campos, 'valores': valores})
        
  

def editar_tabla(request, pk):
    page_title = 'Tablas del sistema'
    tablas = Model_CORE_tabla.objects.all()

    return render(request,"core/tablas_parametros/tablas_listar.html",{'title':page_title, 'tablas': tablas})


#-----------------------CREAR DATOS PARA LAS TABLAS DINÁMICAS-----------------------#
def crear_tabla(request):
    page_title = 'Tablas'
    frm_crear = Form_CORE_tabla

    if request.method == 'GET':
        return render(request, 'core/tablas_parametros/tabla_crear.html', {'title':page_title,'frm':frm_crear})
    if request.method  == 'POST':
        frm_crear = Form_CORE_tabla(request.POST)
        if frm_crear.is_valid():
            frm_crear.save()
            return redirect('core:home')
        else:
            return render(request, 'core/tablas_parametros/tabla_crear.html', {'title':page_title,'frm':frm_crear})
        
def crear_campo_tabla(request):
    page_title = 'Tablas'
    frm_crear = Form_CORE_campos

    if request.method == 'GET':
        return render(request, 'core/tablas_parametros/campo_tabla_crear.html', {'title':page_title,'frm':frm_crear})
    if request.method  == 'POST':
        frm_crear = Form_CORE_campos(request.POST)
        if frm_crear.is_valid():
            campo_crear = frm_crear.save(commit=False)            
            campo_crear.save()
            return redirect('core:home')
        else:
            return render(request, 'core/tablas_parametros/campo_tabla_crear.html', {'title':page_title,'frm':frm_crear})
        

def crear_valores_campo(request):
    page_title = 'Valores de campo'
    frm_crear = Form_CORE_valores

    if request.method == 'GET':
        return render(request, 'core/tablas_parametros/valores_campo_crear.html', {'title':page_title,'frm':frm_crear})
    if request.method  == 'POST':
        frm_crear = Form_CORE_valores(request.POST)
        if frm_crear.is_valid():
            frm_crear.save()
            return redirect('core:home')
        else:
            return render(request, 'core/tablas_parametros/valores_campo_crear.html', {'title':page_title,'frm':frm_crear})


def tabla_estructura(request, pk):
    page_title = 'Valores de campo'
    tabla = CORE_Tabla_estructura(pk)

    if request.method == 'GET':
        return render(request, 'core/tablas_parametros/campo_tabla_estructura.html', {'title':page_title,'tabla': tabla, 'pk': pk})
    if request.method == 'PUT':      
        return render(request, 'core/tablas_parametros/campo_tabla_estructura.html', {'title':page_title,'tabla': tabla})
        
    if request.method == 'POST':

        ids_campo = request.POST.getlist("id_campo_id")
        valor = request.POST.getlist("valor")

        estructura_tablas = CORE_Tabla_estructura(pk)

        # print(ids_campo)
        # print(valor)
        next_linea = estructura_tablas.get_next_linea()
        for i in range(len(ids_campo)):
            object_valor = Model_CORE_valores.objects.create(valor=valor[i], activo='True', linea=next_linea, id_campo_id=ids_campo[i])
        return redirect('core:tabla_estructura', pk= pk)
        # return render(request, 'core/tablas_parametros/campo_tabla_estructura.html', {'title':page_title,'tabla': tabla, 'pk': pk})
    
        
def update_estructura_tabla(request, pk):    
    # model_valor = Model_CORE_tabla.objects.get(id_tabla = 1)
    # frm_tabla_estructura = Form_CORE_tabla(instance=model_valor)

    model_valor = Model_CORE_valores.objects.get(id_campo_id = 1)
    frm_tabla_estructura = Form_CORE_tabla(instance=model_valor)

    registro_editar = CORE_Tabla_estructura(pk)
    rows = registro_editar.get_table_sin_estructura(pk, 2)

    print("A EDITAR", rows)
   
   
    return render(request, 'core/modals/modal_update_tabla_estructura.html', {'frm':frm_tabla_estructura, 'registro_editar': registro_editar} )
    
def modulo_contable (request):
    page_title = 'Módulo contable'
    return render(request, 'core/modulos/contable/modulo_contable.html' , {'title':page_title})

def modulo_fondo (request):
    page_title = 'Módulo contable'
    return render(request, 'core/modulos/fondo/modulo_fondo.html' , {'title':page_title})

def modulo_sistema (request):
    # tablas_guia =  
    page_title = 'Módulo contable'
    return render(request, 'core/modulos/sistema/modulo_sistema.html' , {'title':page_title})



