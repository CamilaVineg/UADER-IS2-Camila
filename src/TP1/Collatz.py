# Generating Collatz convergence plot for numbers 1 to 10000
import matplotlib.pyplot as plt

def collatz_iterations(n):
    """Devuelve la cantidad de pasos que tarda n en llegar a 1."""
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

# Calcular para números entre 1 y 10000
nums = list(range(1, 10001))
iters = [collatz_iterations(n) for n in nums]

# Crear gráfico
plt.figure(figsize=(10,6))
plt.scatter(iters, nums, s=2, color="blue")
plt.title("Conjetura de Collatz (1 a 10000)")
plt.xlabel("Iteraciones hasta converger")
plt.ylabel("Número inicial n")

# Guardar en la misma carpeta del script
plt.savefig("collatz_convergencia.png", dpi=300)

# Mostrar en pantalla
plt.show()
