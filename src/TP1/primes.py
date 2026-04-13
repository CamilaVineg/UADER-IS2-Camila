#!/usr/bin/python3
# programa para imprimir los números primos entre 1 y 500

lower = 1
upper = 500

print("Números primos entre", lower, "y", upper, "son:")

# iteración a través de cada número en el rango dado

for num in range(lower, upper + 1):

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
