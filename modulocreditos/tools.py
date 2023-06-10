from decimal import Decimal, ROUND_HALF_UP , ROUND_UP
import decimal 

decimal.getcontext().rounding = ROUND_HALF_UP
decimal.getcontext().prec = 30

def diner( value):
    return(Decimal(str(value)))