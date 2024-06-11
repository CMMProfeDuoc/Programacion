# SECCION 003 D
# V 1.7
# fecha: 5/6
# hagan los ejercicios

from funciones import *
# from X import * = traer todo

# import = 'traer' otro archivo
# from X import Y = desde X solo traer Y
# import X as Z = trae X y llamalo Z
# from X import Y as Z = trae Y desde X y llamalo Z

import datos_animales as datos

nombre_archivo = 'datos_gatos.csv'
lista_animales = datos.obtenerDatos(nombre_archivo)

while (True): #programa

    opciones_menu = {
        'salir':['s','salir','chao'],
        'ver animales':['v','ver'],
        'filtrar':['/f','f','filtrar','filter'],
        'filtrar por tipo':['ft','tipo'], #<<
        'agregar':['a','add'], #<<
        'quitar':['q','quitar','eliminar','delete'],#<<
        'modificar':['m','mod','modificar'], #<<
        'guardar':['g'], #✔
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

    if (sel in opciones_menu['guardar']):
        datos.guardarDatos(lista_animales,nombre_archivo)

    if (sel in opciones_menu['quitar']):
        mostrarListaAnimales(lista_animales,'Quitar Animal')
        while (True):
            sel = int(input(">> "))-1
            if (sel in range(len(lista_animales))):
                animal = lista_animales[sel] 
                for llave in animal.keys():
                    print(llave,': ',animal[llave],sep='')
                print('-'*10)
                break
        lista_animales.pop(sel)