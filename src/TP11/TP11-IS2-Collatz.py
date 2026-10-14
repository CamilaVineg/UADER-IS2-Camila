
"""Módulo para el cómputo y verificación de la Conjetura de Collatz."""

import sys

def collatz(num: int) -> int:
    """Calcula el número de iteraciones necesarias para alcanzar el valor 1."""
    iteraciones = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        iteraciones += 1
    return iteraciones

def main() -> None:
    """Punto de entrada: captura, valida y ejecuta el cálculo."""
    try:
        entrada = input("Ingrese un número entero positivo (1 a 1999): ").strip()
        num = int(entrada)
        if not (1 <= num <= 1999):
            print("Error: El número debe estar en el rango [1, 1999].")
            sys.exit(1)
        pasos = collatz(num)
        print(f"El número de iteraciones para {num} es {pasos}\n")
    except ValueError:
        print("Error: Debe ingresar un valor numérico entero válido.")
        sys.exit(1)


if __name__ == "__main__":
    main()