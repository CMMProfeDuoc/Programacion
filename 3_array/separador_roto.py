"""
Cree un programa que tenga un string que tendra una palabra y luego un numero
de varios digitos.
Indique cual es la palabra y cual es el digito, por separado.
Solo sabe que el string vendra en formato 'palabra-numero'
El numero es siempre positivo y entero

DESAFIO: no usar .split()
"""

palabra = input("ingrese texto: ")
separador = input("Ingrese elemento para separar: ")

lista_separada = []
pal = ''

# CORREJIR: que no se agrege el 'separador' a las palabras de la lista

for letra in palabra:
    if (letra == separador):
        lista_separada.append(pal)
        pal = ''
    pal += letra
lista_separada.append(pal)

print(lista_separada)
    