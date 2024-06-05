# SECCION 003 D
# V 1.3
# fecha: 5/6
# hagan los ejercicios

"""
    ✔ 1. Mostrar la lista numerada de animales (para poder seleccionar)
    
    >> Crear funcion para filtrar por llave
        La funcion recibe una lista y un filtro
        Y devuelve una lista con los elementos filtrados
        (recordar que los elementos no se pueden repetir)

    3. Agregar animales a la lista (deben tener los mismos datos,
    nombre, tipo, peso, color)
"""

def seleccionMenu (menu:dict) -> str:
    for opcion in menu.keys():
        print(opcion, '=>', menu[opcion])

    opc_sel = input('ingrese comando: ')
    return opc_sel


def mostrarListaAnimales (
        lista_animales:list[dict],
        nombre_lista:str,
        ) -> None:
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
        'filtrar':['/f','f','filtrar','filter']
    }

    sel = seleccionMenu(opciones_menu)

    if (sel in opciones_menu['ver animales']):
        #1
        #mostrar animales de la lista
        mostrarListaAnimales(lista_animales,'Animales')
        #1 seleccionar un animal y mostrar detalle
        while (True):
            sel = int(input(">> "))-1
            if (sel in range(len(lista_animales))):
                animal = lista_animales[sel] #asignar variable para mejor legibilidad
                for llave in animal.keys():
                    print(llave,': ',animal[llave],sep='')
                print('-'*10)
                break

    if (sel in opciones_menu['filtrar']):
        #2 - filtar
        print('Filtrar: ')
        lista_filtrada = []
        filtro = input('indique <tipo> a filtrar: ').lower()
        for animal in lista_animales:
            if (animal['tipo'].lower() in filtro):
                lista_filtrada.append(animal)
        print('-'*10)
        mostrarListaAnimales(lista_filtrada,'Resultado')

    if (sel in opciones_menu['salir']):
        print("adios")
        break
