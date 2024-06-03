"""
Cree un programa que calcule el area de distintas figuras.
Para eso, cree una funcion que reciba un numero (el radio) y
retorne el area del circulo ( A = r*r*3.1415 )

Luego cree una funcion que calcule el area de un cilindro, recibiendo el radio y el
alto de la figura.

(A = Acirculo * altura)

*Si el area es 'imposible' (menor a 0)
Retornar -1

Se le otorgara una lista de diccionarios con las mediadas de los cilindros
"""

def areaCirculo (radio:float) -> float:
    area = radio * radio * 3.1415
    return area

def areaCilindro (radio:float, altura:float) -> float:
    area = areaCirculo(radio) * altura
    return area

lista_cilindros = [
    {
        'radio':5,
        'altura':6,
    },
    {
        'radio':2.1,
        'altura': 5,
    },
    {
        'radio':3,
        'altura':18,
    },
]

for cilindro in lista_cilindros:
    cilindro.update({
        'area':areaCilindro(cilindro['radio'],cilindro['altura'])
    })
    print(cilindro)
