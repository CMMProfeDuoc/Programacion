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

lista_animales = []
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

for animal in lista_animales:
    for llave in animal:
        print(llave, '=>',animal[llave])
    print('-'*10)

