# SECCION 001 D
# V 1.9
# fecha: 7/6
# hagan los ejercicios

from os import system

from funciones import *

nombre_archivo = 'datos_gatos.csv'
import datosAnimales
lista_animales = datosAnimales.extraerDatosAnimales(nombre_archivo)

opciones_menu = {
    'salir':['s','salir','chao'], # ✔
    'ver animales':['v','ver'], # ✔
    'filtrar':['f','filtrar'], # ✔
    'ver detalle':['d'], # ✔
    'ver animales guardados':['g'], # ✔
    'eliminar animal':['del'], # ✔
    'modificar animal':['mod'], # ✔
    'modificar lista guardada': ['lista'], #<<<
    'guardar Archivo':['guardar']
}

animales_guardados = []

while (True):

    # limpar pantalla
    system('cls') #solo funciona en windows

    for opcion in opciones_menu.keys():
        print (opcion,' => ',opciones_menu[opcion])

    print('ingrese un comando: ')
    sel = input('>> ')

    print('-'*10)
    print()

    if (sel in opciones_menu['salir']):
        if (sel == 'chao'):
            print('hasta la proxima!')
        break

    #mostrar lista numerada
    if (sel in opciones_menu['ver animales']):
        animal = selAnimal(lista_animales,'Lista Animales')
        if (animal not in animales_guardados):
            animales_guardados.append(animal)
        else:
            print('animal ya esta guardado')

        print('ID | Nombre | Tipo | Peso | Color')
        for dato in animal.values():
            print(dato,end=' | ')
        continue

    #filtrar
    if (sel in opciones_menu['filtrar']):
        lista_filtrada = filtrarTodo(
            lista_animales,
            input('ingrese filtro: ')
        )
        animal_sel = selAnimal(lista_filtrada,'Resultado')
        if (animal not in animales_guardados):
            animales_guardados.append(animal)
        else:
            print('animal ya esta guardado')
        pausa()
        continue
    print()

    if (sel in opciones_menu['ver animales guardados']):
        imprimirListaAnimales(animales_guardados,'Guardados')
        input('presione enter para continuar... ')

    if (sel in opciones_menu['eliminar animal']):
        lista_animales.remove(selAnimal(lista_animales,'Eliminar animal'))
        pausa()

    if (sel in opciones_menu['modificar animal']):
        animal_sel = selAnimal(animales_guardados,'Modificar')
        detalleAnimal(animal_sel)
        llave_mod = input('ingrese llave a modificar: ')
        valor_mod = input('ingrese valor a modificar: ')
        animal_sel[llave_mod] = valor_mod
        pausa()

    if (sel in opciones_menu['ver detalle']):
        detalleAnimal(selAnimal(animales_guardados,'Guardados'))
        pausa()

    if (sel in opciones_menu['guardar Archivo']):
        datosAnimales.guardarDatosAnimales(lista_animales,nombre_archivo)
        pausa()