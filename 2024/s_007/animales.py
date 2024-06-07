# s007
# 7/6
# V 1.8 <-

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


def selectAnimal (lista:list[dict],nombre_lista:str) -> dict:
    imprimirAnimales(lista,nombre_lista)
    while(True): #gg usuario
        sel = int(input('>> '))-1
        if (sel in range(len(lista))):
            return lista[sel]
        else:
            print('opcion invalida... ')

def guardarAnimal (animal:dict, lista_objetivo:list[dict]) -> list[dict]:
    if (animal not in lista_objetivo):
        lista_objetivo.append(animal)
        print('animal guardado')
    else:
        print('animal ya guardado')
    return lista_objetivo

def mostrarDetalleAnimal (animal:dict) -> None:
    for key in animal.keys():
        print(key,'=>',animal[key])

def pausa() -> None:
    input('presione enter para continuar... ')

#variables

#instrucciones

opciones_menu = {
    'salir':['exit'], #✔
    'ver animales':['ver','v','mirar'], #✔🐱‍🐉
    'filtrar':['f','filtrar'], # ✔ Agregar la opcion de guardar los elementos que aparecen
    'buscar':['b'], #<<
    'ver detalle':['detalle'], # ✔
    'agregar animal':['a'], #<<
    'eliminar':['del'], #<<
    'modificar':['mod'], #<<
    'ver guardados':['g','guardados'],
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
        animal_selec = selectAnimal(lista_animales,'Animales')

        if (input('ingrese <guardar> para guardar el animal: ').lower() == 'guardar'):
            animales_guardados = guardarAnimal(animal_selec,animales_guardados)

    if (selec in opciones_menu['filtrar']):
        lista_filtrada = superFiltro(lista_animales,input('ingrese filtro: '))
        imprimirAnimales(lista_filtrada,'Resultado')
        pausa()

    if (selec in opciones_menu['ver detalle']):
        animal = selectAnimal(lista_animales,'Seleccionar')
        mostrarDetalleAnimal(animal)
        pausa()

    if (selec in opciones_menu['ver guardados']):
        imprimirAnimales(animales_guardados,'Guardados')
        pausa()

    if (selec in opciones_menu['salir']):
        break
