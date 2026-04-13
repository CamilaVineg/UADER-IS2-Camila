import sys

class Factorial:
    def __init__(self):
        # Constructor: no necesita parámetros, pero mantiene la estructura OOP
        pass

    def calcular(self, num):
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

    def run(self, min_val, max_val):
        for num in range(min_val, max_val + 1):
            print(f"Factorial {num}! es {self.calcular(num)}")


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


if __name__ == "__main__":
    # Si no hay argumento, pedirlo con input
    if len(sys.argv) < 2:
        rango_str = input("Debe informar un rango (ej: 4-8, -10, 5-): ")
    else:
        rango_str = sys.argv[1]

    desde, hasta = procesar_rango(rango_str)

    # Crear objeto y ejecutar
    f = Factorial()
    f.run(desde, hasta)