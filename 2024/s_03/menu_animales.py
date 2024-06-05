# SECCION 003 D
# V 1.7
# fecha: 5/6
# hagan los ejercicios

"""
    ✔ 1. Mostrar la lista numerada de animales (para poder seleccionar)
    
    ✔ Crear funcion para filtrar por llave
        La funcion recibe una lista y un filtro
        Y devuelve una lista con los elementos filtrados
        (recordar que los elementos no se pueden repetir)

    >> Agregar animales a la lista (deben tener los mismos datos,
    nombre, tipo, peso, color)
"""

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

lista_animales = [
    {
        'nombre': 'pepito',
        'tipo' : 'gato',
        'peso' : 7.2, 
        'color' : 'naranjo',
    },
    {
        'nombre': 'jaimico',
        'tipo' : 'mandril',
        'peso' : 20.2, 
        'color' : 'plomo',
    },
    {
        'nombre': 'soy la comadreja',
        'tipo' : 'comadreja',
        'peso' : 7.2, 
        'color' : 'rojo',
    },
    {
        'nombre': 'mojojojo',
        'tipo' : 'mono',
        'peso' : 25.3, 
        'color' : 'verde',
    },
    {
        'nombre': 'mordecai',
        'tipo' : 'azulejo',
        'peso' : 2.2, 
        'color' : 'azul',
    },
    {
        'nombre': 'skips',
        'tipo' : 'yeti',
        'peso' : 200, 
        'color' : 'blanco',
    },
    {
        'nombre': 'juanito',
        'tipo' : 'gato',
        'peso' : 6, 
        'color' : 'negro',
    },
    {
        'nombre': 'pedrito',
        'tipo' : 'mapache',
        'peso' : 5, 
        'color' : 'cafe',
    },
    {
        'nombre': 'rocket',
        'tipo' : 'mapache',
        'peso' : 5, 
        'color' : 'plomo',
    },
]


while (True): #programa

    opciones_menu = {
        'salir':['s','salir','chao'],
        'ver animales':['v','ver'],
        'filtrar':['/f','f','filtrar','filter'],
        'filtrar por tipo':['ft','tipo'], #<<
        'agregar':['a','add'], #<<
        'quitar':['q','quitar','eliminar','delete'],#<<
        'modificar':['m','mod','modificar'] #<<
    }

    #Agregar opciones marcadas
    
    sel = seleccionMenu(opciones_menu)

    if (sel in opciones_menu['ver animales']):
        mostrarListaAnimales(lista_animales,'Animales')
        while (True):
            sel = int(input(">> "))-1
            if (sel in range(len(lista_animales))):
                animal = lista_animales[sel] 
                for llave in animal.keys():
                    print(llave,': ',animal[llave],sep='')
                print('-'*10)
                break

    if (sel in opciones_menu['filtrar']):
        print('Filtrar: ')
        lista_filtrada = filtrarTodo(
            lista_animales,
            input('ingrese filtro: ')
            )
        mostrarListaAnimales(lista_filtrada,'Resultado')

    if (sel in opciones_menu['salir']):
        print("adios")
        break
