# SECCION 002 D
# V 4.5
# fecha: 30/05
# hagan los ejercicios

"""
    ✔ Agregar menu para seleccionar:
        ✔ - Mostrar la lista numerada de animales (para poder seleccionar)
            y mostrar detalle del animal 
            ✔ >> solucionar posibles errores en seleccion
        
        - Guardar los animales seleccionados
    
        - Mostrar animales seleccionados

        ✔ Poder 'filtrar' la lista de animales, segun el tipo
        
        - Agregar animales a la lista (deben tener los mismos datos,
        nombre, tipo, peso, color)

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

def selOpcion (lista:list) -> int:
    while (True):
        sel = input(">> ")
        if (sel.isnumeric()):
            sel = int(sel)-1
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

opciones_menu = [
    'mostrar lista animales y seleccionar',
    'seleccionar por tipo',
    'agregar animales',
]

while (True): #WHILE MENU
    mostrarLista(opciones_menu)
    sel = selOpcion(opciones_menu)

    if (sel == 0):
        mostrarAnimalLista(lista_animales)
        print()
        sel = selOpcion(lista_animales)

        animal_seleccionado = lista_animales[sel]
        print('-'*10)
        for llave in animal_seleccionado.keys():
            print(llave,'=>',animal_seleccionado[llave])
        continue            
    #end if 0

    if (sel == 1):
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
        
    if (sel == 2):
        print("OPCION AUN NO LISTA")
        continue
