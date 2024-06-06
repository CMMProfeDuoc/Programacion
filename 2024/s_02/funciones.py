def mostrarLista (lista:list) -> None:
    for i, elemento in enumerate(lista):
        print(i,'=>',elemento)

def mostrarAnimalLista (lista:list) -> None:
    for i, animal in enumerate(lista):
        print(i+1,'. ', animal['nombre'],' => ', animal['tipo'], sep='')

def selOpcion (lista:list,desfase:int=0) -> int:
    while (True):
        sel = input(">> ")
        if (sel.isnumeric()):
            sel = int(sel)-desfase
            if (sel in range(len(lista))):
                break
    return sel

def mostarMenu (opciones_menu : dict) -> str:
    for key in opciones_menu.keys():
        print(key,'=>',opciones_menu[key])
    selec = input('>> ').lower()
    return selec

def mostrarAndSelectAnimal (lista:list, desfase:int=0) -> dict:
    mostrarAnimalLista(lista)
    sel = selOpcion(lista,desfase)
    dict_sel = lista[sel]
    return dict_sel

def mostrarDetalle (diccionario:dict) -> None:
    for key in diccionario.keys():
        print(key,': ',diccionario[key],sep='')