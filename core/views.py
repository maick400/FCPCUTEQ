from django.shortcuts import render, redirect
# control de usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
def iniciar_sesion(request):
    page_title = 'Iniciar sesión'
    
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
