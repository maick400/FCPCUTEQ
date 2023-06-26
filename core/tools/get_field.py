from django import forms
from django.db import connection


numero_columnas = 2

def get_choices(cmd):
    with connection.cursor() as cursor:
            cursor.execute(cmd)
            rows = cursor.fetchall()
            resgistros = rows.count()
            
            iterables = int(resgistros/numero_columnas)
            tuple = ()
            values = []
            for i in range(iterables) :    
                aux = (rows[i*numero_columnas-2][6],rows[i*numero_columnas-1][6])
                tuple = (*tuple, aux)

                    
   
            return  tuple
        
     