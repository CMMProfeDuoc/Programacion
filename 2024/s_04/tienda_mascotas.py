# V 1.4
# 6/6

"""
    4. Añadir prevencion de errores al seleccionar cosas del menu

    ✔ 1. Mostrar lista animales, enumerada, mostrando solo nombre y tipo
    ✔    1.5. Seleccionar un animal y mostrar los detalles

    ✔ 2. Filtrar animal segun el tipo (ingresado por usuario)

    3. Agregar un animal, que debe tener, por lo menos, los sig atributos
    nombre, tipo, color, peso
"""

def imprimirListaAnimales (lista:list[dict], nombreLista:str='Lista') -> None:
    print('--',nombreLista,'--')
    for i, animal in enumerate(lista):
        print(i+1, animal['nombre'],animal['tipo'])
    print('-'*10)

def selecItemLista (lista:list, nombreLista:str) -> int:
    print('--',nombreLista,'--')
    for i, item in enumerate(lista):
        print(i+1, item)

    while (True):
        selec = int(input('>> '))-1
        if (selec in range(len(lista))):
            return selec
        
def filtrarListaDict (lista:list[dict], llave:str, filtro:str) -> list[dict]:
    lista_filtrada = []
    for elemento in lista:
        if (str(elemento[llave]) == str(filtro)):
            lista_filtrada.append(elemento)
    return lista_filtrada

lista_animales = [
    {
        'nombre' : 'Pedrito',
        'tipo' : 'mapache',
        'color' :'plomo',
        'peso' : 5,
    },
    {
        'nombre' : 'juanito',
        'tipo' : 'gato',
        'color' :'negro',
        'peso' : 5,
    },
    {
        'nombre' : 'mordecai',
        'tipo' : 'azulejo',
        'color' :'azul',
        'peso' : 2,
    },
    {
        'nombre' : 'rigby',
        'tipo' : 'mapache',
        'color' :'cafe',
        'peso' : 4,
    },
    {
        'nombre' : 'panxito',
        'tipo' : 'perro',
        'color' :'plomo',
        'peso' : 8,
    },
    {
        'nombre' : 'aslan',
        'tipo' : 'leon',
        'color' :'dorado',
        'peso' : 80,
    },
    {
        'nombre' : 'mufasa',
        'tipo' : 'leon',
        'color' :'naranjo',
        'peso' : 70,
    },
]

opciones_menu = [
    'salir',
    'seleccionar y mostrar detalle',
    'filtrar por TIPO',
    'agregar (WIP)',
]

while (True):
    sel_opcion = selecItemLista(opciones_menu,'Menu')

    if (sel_opcion == 0):
        break

    #1 - mostrar y seleccionar
    if (sel_opcion == 1):
        imprimirListaAnimales(lista_animales,'Animales')

        sel = int(input(">> "))-1
        animalSel = lista_animales[sel]
        for key in animalSel:
            print(key,'=>',animalSel[key])    


    #2 - filtrar por tipo
    if (sel_opcion == 2):
        lista_filtros = ['nombre','color','tipo','peso']
        sel_filtro = selecItemLista(lista_filtros,'Llaves Busqueda')
        lista_filtrada = filtrarListaDict(
            lista_animales,
            lista_filtros[sel_filtro],
            input('ingrese filtro: ')
        )
        imprimirListaAnimales(lista_filtrada,'Resultado Filtro')


    if (sel_opcion == 3):
        print("trabajo en progreso")
