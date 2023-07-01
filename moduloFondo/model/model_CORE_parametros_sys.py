from django.db import models
from core.model.choices.choices_FND_parametros_sys import * 


from moduloFondo.model.model_FND_tipo_fondo_complementario import Model_FND_tipo_fondo_complementario as TipoFondo
from moduloFondo.model.model_FND_provincia import Model_FND_provincia as Provincia
from moduloFondo.model.model_FND_Personal import Model_FND_Empleado_Cargo as Personal





class Model_FND_Parametros_sys(models.Model):
    id = models.TextField (primary_key=True, max_length=3, verbose_name='Código del fondo')
    codigo_tipo_fondo = models.ForeignKey(TipoFondo, on_delete= models.CASCADE, verbose_name='Codigo Fondo', db_column='id_tipo_fondo')
    nombre_fondo = models.TextField(max_length=500, null=False, blank=False, verbose_name="Nombre del Fondo")
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, verbose_name='Provincia', db_column='id_provincia')
    canton = models.TextField(max_length=2,null=False, blank=False)
    logo_fondo  = models.ImageField(upload_to='moduloFondo/img_general', verbose_name='Logo del Fondo')
    codigo_entidad  = models.TextField ( max_length=200 , null=False, blank= False,    verbose_name='Código de entidad (SB)')
    tipo_identificacion_fcpc = models.TextField(max_length=3, null=False, blank= False, choices=TIPO_IDENTIFICACION_FONDO, verbose_name='Tipo identificación del fondo')
    identificacion_fondo = models.TextField(max_length=13, null= False, blank=False, verbose_name='Número de identificación')
    numero_resolucion = models.TextField(max_length=15,  null= False, blank=False, verbose_name= 'Número de resolución' )    
    fecha_resolucion = models.DateField(null=False, blank=False, verbose_name='Fecha de resolución')
    dirección = models.TextField(max_length=30, null= False, blank=False, verbose_name= 'Direccion')
    correo_electronico = models.TextField(max_length=200, null=False , blank=False, verbose_name='Email')
    tipo_sistema = models.TextField(max_length=5, null=False, blank=False, verbose_name= "Tipo de sistema", choices=TIPO_SISTEMA)
    tipo_prestacion = models.TextField(max_length=5, null=False, blank=False,choices=TIPO_PRESTACION, verbose_name='Tipo de prestación')
    tipo_aporte  = models.TextField(max_length=5,  null=False, blank=False, choices=TIPO_DE_APORTE, verbose_name='Tipo de aporte')
    tipo_administracion = models.TextField(max_length=5, null=False, blank=False, choices= TIPO_DE_AMINISTRACION , verbose_name='Tipo de administración')
    fecha_traspaso = models.TextField(max_length=5, blank=True, null=True, choices= '', verbose_name='Fecha de traspaso')
    no_resolucion_cambio_estatuto = models.TextField(max_length=15, null=True, blank=True, verbose_name='N° de resolución cambio estatuto')
    porc_aporte_personal_cesantia  = models.DecimalField(max_digits=4,  default=0, decimal_places=2, null=False , blank=False, verbose_name='Procentaje de aporte personal por cesantía')
    porc_aporte_patronal_cesantia  = models.DecimalField(max_digits=4,  default=0, decimal_places=2, null=False , blank=False, verbose_name='Procentaje de aporte patronal por cesantía')
    porc_aporte_personal_jubilacion = models.DecimalField(max_digits=4, default=0,  decimal_places=2, null=False,  blank=False, verbose_name='Procentaje de aporte personal por jubilación')
    porc_aporte_patronal_jubilacion = models.DecimalField(max_digits=4, default=0,  decimal_places=2, null=False,  blank=False, verbose_name='Procentaje de aporte patronal por jubilación')
    valor_aporte_personal_cesantia = models.DecimalField (max_digits=4, default=0,  decimal_places=2, null=False,  blank=False, verbose_name='valor de aporte personal por jubilación')
    valor_aporte_personal_cesantia = models.DecimalField (max_digits=4, default=0,  decimal_places=2, null=False,  blank=False, verbose_name='valor de aporte personal por cesantía')
    pocentaje_seguro_degavamen  = models.DecimalField(max_digits=4, decimal_places=2, null= False , blank=False, verbose_name='Porcentaje seguro desgravamen')
    pocentaje_seguro_prima  = models.DecimalField(max_digits=4, decimal_places=2, null= False , blank=False, verbose_name='Porcentaje PRIMA seguro')
    pocentaje_seguro_cam  = models.DecimalField(max_digits=4, decimal_places=2, null= False , blank=False, verbose_name='Porcentaje CAM seguro')
    contador_perosnal_id = models.ForeignKey(Personal,null= False, on_delete=models.CASCADE, related_name='contador', db_column='contador_id_personal', verbose_name='contador')
    nombre_contador = models.TextField (max_length=200, null=False, blank=False, verbose_name='Nombre del contador' )
    matricula_contador = models.TextField (max_length= 20, null=False, blank=False, verbose_name='N° de Matricula del contador')
    representante_legal_id = models.ForeignKey(Personal, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Representante' ,related_name='reprensentante_legal' , db_column='representante_legal_id')
    nombre_representante_legal = models.TextField(max_length=200, null=False , blank= False, verbose_name='Nombre representante')
    identificacion_rep_legal = models.TextField(max_length= 13, null= False, blank=False, verbose_name='Identificación del representante')
    responsable_credito_id_personal = models.ForeignKey(Personal, on_delete= models.CASCADE, related_name='Representante_de_crédito', verbose_name='Responsable de cŕeditos', db_column='reprensentante_credito_id_personal')
    identificacion_res_credito = models.TextField(max_length=200, null=False, blank=False, verbose_name='Nombre representante de crédito')
    nombre_res_credito = models.TextField(max_length=200, null=False, blank=False, verbose_name='Nombre del responsable de crédito')
    fecha_const_fondo = models.DateField(null=False, blank=False, verbose_name='Fecha de constitición del fondo')
    smtp_server = models.TextField(max_length=500, null=True, blank=False, verbose_name='Servidor smtp')
    smtp_port = models.TextField(max_length=500, null=True, blank=False, verbose_name='Puerto smtp')
    smtp_cuenta = models.TextField(max_length=500, null=True, blank=False, verbose_name='Cuenta smtp')
    smtp_password = models.TextField(max_length=500, null=True, blank=False, verbose_name='Contraseña smtp')
    
    class Meta:
        app_label = "moduloFondo"
        managed = True
        db_table = 'core_parametros_del_sistema'
        verbose_name = 'Parámetro del sistema'
        verbose_name_plural = 'Parametros del sistema'
