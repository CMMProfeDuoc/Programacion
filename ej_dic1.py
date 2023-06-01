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

#No modificar
import herramientasProfesor as Michi
#de aqui en adelante puede modificar -----------------

#ejemplo de diccionario
usuario = {
    "nombre":"Pepito",
    "edad":19
}

#imprimir un dato del diccionario
print(usuario["nombre"])

#cambiar un dato del diccionario
usuario["nombre"] = "Pepo"

#Imprima el nuevo valor <<<<


#agregar una llave y un nuevo valor al diccionario
usuario["altura"] = 1.67 #<- en este caso agregamos un float
#si colocamos una llave que no existe, python la creara y agregara ese valor!