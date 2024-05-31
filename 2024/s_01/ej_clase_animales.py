# SECCION 001 D
# V 1.5
# fecha: 31/05
# hagan los ejercicios

"""
    Cree un programa que permita ingresar animales a una tienda de mascotas. Los animales tienen los siguientes atributos:
    nombre, tipo, peso, color
    Se detiene el ingreso luego de 5 animales.
    Luego, muestre los animales listados.

    ✔ Crear menu para seleeccionar de estos items:

    > Al filtrar o seleccionar animales, guardarlos en una lista separada

        ✔ Mostrar la lista numerada de animales (para poder seleccionar)
        ✔ Poder 'filtrar' la lista de animales
        ✔ Mostrar lista de animales seleccionados
            > Poder seleccionar y modificar el dato de un animal
        - Poder agregar datos extra a un animal (seleccionado)
        - Poder seleccionar usando un nombre
        - Agregar Animal

        
"""

from os import system

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
    'mostrar lista de animales guardados', #3
]

animales_guardados = []

while (True):

    # limpar pantalla
    system('cls') #solo funciona en windows

    for i, opcion in enumerate(opciones_menu):
        print(i, opcion)

    sel = int(input('>> '))

    print('-'*10)
    print()

    if (sel == 0):
        break

    #mostrar lista numerada
    if (sel == 1):
        for i, animal in enumerate(lista_animales):
            print(i+1, animal['nombre'],' | ',animal['tipo'])
        
        sel = int(input('>> '))-1
        animal = lista_animales[sel]
        if (animal not in animales_guardados):
            animales_guardados.append(animal)
        else:
            print('animal ya esta guardado')

        print('ID | Nombre | Tipo | Peso | Color')
        for dato in animal.values():
            print(dato,end=' | ')
        continue

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
        continue
    
    if (sel == 3):
        for i,animal in enumerate(animales_guardados):
            print(i+1, animal['nombre'])
        print('seleccione animal para ver detalles y modificar')
        sel = int(input('>> '))-1
        animal = animales_guardados[sel]
        for llave in animal.keys():
            print(llave,'=>',animal[llave])
        print('escriba la llave a modificar o agregar')
        llave = input('>> ').lower()
        valor = input('valor: ')
        animales_guardados[sel][llave] = valor

        #modificar el dato en la lista original
        for animal in lista_animales:
            if (animal['nombre'] == animales_guardados[sel]['nombre']):
                animal[llave] = valor
        # no usar nombre como ID !!
        # crear llave ID
    print()
