from django.shortcuts import render, redirect
# control de usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from core.tools.get_field import Core_Tabla
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

def get_table(request):
    tabla = Core_Tabla(183)
    print(tabla.datos)
    return render(request, 'core/tablas_parametros/get_tabla.html', {'tabla':tabla})

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



