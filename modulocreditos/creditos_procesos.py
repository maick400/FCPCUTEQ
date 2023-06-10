from amortization.schedule import amortization_schedule
from tabulate import tabulate
from decimal import Decimal


class TablaAmortizacion: 
    def __init__(self, periodo,monto, cuotas,tasa_interes, seguro) -> None:
        self.monto = monto
        self.tasa_interes  = tasa_interes
        self.periodo = periodo
        self.cuotas = cuotas
        self.seguros = seguro
        self.tabla = self.francesa()
    def francesa(self) -> None:
            
        if self.periodo == 'MEN':
            tasa_interes = self.tasa_interes/12
        elif self.periodo == 'TRI':
            tasa_interes = self.tasa_interes/4
        elif self.periodo == 'SEM':
            tasa_interes = self.tasa_interes/2 
        #  ((1 - (1 + tasa_interes)**(-cuotas)))
        tb = []
        tb_amortizacion = list(x for x in amortization_schedule(15000, 0.12, 48))
        for index, cuota in enumerate(tb_amortizacion):
            tb.append( 
                self.Cuota(
                numero_cuota=cuota[0], 
                valor_neto=cuota[3],
                interes=cuota[2],
                seguro= cuota[4],
                restante=cuota[4]
                )
                )
        print(list(tb_amortizacion))

        return tb
    

        
    class Cuota():
        def __init__(self, numero_cuota, valor_neto, interes, seguro, restante ) -> None:  
            self.numero_cuota=numero_cuota
            self.valor_neto=valor_neto
            self.interes=interes
            self.seguro=seguro
            self.total = valor_neto + interes
            self.restan=restante

tb1 = TablaAmortizacion('MEN', 15000, 48, 0.12, 0.00104)

total_neto = 0
total_interes = 0

# for cuota in tb1.tabla:
#     print(cuota.numero_cuota,cuota.valor_neto, cuota.interes, cuota.total, cuota.restan)
# print((total_neto), (total_interes))

print(round(4.125121,2))