# SECCION 001 D
# V 1.2
# fecha: 27/05
# hagan los ejercicios

"""
    Cree un programa que permita ingresar animales a una tienda de mascotas. Los animales tienen los siguientes atributos:
    nombre, tipo, peso, color
    Se detiene el ingreso luego de 5 animales.
    Luego, muestre los animales listados.

    1. Mostrar la lista numerada de animales (para poder seleccionar)
    2. Poder 'filtrar' la lista de animales
    3. Poder seleccionar y modificar el dato de un animal
    4. Poder agregar datos extra a un animal (seleccionado)
    5. Poder seleccionar usando un nombre
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
max_animales = 2

for i in range(max_animales):
    lista_animales.append(
        {
            'nombre': input('ingrese nombre: '),
            'tipo' : input('Ingrese tipo: '),
            'peso' : float(input('ingrese peso: ')), 
            'color' : input('color: '),
        }
    )
    print()

print('-'*10)
print()

#mostrar lista numerada
print('ID | Nombre | Tipo | Peso | Color')
for i, animal in enumerate(lista_animales):
    print(i,'.',end=' ')
    for dato in animal.values():
        print(dato,end=' | ')
    print()

#filtrar por nombre
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

