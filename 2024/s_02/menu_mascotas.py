# SECCION 002 D
# V 4.5
# fecha: 30/05
# hagan los ejercicios

"""
    ✔ Agregar menu para seleccionar:
        ✔ - Mostrar la lista numerada de animales (para poder seleccionar)
            y mostrar detalle del animal 
            ✔ >> solucionar posibles errores en seleccion
        
        ✔ Guardar los animales seleccionados
            
    ✔ Mostrar animales seleccionados
        opciones:
        - limpiar lista
        - ver detalle de un animal
        - quitar item de lista
        
    ✔ Poder 'filtrar' la lista de animales, segun el tipo
        - Agregar a la selccion
        
    ✔ Agregar animales a la lista (deben tener los mismos datos,
        nombre, tipo, peso, color)
        - validar datos

    ✔ Crear Funcion que determine si una seleccion es valida
            El usuario tiene un rango de seleccion, y la funcion retorna True o False
            dependiendo si la seleccion es valida o no

    - Eliminar Animal
            - mostrar la lista
            - seleccionar que cosa eliminar

    - Modificar el dato de un animal

    - Agregar un dato (llave : valor) a un animal           

    

"""

def mostrarLista (lista:list) -> None:
    for i, elemento in enumerate(lista):
        print(i,'=>',elemento)

def mostrarAnimalLista (lista:list) -> None:
    for i, animal in enumerate(lista):
        print(i+1,'. ', animal['nombre'],' => ', animal['tipo'], sep='')

def selOpcion (lista:list,desfase:int=0) -> int:
    while (True):
        sel = input(">> ")
        if (sel.isnumeric()):
            sel = int(sel)-desfase
            if (sel in range(len(lista))):
                break
    return sel

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
        'nombre': 'rigby',
        'tipo' : 'mapache',
        'peso' : 8, 
        'color' : 'cafe',
    },
    {
        'nombre': 'pedro',
        'tipo' : 'mapache',
        'peso' : 5, 
        'color' : 'negro',
    },
    {
        'nombre': 'panxito',
        'tipo' : 'conejo',
        'peso' : 3, 
        'color' : 'verde',
    },
    {
        'nombre': 'panxote',
        'tipo' : 'conejo',
        'peso' : 10, 
        'color' : 'azul',
    },
]

animales_guardados = []

opciones_menu = [
    'salir', #con 0 se sale
    'mostrar lista animales y seleccionar',
    'seleccionar por tipo',
    'agregar animales',
    'mostrar animales guardados'
]

while (True): #WHILE MENU
    mostrarLista(opciones_menu)
    sel = selOpcion(opciones_menu)

    if (sel==0):
        break
    
    if (sel == 1):
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
    #end if 0

    if (sel == 2):
        lista_filtrada = []
        filtro = input('ingrese tipo a filtrar: ').lower()
        for animal in lista_animales:
            if animal['tipo'] == filtro:
                lista_filtrada.append(animal)
        mostrarAnimalLista(lista_filtrada)
        print()
        input() # pausa
        continue
    #end if 1
        
    #agregar animal a la lista
    if (sel == 3):
        #Falta crear validacion de datos
        lista_animales.append(
            {
                'nombre': input('ingrese nombre: '),
                'tipo' : input('ingrese tipo: '),
                'peso' : float(input('ingrese peso: ')), 
                'color' : input('ingrese color: '),
            }
        )

    if (sel == 4):
        mostrarAnimalLista(animales_guardados)
        continue
