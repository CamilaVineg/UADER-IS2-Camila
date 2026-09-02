

import os
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#*-------------------------------------------------------------------
class Memento:
	def __init__(self, file, content):
		
		self.file = file
		self.content = content


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


class FileWriterCaretaker:


	def save(self, writer):
		self.obj = writer.save()

	def undo(self, writer):
		writer.undo(self.obj)


if __name__ == '__main__':

	os.system("clear")
	print("Crea un objeto que gestionará la versión anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar");
	writer = FileWriterUtility("GFG.txt")

	print("Se graba algo en el objeto y se salva")
	writer.write("Clase de IS2 en UADER\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	#Se agrega contenido al objeto writer con la función write de la clase 
 	#FileWriterUtility y se guarda su estado actual, con la función save 
	#de la clase FileWriterCaretaker.
	print("Se graba algo en el objeto y se salva")
	writer.write("Clase de IS2 en UADER\n")
	print(writer.content + "\n\n")
	caretaker.save(writer) #lo hace el objeto caretaker porque es el 
 							#encargado de gestionar los estados anteriores del 
        					# objeto writer.


	#se repite el procedimiento de agregar contenido al objeto writer 
 	#en diferentes momentos para simular la realidad de versiones de un documento.
	#Se guarda siempre en caretaker para preservar el historial de versiones 
 	#del objeto writer.
  
	print("Se graba información adicional")
	writer.write("Material adicional de la clase de patrones\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)


	print("Se graba información adicional II")
	writer.write("Material adicional de la clase de patrones II\n")
	print(writer.content + "\n\n")

	#Por ultimo se invoca la funcion undo del objeto caretaker 
 	#para recuperar el estado inmediato anterior del objeto writer, 
  	#y se muestra el estado actual del mismo.
	
	
	print("se invoca al <undo>")
	caretaker.undo(writer)

	print("Se muestra el estado actual")
	print(writer.content + "\n\n")

	#Error: se invoca al undo para recuperar el estado 
	#anterior al inmediato despues de un undo realizado, pero no se 
	#muestra la version anterior, sino que muestra la misma versión que 
	#se muestra en el primer undo, porque el objeto caretaker solo guarda 
	#un estado anterior del objeto writer, y no tiene la capacidad de 
	#guardar hasta 4 estados anteriores como se pide en el ejercicio.
	#Solucion: modificar la clase FileWriterCaretaker para que tenga una 
	#lista de objetos Memento, y cada vez que se guarde un estado 
	#del objeto writer, se agregue a la lista, y cada vez que se 
	#invoque al undo, se recupere el estado anterior de la lista y 
	#se muestre el estado actual del objeto writer. De esta manera se podrá 
	#recuperar hasta 4 estados anteriores del objeto writer en cualquier 
	#orden de ser necesario.

	print("se invoca al <undo>")
	caretaker.undo(writer)

	print("Se muestra el estado actual")
	print(writer.content + "\n\n")

