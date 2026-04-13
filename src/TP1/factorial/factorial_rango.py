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

#procesa el rango ingresado manualmente y lo convierte en valores enteros para el rango de números a calcular.
def procesar_rango(rango_str):
    try:
        desde, hasta = rango_str.split("-")
        desde, hasta = int(desde), int(hasta)
        return desde, hasta
    except ValueError:
        print("Formato inválido. Use desde-hasta (ej: 4-8).")
        sys.exit()


if len(sys.argv) < 2:
    rango_str = input("Debe informar un rango (ej: 4-8): ")
else:
    rango_str = sys.argv[1]

desde, hasta = procesar_rango(rango_str)

#calcula el factorial de los números comprendidos en el rango insertado.
for num in range(desde, hasta + 1):
    print(f"Factorial {num}! es {factorial(num)}")