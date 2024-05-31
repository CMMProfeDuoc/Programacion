# SECCION 001 D
# V 1.3
# fecha: 31/05
# hagan los ejercicios

"""
    Cree un programa que permita ingresar animales a una tienda de mascotas. Los animales tienen los siguientes atributos:
    nombre, tipo, peso, color
    Se detiene el ingreso luego de 5 animales.
    Luego, muestre los animales listados.

    - Crear menu para seleeccionar de estos items:

        ✔ Mostrar la lista numerada de animales (para poder seleccionar)
        ✔ Poder 'filtrar' la lista de animales
        - Poder seleccionar y modificar el dato de un animal
        - Poder agregar datos extra a un animal (seleccionado)
        - Poder seleccionar usando un nombre
        - Agregar Animal
"""

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
]

opciones_menu = [
    'salir', #0
    'mostrar lista numerada', #1
    'filtrar por nombre', #2
]

while (True):
    for i, opcion in enumerate(opciones_menu):
        print(i, opcion)

    sel = int(input('>> '))

    print('-'*10)
    print()

    if (sel == 0):
        break

    #mostrar lista numerada
    if (sel == 1):
        print('ID | Nombre | Tipo | Peso | Color')
        for i, animal in enumerate(lista_animales):
            print(i,'.',end=' ')
            for dato in animal.values():
                print(dato,end=' | ')
            print()

    #filtrar por nombre
    if (sel == 2):
        filtro = input('ingrese nombre a filtrar: ')
        llave_filtro = 'nombre'
        lista_filtrada = []
        for animal in lista_animales:
            if (filtro in animal[llave_filtro]):
                lista_filtrada.append(animal)

        print("LISTA FILTRADA")
        print('ID | Nombre | Tipo | Peso | Color')
        for i, animal in enumerate(lista_filtrada):
            print(i,'.',end=' ')
            for dato in animal.values():
                print(dato,end=' | ')
            print()

    print()
