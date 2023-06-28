from django.db import connection
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from moduloCreditos.form.frm_tipo_bien import *
from moduloCreditos.form.frm_tipo_bien_atributo import *
from moduloCreditos.form.frm_tipo_bien_tipo_credito import *
from moduloCreditos.form.frm_tipo_credito_docs_requeridos import *
from moduloCreditos.form.frm_credito_bien_solicitud import *
 
from moduloCreditos.form.frm_tipo_bien_documentos import *
from moduloCreditos.form.frm_solicitud_credito import *
from moduloCreditos.form.frm_solicitud_bienes import *

from moduloCreditos.form.frm_solicitud_documentos_bien import *
from moduloCreditos.form.frm_credito_amortizacion import *

from moduloCreditos.form.frm_credito_bien import *

from moduloCreditos.form.frm_creditos_pagos import *
from moduloCreditos.form.frm_tipo_credito import *

from moduloCreditos.form.frm_credito_garante import *
from django.core.paginator import Paginator

# Create your views here.
@login_required


def crear_tipo_bien_atributo (request):
    pag_titulo = "Atributos de bien"
    form_atributos_bien = frm_tipo_bien_atributo

    if request.method == 'GET':
        return render(request, 'creditos/tipo_creditos_atributo/crear.html', {'title':pag_titulo,'frm':form_atributos_bien})

def listar_tipo_bien_atributo (request):
    pag_titulo = "Lista de atributos de bien"
    form_atributos_bien = Model_CRE_tipo_bien_atributo.objects.all()
    paginator = Paginator(form_atributos_bien, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'creditos/tipo_creditos_atributo/listar.html', {'title':pag_titulo,'frm':page_obj})

def crear_tipo_bien_tipo_credito (request):
    pag_titulo = "Tipo bien por tipo de crédito"
    formtipo_bien_tipo_atributo = frm_tipo_bien_tipo_credito

    if request.method == 'GET':
        return render(request, 'creditos/tipo_bien_tipo_credito/crear.html', {'title':pag_titulo,'frm':formtipo_bien_tipo_atributo})
 

def crear_doc_requerido_credito (request):
    pag_titulo = "Documentos requeridos para crédito"
    form_docs_requeridos = frm_tipo_credito_docs_requeridos

    if request.method == 'GET':
        return render(request, 'creditos/tipo_creditos_docs_requeridos/crear.html', {'title':pag_titulo,'frm':form_docs_requeridos})

#Arrreglar
def crear_credito_bien_solicitud (request):
    pag_titulo = "Documentos requeridos para crédito"
    form_docs_requeridos = frm_credito_bien_solicitud

    if request.method == 'GET':
        return render(request, 'creditos/solicitud_credito_bien/crear.html', {'title':pag_titulo,'frm':form_docs_requeridos})

def crear_tipo_bien_documento (request):
    pag_titulo = "Documentos requeridos para bienes"
    frm_docs_bien_requerido = frm_tipo_bien_documento

    if request.method == 'GET':
        return render(request, 'creditos/tipo_bien_documentos/crear.html', {'title':pag_titulo,'frm':frm_docs_bien_requerido})

def crear_solicitud_credito (request):
    pag_titulo = "Solicitud de crédito"
    frmsolicitud_credito = frm_solicitud_credito

    if request.method == 'GET':
        return render(request, 'creditos/solicitud_credito/crear.html', {'title':pag_titulo,'frm':frmsolicitud_credito})

def listar_solicitud_credito (request):
    pag_titulo = "Lista de solicitudes de crédito"
    frmsolicitud_credito = Model_CRE_solicitud_credito.objects.all()
    paginator = Paginator(frmsolicitud_credito, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'creditos/solicitud_credito/listar.html', {'title':pag_titulo,'frm':page_obj})

def crear_solicitud_bienes (request):
    pag_titulo = "Solicitud de crédito bienes"
    frmsolicitud_credito_bienes = frm_solicitud_bienes

    if request.method == 'GET':
        return render(request, 'creditos/solicitud_credito_bien/crear.html', {'title':pag_titulo,'frm':frmsolicitud_credito_bienes})


#Modificar el formulario -> el modelo tiene el atributo default y no permite establecer una opción en el select.
def crear_solicitud_documento_bien(request):
    pag_titulo = "Documentos para solicitud bien"
    frmsolicitud_documento_bienes = frm_solicitud_documentos_bien

    if request.method == 'GET':
        return render(request, 'creditos/solicitud_documentos_bienes/crear.html', {'title':pag_titulo,'frm':frmsolicitud_documento_bienes})



def crear_tabla_amortizacion(request):
    pag_titulo = "Tabla de amortización"
    formtabla_amortizacion = frm_credito_amortizacion

    if request.method == 'GET':
        return render(request, 'creditos/credito_amortizacion/crear.html', {'title':pag_titulo,'frm':formtabla_amortizacion})

