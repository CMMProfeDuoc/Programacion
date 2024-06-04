"""
    Cree un dos funciones para calcular el area de
    un cilindro.
    
    Primero cree una funcion que calcule el area de un
    circulo (Acirculo = radio * radio * 3.1415)

    Luego use la Fx anterior para calcular el area
    del cilindro
    Acilindro = (2 * A_circulo) + (altura * radio * 2 * 3.1415)

    El usuario ingresa la altura y el radio
"""

def area_circulo (radio:float) -> float:
    area = radio * radio * 3.14159
    return area

def circunferencia (radio:float) -> float:
    circ = radio * 2 * 3.14159
    return circ

def area_cilindro (radio:float, altura:float) -> float:
    area = (2 * area_circulo(radio)) + (altura * circunferencia(radio))
    return area


cilindro = {
    'radio':float(input('ingrese radio: ')),
    'altura':float(input('ingrese altura: ')),
}

cilindro['area'] = area_cilindro(cilindro['radio'],cilindro['altura'])

print(cilindro)
