"""
Escriba un programa que reciba numeros (pueden ser enteros o decimales) y los guarde en una lista.

El programa deja de recibir numeros cuando el usuario ingresa 'salir'.

Luego, el programa pide dos cosas:
un numero
Y un simbolo, el simbolo puede ser '+' '=' o '-'

Si es (+) -> se eliminan los mayores al numero
Si es (-) -> se eliminan los menores al numero
Si es (=) -> se eliminan los iguales al numero
"""

lista_numeros = []

while (True):
    entrada = input(">> ").lower()
    if (entrada == 'salir'):
        break
    
    #FALTA COMPLETAR
    num = float(entrada)
    lista_numeros.append(num)

print(lista_numeros)

# -----------

nro = float(input("Ingrese numero: "))
simbolo = input("Ingrese simbolo (+) (-) (=): ")

lista_filtrada = []

for numero in lista_numeros:
    if (simbolo == '='):
        if (numero != nro):
            lista_filtrada.append(numero)

    if (simbolo == '+'):
        if (numero <= nro):
            lista_filtrada.append(numero)
    
    if (simbolo == '-'):
        if (numero >= nro):
            lista_filtrada.append(numero)

print(lista_filtrada)
    