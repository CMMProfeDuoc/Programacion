"""
Hasta ahora hemos visto como crear codigo
sin embargo, todo lo se ha creado en un solo "bloque" de codigo
¿Pero que pasa cuando encontramos algunas partes del codigo que
se repiten muchas veces?

Como ejemplo:
Si queremos imprimir una lista usamos un ciclo
"""
lista_frutas = ["manzana","sandia","pera","kiwi"]
lista_verduras = ["cebolla","papa","zanahoria"]
lista_legumbres = ["porotos","lentejas","habas","soya","porotos negros"]

for elemento in lista_frutas:
    print(elemento)

#Es facil cuando es una vez
#Pero si queremos volver a hacerlo?

for elemento in lista_frutas:
    print(elemento)

#Y si queremos imprimir otra lista?
for elemento in lista_legumbres:
    print(elemento)

#El codigo es muy similar, solo cambia la lista
#¿Y si quiero agregar un nombre antes de la lista?

print("Lista de Verduras")
for elemento in lista_verduras:
    print(elemento)

#Y hay que repetir esto para cada parte
print("Lista de Frutas")
for elemento in lista_frutas:
    print(elemento)

#Se vuelve tedioso, por eso existen Funciones
#En el archivo 5_2_escribir_func.py Veremos como se escriben
#Y como se usan las funciones