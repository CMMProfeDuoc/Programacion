# s007
# 31/5
# V 1.5 <-

#import

#funciones
#filtrar, filtra cosas de una lista
def isOnDict (diccionario:dict, filtro:str) -> bool:
    for dato in diccionario.values():
        if (str(filtro) in str(dato)):
            return True
    return False

def superFiltro (lista_objetivo:list[dict], filtro:str) -> list[dict]:
    lista_filtrada = []
    for elemento in lista_objetivo:
        if (isOnDict(elemento,filtro)):
            lista_filtrada.append(elemento)
    return lista_filtrada

def imprimirAnimales (lista:list[dict], nombre_lista:str='Animales') -> None:
    print('--',nombre_lista,'--')
    for i,elemento in enumerate(lista):
        print(i+1,'->',elemento['nombre'])
    print('-'*10)

#sin uso
def filtrar (lista_objetivo:list[dict], llave_filtro:str, filtro:str) -> list[dict]:
    lista_filtrada = []
    for elemento in lista_objetivo:
        if (filtro in elemento[llave_filtro]):
            lista_filtrada.append(elemento)
    return lista_filtrada

#obsoleto
def filtroMultiple (lista_objetivo:list[dict], lista_llaves:list[str], filtro:str) -> list[dict]:
    lista_filtrada = []
    lista_sin_rep = []
    for llave in lista_llaves:
        lista_filtrada += filtrar(lista_objetivo,llave,filtro)

    #remover repetidos
    for elemento in lista_filtrada:
        if (elemento not in lista_sin_rep):
            lista_sin_rep.append(elemento)

    return lista_sin_rep

def pausa() -> None:
    input('presione enter para continuar... ')

#variables

#instrucciones

opciones_menu = {
    'salir':['exit'], #✔
    'ver animales':['ver','v','mirar'], #✔🐱‍🐉
    'filtrar':['f','filtrar'], # ✔ Agregar la opcion de guardar los elementos que aparecen
    'buscar':['b'], #<<
    'ver detalle':['detalle'], #<<
    'agregar animal':['a'], #<<
    'eliminar':['del'], #<<
    'modificar':['mod'], #<<
}

lista_animales = [
    {
        'id' : 1,
        'nombre' : 'panxito',
        'tipo' : 'panda',
        'color' : 'blanco con amarillo',
        'com_fav' : ['gohan','bamboo']
    },
    {
        'nombre' : 'pepito',
        'tipo' : 'gato',
        'color' : 'verde',
        'id' : 2,
    },
    {
        'nombre' : 'pepita',
        'tipo' : 'pig',
        'color' : 'rosada',
        'id' : 3,
    },
    {
        'nombre' : 'rigby',
        'tipo' : 'mapache',
        'color' : 'cafe',
        'id' : 4,
    },
    {
        'nombre' : 'mordecai',
        'tipo' : 'azulejo',
        'color' : 'azul',
        'id' : 5,
    },
    {
        'nombre' : 'pedrito',
        'tipo' : 'mapache',
        'color' : 'plomo',
        'id' : 6,
    },
]



animales_guardados = []

while (True):

    for llave in opciones_menu.keys():
        print(llave,'=> ',opciones_menu[llave])

    selec = input('>> ')


    if (selec in opciones_menu['ver animales']):
        imprimirAnimales(lista_animales)

        sel = int(input('>> '))-1

        anm_sel = lista_animales[sel]
        for k in anm_sel.keys():
            print(k, anm_sel[k])
        print('-'*10)

        if (input('ingrese <guardar> para guardar el animal: ').lower() == 'guardar'):
            if (anm_sel not in animales_guardados):
                animales_guardados.append(anm_sel)
                print('animal guardado!')

        for animal in animales_guardados:
            print(animal)
        print()

    if (selec in opciones_menu['filtrar']):
        lista_filtrada = superFiltro(lista_animales,input('ingrese filtro: '))
        imprimirAnimales(lista_filtrada,'Resultado')
        pausa()

    if (selec in opciones_menu['salir']):
        break
