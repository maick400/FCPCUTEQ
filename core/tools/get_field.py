from django import forms
from django.db import connection


class Core_Tabla():
    def __init__(self, name ) -> None:
        self.nombre_tabla = name
        self.consulta = self.set_consulta()
        self.id_tabla = self.consulta[0][1]
        self.numero_tabla = self.consulta[0][3]
        self.cantidad_columnas = self.consulta[0][0]
        self.cantidad_registros = len(self.consulta)
        self.columnas = self.get_columnas()
        self.datos, self.filas_tabla = self.get_datos()  
        self.choices = self.get_choices()
        self.table_dict  = self.filas_diccionario()
        
    def set_consulta(self):
        with connection.cursor() as cursor:
            cursor.execute("select  * from obtener_tabla_con_parametro('" + str(self.nombre_tabla) + "')")
            rows = cursor.fetchall()
            
            if len(rows) == 0: 
                return None
            
            return list(rows )
    def get_datos(self):
        if len(self.consulta) == None:
            return None

        datos = []
        tabla = []
        campos = []
        flag = 1 
        for dato in range(self.cantidad_registros):
            datos.append({
                'id_valor':self.consulta[dato][7], 
                'valor':self.consulta[dato][8], 
                'activo':self.consulta[dato][9], 
                'linea':self.consulta[dato][10], 
                'id_campo_id':self.consulta[dato][11]})
  
#             if flag <= self.cantidad_columnas: 
#                 campos.append(str(self.consulta[dato][8]))
#                 campos.append(str(self.consulta[dato][7]))

#             if  flag == self.cantidad_columnas : 
#                 tabla.append(campos)
#                 campos = []
#                 flag = 0

                
#             flag = flag+1
            
            
#         return datos, tabla
            
    def filas_diccionario(self): 
        if len(self.consulta) == None:
            return None
        
        datos = []
        aux = {}
        for fila in self.filas_tabla:
            for index, dato in enumerate(fila):
                if index % 2 == 0: 
                    aux['valor'] =  dato
                else: 
                    aux['id'] =  dato
            datos.append(aux)
        return datos

                    
                
                
    def get_numero_registros(self):
        if len(self.consulta) == None:
            return None
        
        return self.consulta.count()
    
    def get_choices(self):
        if len(self.consulta) == None:
            return None
        
        tuple = ()
        display =  ''
        
        
        for fila  in self.filas_tabla:
            
            for i in range(0,self.cantidad_columnas):
                
                if i != self.cantidad_columnas - 1:
                    display = display+ fila[i*2 ] + '  -  '
                else: 
                    display = display+ fila[i*2]
            
            aux = (
                fila[0], #Valie del select
                  display,  #display del input
                )
            
            display =  ''

    
#             tuple = (*tuple, aux)
#         return   tuple
    
    def get_columnas(self):
        if len(self.consulta) == None:
            return None
        
   
        
        columnas = []
        for columna in range(self.cantidad_columnas):
            columnas.append({
                'id':self.consulta[columna][4], 
                'nombre_campo':self.consulta[columna][5],
                })
            
#         return columnas
#         return columnas
    
    



            

        
        
        
    
    
        
        
        
        
        

# def get_choices(cmd):
#     with connection.cursor() as cursor:
#             cursor.execute("select  * from obtener_tabla('Código de provincia ')")
#             rows = cursor.fetchall()
#             resgistros = rows.count()
#             numero_columnas = rows[0][2]
            
# #             iterables = int(resgistros/numero_columnas)
# #             tuple = ()
# #             values = []
            
# #             for i in range(iterables) :    
# #                 aux = (rows[i*numero_columnas-2][1],rows[i*numero_columnas-1][1])
# #                 tuple = (*tuple, aux)
# #             return  tuple
        
     