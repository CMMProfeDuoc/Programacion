# s007
# 31/5
# V 1.5 <-

"""
    ✔ Crear un menu para seleccionar una de las siguientes acciones:

        ✔ Mostrar animales en la lista, de forma numerada, mostrando "nombre"
        Para poder seleccionar un animal y mostrar los detalles del animal. 

        ✔ Seleccionar un animal de la lista y guardarlo en otra lista separada, la nueva lista no puede tener repetidos.

        - Filtrar animales segun el <tipo>. El <tipo> lo ingresa el usuario.

        - Filtrar por nombre

        - Agregar animal (asegurar que el id no se repita!)
            (el ID no lo ingresa el usuario)!!
            El resto de datos (nombre, tipo, color) los ingresa el usuario
    
    >> crear más comandos.
"""
opciones_menu = {
    'salir':['exit'],
    'ver animales':['/ver','/v','/mirar'], #comandos!
    'filtrar animal por tipo':['filtrar'],
    #'agregar animal':3,
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
        for i,animal in enumerate(lista_animales):
            print(i+1, animal['nombre'])

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

    if (selec in opciones_menu['filtrar animal por tipo']):
        print("EN PROGRESO")

    if (selec in opciones_menu['salir']):
        break

    if (selec not in opciones_menu.values()):
        print('opcion invalida. tonoto')
