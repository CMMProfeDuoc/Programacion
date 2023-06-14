import michiHerramientas as MH
listaTelefonos = MH.GetTelefonos()

#test de funcionamiento
print(listaTelefonos)

"""
Parte 1
Cree un sistema de agenda de telefono que sea capaz de filtrar por nombre o telefono.
Para esto, usted recibe una lista de nombres, los cuales tienen un numero de telefono asociado

El usuario ingresará un string para buscar un contacto. El programa debe encontrar todos los contactos
que tengan en alguna parte del nombre el string ingresado
El programa mostrara el nombre y el numero
"""


"""
Parte 2
El usuario tambien puede buscar por numero telefonico, esto ocurre si el usuario ingresa un numero (int)
El programa mostrara el nombre y el numero
"""


"""
Parte 3
El usuario tiene la opcion de agregar un mail a cada contacto, para esto, debe buscar un contacto
y el programa debe dar la opcion de agregar, reemplazar o quitar el mail asociado al contacto
"""

#-- NO MODIFICAR ----
import michiHerramientas as Michi
lista_telefonos = Michi.GetTelefonos()
#-----------------

print(lista_telefonos)