def listar_tabla_amortizacion(request):
    pag_titulo = "Tabla de amortización"
    formtabla_amortizacion = Model_CRE_credito_amortizacion.objects.all()
    paginator = Paginator(formtabla_amortizacion, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'creditos/credito_amortizacion/listar.html', {'title':pag_titulo,'frm':page_obj})


def crear_pago_credito(request):
    pag_titulo = "Registro de pago de crédito"
    form_pagos_credito = frm_creditos_pagos

    if request.method == 'GET':
        return render(request, 'creditos/credito_amortizacion/crear.html', {'title':pag_titulo,'frm':form_pagos_credito})

def listar_pago_credito(request):
    pag_titulo = "Lista de pago de crédito"
    form_pagos_credito = Model_CRE_credito_pagos.objects.all()
    paginator = Paginator(form_pagos_credito, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'creditos/credito_pagos/listar.html', {'title':pag_titulo,'frm':page_obj})


def crear_credito_bien(request):
    pag_titulo = "Registro de bien para crédito"
    form_creditobien = frm_credito_bien

    if request.method == 'GET':
        return render(request, 'creditos/credito_bien/crear.html', {'title':pag_titulo,'frm':form_creditobien})

def listar_credito_bien(request):
    pag_titulo = "Lista de bienes para crédito"
    form_creditobien = Model_CRE_credito_bien.objects.all()
    paginator = Paginator(form_creditobien, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'creditos/credito_bien/listar.html', {'title':pag_titulo,'frm':page_obj})

def listar_credito_bien(request):
    pag_titulo = "Lista de solicitudes de credito bien"
    form_creditobien = Model_CRE_credito_bien.objects.all()
    paginator = Paginator(form_creditobien, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'creditos/credito_bien/listar.html', {'title':pag_titulo,'frm':page_obj})

def crear_credito_garante(request):
    pag_titulo = "Registro de garante para crédito"
    form_garante = frm_credito_garante

    
    if request.method == 'GET':
        return render(request, 'creditos/credito_garante/crear.html', {'title':pag_titulo,'frm':form_garante})

def listar_credito_garante(request):
    pag_titulo = "Lista de garantes para crédito"
    form_garante = Model_CRE_credito_garante.objects.all()
    paginator = Paginator(form_garante, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'creditos/credito_garante/listar.html', {'title':pag_titulo,'frm':page_obj})


# ------------------- MAESTRA TIPO CREDITO ------------------- #
@permission_required('moduloCreditos.add_model_cre_tipo_credito')
def crear_tipo_credito (request):
    pag_titulo = 'Registrar un tipo de credito'
    frm_crear = frm_tipo_credito
    if request.method == 'GET':
        return render(request, 'creditos/tipo_credito/crear_tipo_credito.html', {'title':pag_titulo,'frm':frm_crear})
    if request.method  == 'POST':
        frm_crear = frm_tipo_credito(request.POST)
        if frm_crear.is_valid():
            frm_crear.save()
            messages.success(request, 'Se ha generado corectamente el formulario')
            return redirect('core:home')
        else:
            messages.warning(request, 'Se ha generado un error desconocido')
            return render(request, 'creditos/tipo_credito/crear_tipo_credito.html', {'title':pag_titulo,'frm':frm_crear})


def listar_tipo_credito (request):
    pag_titulo = "Lista de tipos de crédito"
    form_tipo_credito = Model_CRE_tipo_credito.objects.all()
    paginator = Paginator(form_tipo_credito, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'creditos/tipo_credito/listar_tipo_credito.html', {'title':pag_titulo,'frm':page_obj})

# ------------------- MAESTRA TIPO BIEN ------------------- #

def crear_tipo_bien (request):
    pag_titulo = 'Registrar un tipo de bien'
    frm_crear = frm_tipo_bien
    if request.method == 'GET':
        return render(request, 'creditos/tipo_bien/crear.html', {'title':pag_titulo,'frm':frm_crear})
    if request.method  == 'POST':
        frm_crear = frm_tipo_bien(request.POST)
        if frm_crear.is_valid():
            frm_crear.save()
            messages.success(request, 'Se ha generado corectamente el formulario')
            return redirect('core:home')
        else:
            messages.warning(request, 'Se ha generado un error desconocido')
            return render(request, 'creditos/tipo_bien/crear.html', {'title':pag_titulo,'frm':frm_crear})

def listar_tipo_bien (request):
    pag_titulo = "Lista de tipo de bienes"
    form_tipo_bien = Model_CRE_tipo_bien.objects.all()
    paginator = Paginator(form_tipo_bien, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'creditos/tipo_bien/listar.html', {'title':pag_titulo,'frm':page_obj})






def obtener_resultados_funcion():

    values = []

    with connection.cursor() as cursor:
        cursor.execute('Select * from obtener_datos_funcion(1)')
        rows = cursor.fetchall()
         
        for row in rows:
            values.append({'label':row[1], #Etiqueta/título de la tabla
                            'valor': row[5], #Valores de la tabla
                            'tipo_dato': row[4], #Tipo de input para HTML
                            'max_length': row[7], #Validación de longitud para el input
                            'cod_valor':row[8]
                          }) 
        print(values)

    return values


