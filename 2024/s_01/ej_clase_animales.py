# SECCION 001 D
# V 1.7
# fecha: 
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
            >> Crear funcion para filtrar por cualquier llave (el usuario selecciona)
        ✔ Mostrar lista de animales seleccionados
            > Poder seleccionar y modificar el dato de un animal
        - Poder agregar datos extra a un animal (seleccionado)
        - Poder seleccionar usando un nombre
        - Agregar Animal
"""

from os import system

def pausa () -> None:
    input('presione enter para continuar...')

def imprimirListaAnimales (lista_animales:list[dict], nombre_lista:str = 'Lista Animales') -> None:
    print('--',nombre_lista,'--')
    for i, animal in enumerate(lista_animales):
        print(i+1,animal['nombre'])
    print('-'*10)

def filtrar (lista:list[dict], filtro:str, llave:str='nombre') -> list:
    lista_filtrada = []
    for elemento in lista:
        if (str(elemento[llave]) in str(filtro)):
            lista_filtrada.append(elemento)
    return lista_filtrada

def filtrarTodo (lista:list[dict], filtro:str) -> list:
    lista_filtrada = []
    lista_aux = []
    for elemento in lista:
        for llave in elemento.keys():
            lista_aux += filtrar(lista,filtro,llave)
    
    for elemento in lista_aux:
        if (elemento not in lista_filtrada):
            lista_filtrada.append(elemento)

    return lista_filtrada

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
        'nombre':'Luciano',
        'tipo':'mandril',
        'color':'blano con pelo negro',
        'peso':400,
        #'lentes':True, #solucionar esto   
    }
]

opciones_menu = {
    'salir':['s','salir','chao'],
    'ver animales':['v','ver'],
    'filtrar':['f','filtrar'],
    'ver detalle':['d']
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
        imprimirListaAnimales(lista_animales)
        
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

    #filtrar
    if (sel in opciones_menu['filtrar']):
        lista_filtrada = filtrarTodo(
            lista_animales,
            input('ingrese filtro: ')
        )
        imprimirListaAnimales(lista_filtrada,'Resultado Busqueda')
        pausa()
        continue
    
    if (sel in opciones_menu['ver detalle']):
        imprimirListaAnimales(animales_guardados,'Animales Guardados')
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
