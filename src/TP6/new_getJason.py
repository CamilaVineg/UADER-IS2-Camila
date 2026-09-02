import json
import sys

# Archivo JSON (obligatorio)
# esta función toma el primer argumento de la línea de comandos como el nombre del archivo JSON a leer.
jsonfile = sys.argv[1]

# Clave JSON (opcional)
# esta línea verifica si se ha proporcionado un segundo argumento en la línea de comandos.
jsonkey = sys.argv[2] if len(sys.argv) > 2 else 'token1'
# Si es así, lo asigna a jsonkey; de lo contrario
# asigna el valor token1 por defecto.

# Esta línea abre el archivo JSON en modo de lectura ('r') y lo asigna a la variable myfile.
with open(jsonfile, 'r') as myfile:
    # El uso de with asegura que el archivo se cierre automáticamente después de su uso.
    data = myfile.read()

# Esta línea convierte la cadena JSON leída del archivo en un objeto de Python (generalmente un diccionario).
obj = json.loads(data)

# Verifica si la clave existe
if jsonkey in obj:
    # Si la clave jsonkey existe en el objeto obj, se imprime su valor convertido a cadena.
    print(str(obj[jsonkey]))
else:
    print(f'La clave "{jsonkey}" no existe en el archivo JSON.')
