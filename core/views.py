from django.shortcuts import render, redirect
# control de usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



# Create your views here.


def signin(request):
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
            return redirect('home')

    # render for get
    return render(request,"core/signin.html",{'title':page_title})

def logout(request):
    logout(request)
    return redirect('core:signin')
    
    
    
@login_required
def home(request):
    page_title = 'Inicio'
    return render(request,"core/home.html",{'title':page_title})
