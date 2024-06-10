def pausa () -> None:
    input('presione enter para continuar...')

def detalleAnimal (animal:dict) -> None:
    for k in animal.keys():
        print(k,'=>',animal[k])

def imprimirListaAnimales (lista_animales:list[dict], nombre_lista:str = 'Lista Animales') -> None:
    print('--',nombre_lista,'--')
    for i, animal in enumerate(lista_animales):
        print(i+1,animal['nombre'])
    print('-'*10)

def filtrar (lista:list[dict], filtro:str, llave:str='nombre') -> list:
    lista_filtrada = []
    for elemento in lista:
        if (str(elemento[llave]) in str(filtro)):
            lista_filtrada.append(elemento)
    return lista_filtrada

def filtrarTodo (lista:list[dict], filtro:str) -> list:
    lista_filtrada = []
    lista_aux = []
    for elemento in lista:
        for llave in elemento.keys():
            lista_aux += filtrar(lista,filtro,llave)
    
    for elemento in lista_aux:
        if (elemento not in lista_filtrada):
            lista_filtrada.append(elemento)

    return lista_filtrada

def selAnimal (animales:list[dict], nombre_lista:str='Animales') -> dict:
    imprimirListaAnimales(animales,nombre_lista)
    while (True):
        sel = int(input('>> '))-1
        if (sel in range(len(animales))):
            return animales[sel]