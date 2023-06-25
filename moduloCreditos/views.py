from django.shortcuts import render

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

from django.core.paginator import Paginator

# Create your views here.

def crear_tipo_bien (request):
    pag_titulo = "Tipo de bienes"
    form_tipo_bien = frm_tipo_bien

    if request.method == 'GET':
        return render(request, 'creditos/tipo_bien/crear.html', {'title':pag_titulo,'frm':form_tipo_bien})
    

def listar_tipo_bien (request):
    pag_titulo = "Tipo de bienes"
    form_tipo_bien = Model_CRE_tipo_bien.objects.all()
    paginator = Paginator(form_tipo_bien, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'creditos/tipo_bien/listar.html', {'title':pag_titulo,'frm':page_obj})


def crear_tipo_bien_atributo (request):
    pag_titulo = "Atributos de bien"
    form_atributos_bien = frm_tipo_bien_atributo

    if request.method == 'GET':
        return render(request, 'creditos/tipo_creditos_atributo/crear.html', {'title':pag_titulo,'frm':form_atributos_bien})


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

def crear_solicitud_bienes (request):
    pag_titulo = "Solicitud de crédito bienes"
    frmsolicitud_credito_bienes = frm_solicitud_bienes

    if request.method == 'GET':
        return render(request, 'creditos/solicitud_credito_bien/crear.html', {'title':pag_titulo,'frm':frmsolicitud_credito_bienes})


#Modificar el formulario -> el modelo tiene el atributo default y no permite establecer una opción en el select.
def crear_solicitud_documento_bien (request):
    pag_titulo = "Documentos para solicitud bien"
    frmsolicitud_documento_bienes = frm_solicitud_documentos_bien

    if request.method == 'GET':
        return render(request, 'creditos/solicitud_documentos_bienes/crear.html', {'title':pag_titulo,'frm':frmsolicitud_documento_bienes})



def crear_tabla_amortizacion (request):
    pag_titulo = "Tabla de amortización"
    formtabla_amortizacion = frm_credito_amortizacion

    if request.method == 'GET':
        return render(request, 'creditos/credito_amortizacion/crear.html', {'title':pag_titulo,'frm':formtabla_amortizacion})



def crear_tipo_credito (request):
    if  request.method == 'GET':
        return render (request,'creditos/tipo_credito/crear_tipo_credito.html')

