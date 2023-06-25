from django import forms
from django.db import connection

def get_values(cmd):
    with connection.cursor() as cursor:
            cursor.execute(cmd)
            rows = cursor.fetchall()
            tuple = ()
            values = []
            
            for row in rows:
                values.append({'label':row[1], #Etiqueta/título de la tabla
                                'valor': row[5], #Valores de la tabla (Lo que ve el usuario)
                                'tipo_dato': row[4], #Tipo de input para HTML 
                                'max_length': row[7], #Validación de longitud para el input
                                'cod_valor':row[8] #Código de valor (el que se registra en la base de datos)
                            }) 
                
                aux = (row[8], row[5])
                tuple = (*tuple, aux)
            
            choices_g = tuple
           
            return  forms.Select(attrs={'class': 'form-control', 'required':True}, choices=choices_g)
        

