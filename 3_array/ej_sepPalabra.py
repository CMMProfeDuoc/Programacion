"""
Cree un programa que tenga un string que tendra una palabra y luego un numero
de varios digitos.
Indique cual es la palabra y cual es el digito, por separado.
Solo sabe que el string vendra en formato 'palabra-numero'
El numero es siempre positivo y entero

DESAFIO: no usar .split()
"""

palabra = input("ingrese palabra-numero >> ")

pal = ''
num = ''
guion_encontrado = False

for letra in palabra:
    if (letra == '-'):
        guion_encontrado = True
        continue

    if (guion_encontrado):
        num += letra
    else:
        pal += letra

print(pal)
print(num)
