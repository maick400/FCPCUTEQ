from django.db import connection

def obtener_resultados_funcion(parametro1):
    with connection.cursor() as cursor:
        resultados = cursor.callfunc('obtener_datos_funcion', [parametro1])

    # Procesa los resultados según sea necesario    
    # for resultado in resultados:
    #     campo1 = resultado[0]
    #     campo2 = resultado[1]
    

    return resultados

result = obtener_resultados_funcion(1)
print(result)