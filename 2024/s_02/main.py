# SECCION 002 D
# V 5
# fecha: 31/05
# hagan los ejercicios

from os import system
 
from funciones import * #Traer todas las cosas sin necesidad de nombrarlas
import datos_mascotas as data #Traer las cosas pero se neceista nombrar
# 'as' asigna un pseudonimo

lista_animales = data.extraerDatos('datos_mascotas.csv')
opciones_menu = data.opciones_menu

animales_guardados = []

while (True): #WHILE MENU
    system('cls')

    sel = mostarMenu(opciones_menu)

    system('cls')

    if (sel in opciones_menu['salir']):
        data.guardarDatos(
            'datos_guardados.csv',
            animales_guardados,
            ['nombre','tipo','peso','color']
        )
        break
    
    if (sel in opciones_menu['ver_animales']):
        mostrarAnimalLista(lista_animales)
        print()
        sel = selOpcion(lista_animales,1)

        animal_seleccionado = lista_animales[sel]
        print('-'*10)
        for llave in animal_seleccionado.keys():
            print(llave,'=>',animal_seleccionado[llave])

        if (animal_seleccionado not in animales_guardados):
            animales_guardados.append(animal_seleccionado)

        continue            
    
    if (sel in opciones_menu['filtrar']):
        lista_filtrada = []
        filtro = input('ingrese tipo a filtrar: ').lower()
        for animal in lista_animales:
            if animal['tipo'] == filtro:
                lista_filtrada.append(animal)
        mostrarAnimalLista(lista_filtrada)
        print()
        input() # pausa
        continue
      
    if (sel in opciones_menu['agregar']):
        #Falta crear validacion de datos
        lista_animales.append(
            {
                'nombre': input('ingrese nombre: '),
                'tipo' : input('ingrese tipo: '),
                'peso' : float(input('ingrese peso: ')), 
                'color' : input('ingrese color: '),
            }
        )

    if (sel in opciones_menu['ver_guardados']):
        mostrarAnimalLista(animales_guardados)
        continue

    if (sel in opciones_menu['modificar']):
        print("MODIFICAR")
        if (animales_guardados == []):
            print('No hay animales para modificar. seleccionar un animal')
            continue
        
        animal = mostrarAndSelectAnimal(animales_guardados,1)
        mostrarDetalle(animal)
        animal.update({
            input('ingrese llave a modificar: ') : input('ingrese valor: ')
        })


    if (sel not in opciones_menu.values()):
        print('tonoto')
