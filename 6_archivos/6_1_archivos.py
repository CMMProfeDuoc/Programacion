#Manejo de Archivo

archivo = open('texto.txt','a')

# Lectura 'r'
# archivo.read() <- entrega todo el archivo como texto
# archivo.readlines() <- entrega todo el archivo como un list[str] de cada linea
# archivo.readline() <- entrega una linea y salta a la siguiente

# Escritura 'w'
# en modo escritura, el archivo se borra al abrirse
# archivo.write(str) <- escribe el str en el texto
# \n <- salto de linea (""enter"")

# Añadir 'a' (append)
# modo añadir, agrega cosas AL FINAL del texto

archivo.write('hola\n')
archivo.write('que tal')

archivo.close()
