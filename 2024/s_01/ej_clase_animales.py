# SECCION 001 D
# V 1.9
# fecha: 7/6
# hagan los ejercicios

from os import system

def pausa () -> None:
    input('presione enter para continuar...')

def detalleAnimal (animal:dict) -> None:
    for k in animal.keys():
        print(k,'=>',animal[k])

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

def selAnimal (animales:list[dict], nombre_lista:str='Animales') -> dict:
    imprimirListaAnimales(animales,nombre_lista)
    while (True):
        sel = int(input('>> '))-1
        if (sel in range(len(animales))):
            return animales[sel]

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
    'salir':['s','salir','chao'], # ✔
    'ver animales':['v','ver'], # ✔
    'filtrar':['f','filtrar'], # ✔
    'ver detalle':['d'], # ✔
    'ver animales guardados':['g'], # ✔
    'eliminar animal':['del'], # ✔
    'modificar animal':['mod'], # ✔
    'modificar lista guardada': ['lista'], #<<<
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
