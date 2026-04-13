#!/usr/bin/python
# *-------------------------------------------------------------------------*
# * factorial.py                                                            *
# * calcula el factorial de un número                                       *
# * Dr.P.E.Colla (c) 2022                                                   *
# * Creative commons                                                        *
# *-------------------------------------------------------------------------*

import sys

def factorial(num):
    if num < 0:
        print("Factorial de un número negativo no existe")
        return None
    elif num == 0:
        return 1
    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact

#procesa el rango ingresado manualmente.
def procesar_rango(rango_str):
    try:
        # Caso "-hasta"
        if rango_str.startswith("-"):
            hasta = int(rango_str[1:])
            return 1, hasta
        # Caso "desde-"
        elif rango_str.endswith("-"):
            desde = int(rango_str[:-1])
            return desde, 60
        # Caso "desde-hasta"
        else:
            desde, hasta = rango_str.split("-")
            return int(desde), int(hasta)
    except ValueError:
        print("Formato inválido. Use desde-hasta, -hasta o desde-")
        sys.exit()

#si no se ingresa el rango por línea de comandos, se solicita al usuario que lo ingrese manualmente.
if len(sys.argv) < 2:
    rango_str = input("Debe informar un rango (ej: 4-8, -10, 5-): ")
else:
    rango_str = sys.argv[1]

desde, hasta = procesar_rango(rango_str)

#calcula el factorial para cada número en el rango y lo imprime.
for num in range(desde, hasta + 1):
    print(f"Factorial {num}! es {factorial(num)}")