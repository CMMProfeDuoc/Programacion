"""
Cree un sistema de Login
Para esto, usted recibe una lista de usuarios, los cuales tienen
<nombre_usuario> <contraseña>

Cree las siguientes funciones:

1. Buscar un usuario

2. Ingresar un usuario a la lista

3. Mostrar todos los usuarios
"""

#no cambiar estas lineas ------------------
import michiHerramientas as Michi
contactos = Michi.GetUserList()
#editar de aqui en adelante ---------------

def imprmirLista (lista:list, show_pass:bool=True) -> None:
    for l in lista:
        print(l["nombre"],end=" ")
        if (show_pass):
            print(l["contraseña"])
        else:
            con = "*" * len(l["contraseña"])
            print(con)

def addUser (lista:list,nombre:str,password:str="1234") -> None:
    if (not buscarUser(lista,nombre)):
        lista.append({"nombre":nombre,"contraseña":password})

def buscarUser (lista:list, user_name:str) -> bool:
    for l in lista:
        if (user_name == l["nombre"]):
            return True
    return False

addUser(contactos,"lalalala") 
imprmirLista(contactos,False)

#-------------
#MENU
#opciones = ["imprimir","añadir usuario","buscar usuario","salir"]
#while(True):
    #pass
    