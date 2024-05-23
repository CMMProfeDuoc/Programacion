"""
Los diccionarios son una estructura de datos que permite agrupar muchas variables y asociarlas a una llave.
La llave es un string y puede estar asociado a cualquier tipo de dato.

En este ejercicio, podra ver como se escribe un diccionario

nombre_diccionario = {
    "llave_1":dato_1,
    "llave_2:dato_2,
    .
    .
    .
    "llave_n":dato_n
}

y para acceder a un valor solo escribimos

nombre_diccionario["llave_n"] = dato_n
"""

#ejemplo de diccionario
usuario = {
    "nombre":"Pepito",
    "edad":19
}

#imprimir un dato del diccionario
print(usuario["nombre"])

#cambiar un dato del diccionario
usuario["nombre"] = "Pepo"

#agregar un dato a nueva llave
usuario["mail"] = "pepito@notmail.com"
#con agregar una nueva llave, se crea y se actualiza el diccionario
#si llave existe, se actualiza el dato

#sacar llave:valor del diccionario 
# var = dict.pop('key') <- se DEBE entregar la llave a sacar. De lo contrario hay error
# el 'pop' nos permite GUARDAR el dato de ser necesario o usarse para solo sacar el dato
user.pop("edad")

# ver las LLAVES -> dict.keys()
# ver los VALORES -> dict.values()

# Mostrar todos los items del diccionario
# for k in dict:
#     print (dict[k])
for k in user:
    print(k, user[k])
