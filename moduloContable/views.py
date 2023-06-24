from django.shortcuts import render, redirect
from moduloContable.form.frmAnioFiscal import *
from moduloContable.form.frmPeriodoFiscal import *
from moduloContable.form.frmCuentaContable import *
from moduloContable.form.frmAsientoContable import *
from moduloContable.form.frmTipoTransaccionContable import *
<<<<<<< HEAD
from moduloContable.form.frmTipoTransaccionContable import *
=======
from moduloContable.form.frmTransaccionContable import *
from moduloContable.model.model_CNT_Tipo_Transaccion_Contable import *
from moduloContable.model.mode_SIS_Tipo_Documentos import *
from moduloContable.form.frmTipoDocumentos import *
>>>>>>> main

# Create your views here.

def cuentas_contable_inicio(request):
    pass

def anio_contable(request):
    pag_titulo="Año Fiscal"
    frmCrearAnio=Frm_Anio_Fiscal 

    if request.method == 'GET':
        return render(request, 'contable/cuentas_contables/cuentas_contable_crear.html', {'title':pag_titulo,'frm':frmCrearAnio})

    if request.method=="POST":
        print("metodo post :V")


def periodo_Fiscal(request):
    pag_titulo="Periodo Fiscal"
    frmPeridFiscal=Frm_Periodo_Fiscal

    if request.method == 'GET':
        return render(request, 'contable/cuentas_contables/periodo_fiscal_crear.html', {'title':pag_titulo,'frm':frmPeridFiscal})


def cuentas_contables(request):
    pag_titulo="Cuentas Contables"
    frmcuentaCont=frm_crear_cuenta_contable

    if request.method == 'GET':
        return render(request, 'contable/cuentas_contables/cuentas_contable_crear.html', {'title':pag_titulo,'frm':frmcuentaCont})



def asiento_contable(request):
    pag_titulo="Asiento Contable"
    frmAsientoContable=frmAsiento_Contable

    if request.method=="GET":
        return render(request,'contable/cuentas_contables/asiento_contable_crear.html', {'title':pag_titulo,'frm':frmAsientoContable})
    


def tipoTransaccion(request):
    pag_titulo="Asiento Contable"
    frmTipoTransaccion=Frm_tipo_Transaccion_Contable

    if request.method=="GET":
        return render(request,'contable/cuentas_contables/tipo_transaccion_contable_crear.html',
                       {'title':pag_titulo,'frm':frmTipoTransaccion})
    if request.method=="POST":
        dato=request.POST["tipo_transaccion"]
        modelotipo=Model_CNT_Tipo_Transaccion_Contable(tipo_transaccion=dato)
        modelotipo.save()
        return render(request,'contable/cuentas_contables/tipo_transaccion_contable_crear.html',
            {'title':pag_titulo,'frm':frmTipoTransaccion})
    

def transaccionContable(request):
    pag_titulo="Asiento Contable"
    frmTransaccionContable=Frm_tipo_Transaccion_Contable

    if request.method=="GET":
        return render(request,'contable/cuentas_contables/transaccion_contable.html',
                       {'title':pag_titulo,'frm':frmTransaccionContable})
<<<<<<< HEAD
        
        
=======
    

def tipoDocumento(request):
    pag_titulo="Asiento Contable"
    frmTipoDoc=frmTipoDocumentos
    if request.method=="GET":
        return render(request,'contable/cuentas_contables/tipo_documento/tipo_documento.html',
                       {'title':pag_titulo,'frm':frmTipoDoc})
>>>>>>> main
