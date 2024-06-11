def filtrar (lista_objetivo:list[dict],llave:str,filtro:str) -> list:
    lista_filtrada = []
    for elemento in lista_objetivo:
        if (str(elemento[llave]) in str(filtro)):
            lista_filtrada.append(elemento)
    return lista_filtrada

def filtrarTodo (lista_objetivo:list[dict], filtro:str) -> list:
    lista_filtrada = []
    lista_final = []
    for elemento in lista_objetivo:
        for key in elemento.keys():
            lista_filtrada += filtrar(lista_objetivo,key,filtro)

    #quitar repetidos
    for elemento in lista_filtrada:
        if (elemento not in lista_final):
            lista_final.append(elemento)

    return lista_final

def seleccionMenu (menu:dict) -> str:
    for opcion in menu.keys():
        print(opcion, '=>', menu[opcion])

    opc_sel = input('ingrese comando: ')

    #verificar que la opcion sea valida
    
    return opc_sel


def mostrarListaAnimales (lista_animales:list[dict],nombre_lista:str) -> None:
    print('--',nombre_lista,'--')
    for i, animal in enumerate(lista_animales):
        print(i, animal['nombre'])
    print('-'*10)