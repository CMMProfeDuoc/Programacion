#-- NO MODIFICAR ----
import michiHerramientas as Michi
lista_telefonos = Michi.GetTelefonos()
#-----------------

def imprimirDiccionario (elemento:dict) -> None:
    for k in elemento.keys():
        print(elemento[k],end=" | ")

def imprimirListaDiccionario (lista:list) -> None:
    for i,elemento in enumerate(lista):
        print(i+1,end=". ")
        imprimirDiccionario(elemento)
        print()

def imprimirListaNormal (lista:list) -> None:
    for i, elemento in enumerate(lista):
        print(i+1,elemento)

def filtrar (lista:list, filtro, llave:str = "nombre") -> list:
    lista_filtrada = []
    for elemento in lista:
        if (str(filtro).lower() in str(elemento[llave]).lower()):
            lista_filtrada.append(elemento)
    return lista_filtrada

def seleccionarDiccionario (lista:list) -> dict:
    imprimirListaDiccionario(lista)
    sel = int(input(">> "))-1
        #HACER FUNCION QUE VALIDE SEL
    return lista[sel]

def agregar_llave (elemento:dict,valor,llave:str) -> dict:
    elemento[llave] = valor
    return elemento

def mod_llave (elemento:dict,valor,llave:str) -> dict:
    elemento[llave] = valor
    return elemento

def buscar (lista:list, filtro) -> list:
    lista_busqueda = []
    for elemento in lista:
        for k in elemento.keys():
            lista_busqueda += filtrar(lista,filtro,k)
    return lista_busqueda

def buscarSensatamente (lista:list, filtro) -> list:
    lista_busqueda = filtrar(lista,filtro,"nombre")
    lista_busqueda += filtrar(lista,filtro,"telefono")
    return lista_busqueda

#----------------
#MENU
#-------------

menu = [
    "Mostrar Contactos",
    "Buscar por Nombre",
    "Buscar por Numero",
]
menu.append("Salir")

while (True):
    imprimirListaNormal(menu)
    sel = int(input(">> "))-1
    #print("DEBUG:",sel)
    print(menu[sel])

    if (sel == len(menu)-1):
        break

    if (sel == 0): #Mostrar Contactos
        imprimirListaDiccionario(lista_telefonos)

    if (sel == 1): #buscar por nombre
        lista_filt = filtrar(lista_telefonos,input("Ingrese nombre a buscar: "),"nombre")
        imprimirListaDiccionario(lista_filt)

    if (sel == 2): #buscar por numero
        lista_filt = filtrar(lista_telefonos,input("Ingrese numero a buscar: "),"telefono")
        imprimirListaDiccionario(lista_filt)



