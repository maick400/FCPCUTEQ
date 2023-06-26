from django import forms
from django.db import connection

def get_choices(cmd):
    with connection.cursor() as cursor:
            cursor.execute(cmd)
            rows = cursor.fetchall()
            tuple = ()
            values = []
            
            for row in rows:
                values.append({ #Etiqueta/título de la tabla
                                'valor': row[6], #Valores de la tabla (Lo que ve el usuario)
                                'campo': row[4], #Tipo de input para HTML 
                            }) 
                
                aux = (row[6], row[4])
                tuple = (*tuple, aux)
   
            return  tuple
        
     