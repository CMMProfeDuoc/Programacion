# SECCION 002 D
# V 3
# fecha: 28/05
# hagan los ejercicios

"""
    ✔ 4. agregar menu para seleccionar:
        ✔ 1. Mostrar la lista numerada de animales (para poder seleccionar) 
        ✔ 1.5. solucionar posibles errores en seleccion
        ✔ 2. Poder 'filtrar' la lista de animales, segun el tipo
        3. Agregar animales a la lista (deben tener los mismos datos,
        nombre, tipo, peso, color)
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
    for i, opcion in enumerate(opciones_menu):
        print(i+1, opcion)
    print()
    while (True):
        sel = input(">>: ")
        if (sel.isnumeric()):
            sel = int(sel)-1
            if (sel in range(len(opciones_menu))):
                break

    if (sel == 0):
        for i, animal in enumerate(lista_animales):
            print(i+1,'. ', animal['nombre'],' | ', animal['tipo'], sep='')
        print()
        while (True):
            sel = input("seleccione animal: ")
            if (sel.isnumeric()):
                sel = int(sel)-1
                if (sel in range(len(lista_animales))):
                    break

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
        for i, animal in enumerate(lista_filtrada):
            print(i+1,'. ', animal['nombre'],' | ', animal['tipo'], sep='')
        print()
        input()
        continue
    #end if 1
        
    if (sel == 2):
        print("OPCION AUN NO LISTA")
        continue

