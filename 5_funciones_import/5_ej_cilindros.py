"""
    Cree un dos funciones para calcular el area de
    un cilindro.
    
    Primero cree una funcion que calcule el area de un
    circulo (Acirculo = radio * radio * 3.1415)

    Luego use la Fx anterior para calcular el area
    del cilindro
    Acilindro = (2 * A_circulo) + (altura * radio)

    El usuario ingresa la altura y el radio
"""

def areaCirculo (radio:float) -> float:
    area = radio * radio * 3.1415
    return area

def areaCilindro (radio:float, altura:float) -> float:
    area = (2 * areaCirculo(radio)) + (radio * altura)
    return area


cilindro = {
    'radio' : float(input('radio: ')),
    'altura' : float(input('altura: '))
}

cilindro['area'] = areaCilindro(cilindro['radio'],cilindro['altura'])

print(cilindro)
