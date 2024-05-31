# s007

"""
    - Crear un menu para seleccionar una de las siguientes acciones:

        ✔ Mostrar animales en la lista, de forma numerada, mostrando "nombre"
        Para poder seleccionar un animal y mostrar los detalles del animal. 

        - Seleccionar un animal de la lista y guardarlo en otra lista separada, la nueva lista no puede tener repetidos.

        - Filtrar animales segun el <tipo>. El <tipo> lo ingresa el usuario.
"""

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
    for i,animal in enumerate(lista_animales):
        print(i+1, animal['nombre'])

    sel = int(input('>> '))-1

    for k in lista_animales[sel].keys():
        print(k, lista_animales[sel][k])
    print('-'*10)

    if (input('ingrese <guardar> para guardar el animal: ').lower() == 'guardar'):
        animales_guardados.append(lista_animales[sel])

    for animal in animales_guardados:
        print(animal)
    print()


    if(input('ingrese <salir> para finalizar programa: ').lower() == 'salir'):
        break
