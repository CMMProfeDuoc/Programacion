# V 1.7.1
# 6/6

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
        
def selecItemMenu (menu:dict, nombreMenu:str='Menu') -> int:
    #llave : int(valor)
    print('--',nombreMenu,'--')
    for opcion in menu.keys():
        print(menu[opcion], opcion)

    while(True):
        selec = int(input('>> '))
        if (selec in menu.values()):
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

opciones_menu = {
    'salir':0,
    'seleccionar Animales':1,
    'ver Detalles':2, #de lista de animales 'seleccionados, elegir y mostrar detalles'
    'modificar datos':3, #<<<<<
    'eliminar':4, #<<
    'filtrar':5,
    'agregar (WIP)':6, #<<
}

while (True):
    sel_opcion = selecItemMenu(opciones_menu)

    if (sel_opcion == opciones_menu['salir']):
        break

    #1 - mostrar y seleccionar
    if (sel_opcion == opciones_menu['seleccionar Animales']):
        imprimirListaAnimales(lista_animales,'Animales')

        sel = int(input(">> "))-1
        animalSel = lista_animales[sel]
        for key in animalSel:
            print(key,'=>',animalSel[key])    


    #2 - filtrar por tipo
    if (sel_opcion == opciones_menu['filtrar']):
        lista_filtros = ['nombre','color','tipo','peso']
        sel_filtro = selecItemLista(lista_filtros,'Llaves Busqueda')
        lista_filtrada = filtrarListaDict(
            lista_animales,
            lista_filtros[sel_filtro],
            input('ingrese filtro: ')
        )
        imprimirListaAnimales(lista_filtrada,'Resultado Filtro')


    if (sel_opcion == opciones_menu['agregar (WIP)']):
        print("trabajo en progreso")

    if (sel_opcion == opciones_menu['eliminar']):
        print('WIP')

    if (sel_opcion == opciones_menu['modificar datos']):
        animal_selec = lista_animales[selecItemLista(lista_animales,'Seleccionar')]
        print('seleccione opcion a modificar')
        lista_llaves = list(animal_selec.keys())
        llave_mod = lista_llaves[selecItemLista(lista_llaves,'Llaves a Modificar')]
        print('Modificar:')
        animal_selec[llave_mod] = input('>> ')
