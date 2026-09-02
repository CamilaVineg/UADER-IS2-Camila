# 5. Modifique el programa IS2_taller_memory.py para que la clase tenga la capacidad de
# almacenar hasta 4 estados en el pasado y pueda recuperar los mismos en cualquier orden de
# ser necesario. El método undo deberá tener un argumento adicional indicando si se desea recuperar
# el inmediato anterior (0) y los anteriores a el (1,2,3).

import os
# *--------------------------------------------------------------------
# * Design pattern memento, ejemplo
# *-------------------------------------------------------------------
# Clase Memento, que almacena el estado del objeto FileWriterUtility


class Memento:
    def __init__(self, file, content):

        self.file = file
        self.content = content

# Clase FileWriterUtility, que es el objeto cuyo estado se quiere preservar


class FileWriterUtility:

    def __init__(self, file):

        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content

# Clase FileWriterCaretaker, que es la encargada de
# gestionar los estados anteriores del objeto FileWriterUtility


class FileWriterCaretaker:

    def __init__(self):
        self.mementos = []

    def save(self, writer):
        # si la lista de mementos tiene 4 elementos, se elimina el primer elemento para agregar el nuevo estado.
        if len(self.mementos) == 4:
            self.mementos.pop(0)  # elimina el primer elemento de la lista
            # (el más antiguo), dejando espacio para el nuevo estado,
            # que se va a agregar al final de la lista.

        self.mementos.append(writer.save())

    def undo(self, writer, index=0):

        if not self.mementos:
            print("No hay estados anteriores disponibles para deshacer.")
            return

        # si la lista de mementos no está vacía y el índice es válido
        if 0 <= index < len(self.mementos):
            writer.undo(self.mementos[-1 - index])
            print(f"\n[OK]Se recuperó el estado {index} del historial.")
        else:
            print(
                f"\n[ERROR] El indice de undo {index} es inválido y se encuentra fueraa de rango. Actualmente hay {len(self.mementos)} estado(s) guardado(s).")

    def show_history(self):
        # muestra el historial de las versiones guardadas en el caretaker
        if not self.mementos:
            print("Historial vacío.")
            return
        else:
            print("--------Historial de versiones--------")
            # muestra el historial de versiones guardadas desde la más reciente hasta la más antigua.
            for i, memento in enumerate(reversed(self.mementos)):
                print(f"[{i}] Hace {i} versión(es) atrás")
                # Muestra los primeros 50 caracteres del contenido
                print(f"Contenido: {memento.content[:50]}...")

            print("------------------------------------")


# programa principal.
if __name__ == '__main__':
    os.system("cls")

    print("====================================================")
    print(" Taller de Patrón Memento - IS2")
    print("====================================================\n")

    print("Crea un objeto que gestionará la(s) versión(es) anterior(es)")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    while True:
        print("\n--- Estado Actual del Documento ---")
        print(f"Archivo: {writer.file}")
        print("Contenido:")
        if writer.content:
            print(f"\"\"\"\n{writer.content}\"\"\"")
        else:
            print("<Vacío>")
        print("----------------------------------")

        print("\n¿Qué desea hacer?")
        print("1. Escribir texto y Guardar versión (Save)")
        print("2. Ver historial de versiones guardadas")
        print("3. Deshacer / Recuperar una versión específica (Undo)")
        print("4. Salir")

        # la funcion strip() elimina los espacios en blanco al inicio y al final de la cadena ingresada por el usuario, para evitar errores de formato al procesar la opción seleccionada.
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == '1':
            texto = input("\nIngrese el texto a agregar: ")
            writer.write(texto + "\n")
            caretaker.save(writer)
            print("[OK] Texto agregado e historial guardado.")

        elif opcion == '2':
            caretaker.show_history()

        elif opcion == '3':
            if not caretaker.mementos:
                print(
                    "\n[ERROR] No hay versiones guardadas aún. Escriba algo primero.")
                continue

            caretaker.show_history()
            try:
                idx = int(input(
                    f"\nSeleccione cuál versión recuperar (0 a {len(caretaker.mementos) - 1}): ").strip())
                caretaker.undo(writer, idx)
            except ValueError:
                print("\n[ERROR] Por favor ingrese un número válido.")

        elif opcion == '4':
            print("\n¡Gracias por usar el gestor de mementos! Saliendo...")
            break
        else:
            print("\n[ERROR] Opción no válida. Intente de nuevo.")
