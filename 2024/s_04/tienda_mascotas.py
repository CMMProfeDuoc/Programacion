# V 01
# 30/5

"""
    1. Mostrar lista animales, enumerada, mostrando solo nombre y tipo
        1.5. Seleccionar un animal y mostrar los detalles

    2. Filtrar animal segun el tipo (ingresado por usuario)

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

for animal in lista_animales:
    print(animal)
