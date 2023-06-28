from django import forms
from django.db import connection

from core.model.Model_CORE_campos import *
from core.model.Model_CORE_tabla import *
from core.model.Model_CORE_valores import *

class CORE_Tabla_estructura():
    cant_ignorar_columnas = 2
    id_tabla = 0
    nombre_tabla = 'Tabla'

    def __init__(self, n_tabla):
        self.n_tabla = n_tabla
        self.rows = self.get_tabla_structurada()

        self.rows_sin_estructura = self.get_table_sin_estructura(self.n_tabla, 1)
        print(self.rows_sin_estructura)

    def get_tabla_structurada(self):
        with connection.cursor() as cursor:
            cursor.execute("select  * from core_get_tabla_struct('" + self.n_tabla + "')")            
            rows = cursor.fetchall()
            
            #Si el resultado del llamado al método es 1(True), entonces se completó la consulta
            print("Resultado: ", rows[0][0])
            if(rows[0][0] == '1'):               
                cursor.execute("Select * from test_table")
                self.columnas = [desc[0] for desc in cursor.description]
                
                rows = cursor.fetchall()
                print("Filas: ", rows)
            else:
                rows = None            
            
            return rows
        
    def get_next_linea(self):
        next_linea = 0
        with connection.cursor() as cursor:
            cursor.execute("select max(linea) from core_valor_campo")
            rows = cursor.fetchall()

            if rows[0][0]:                
                next_linea = rows[0][0] + 1
            else:
                next_linea = 1

        return next_linea
    
    def get_table_sin_estructura(self, n_tabla, tipo):
        with connection.cursor() as cursor:

            if(tipo == 1):
                cursor.execute("Select * from core_get_tabla_wth_struct('{0}')".format(n_tabla))
            if(tipo == 2):
                cursor.execute("Select * from core_get_tabla_valores_wth_struct('{0}')".format(n_tabla))

            rows = cursor.fetchall()

            if(not rows):
                rows =  None    
            else:
                self.nombre_tabla = rows[0][1]
                    
            return rows