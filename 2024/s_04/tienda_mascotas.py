# V 1.2
# 30/5

"""
    4. Añadir prevencion de errores al seleccionar cosas del menu

    ✔ 1. Mostrar lista animales, enumerada, mostrando solo nombre y tipo
    ✔    1.5. Seleccionar un animal y mostrar los detalles

    ✔ 2. Filtrar animal segun el tipo (ingresado por usuario)

    3. Agregar un animal, que debe tener, por lo menos, los sig atributos
    nombre, tipo, color, peso
"""

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
    for i, opcion in enumerate(opciones_menu):
        print(i, opcion)
    sel_opcion = int(input(">> "))

    if (sel_opcion == 0):
        break

    #1 - mostrar y seleccionar
    if (sel_opcion == 1):
        for i, animal in enumerate(lista_animales):
            print(i+1,'. ', animal['nombre'],' => ',animal['tipo'], sep='')

        sel = int(input(">> "))-1
        animalSel = lista_animales[sel]
        for key in animalSel:
            print(key,'=>',animalSel[key])    


    #2 - filtrar por tipo
    if (sel_opcion == 2):
        lista_filtrada = []
        filtro = input("ingrese <tipo> filtro: ").lower()
        for animal in lista_animales:
            if (animal['tipo'] == filtro):
                lista_filtrada.append(animal)

        for i, animal in enumerate(lista_filtrada):
            print(i+1,'. ', animal['nombre'],' => ',animal['tipo'], sep='')

    if (sel_opcion == 3):
        print("trabajo en progreso")
