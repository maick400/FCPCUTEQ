from django.shortcuts import render

# Create your views here.
def crear_tipo_credito (request):
    if  request.method == 'GET':
        return render (request,'creditos/tipo_credito/crear_tipo_credito.html')
