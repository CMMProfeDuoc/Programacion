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

def imprimirLista (lista:list) -> None:
	for element in lista:
		for k in element:
			print(element[k]," ",end="")
		print("")

def buscarContactoNombre (lista:list, nombre:str) -> dict:
	for cont in lista:
		if (cont["nombre"] == nombre):
			return cont
	return None

def buscarContactoNumero (lista:list, numero:int) -> dict:
	for cont in lista:
		if (cont["numero"] == numero):
			return cont
	return None

def buscarContacto (lista:list, busqueda) -> dict:
	if (busqueda.isnumeric()):
		return buscarContactoNumero(lista,int(busqueda))
	return buscarContactoNombre (lista,busqueda)

def buscarNombreNotComplete (lista:list, string:str) -> list:
	contactos = []
	for cont in lista:
		if (string in cont["nombre"]):
			contactos.append[cont]
	return contactos
# ----------------
