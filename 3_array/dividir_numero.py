"""
Cree un programa que reciba un numero decimal e intercambie la parte decimal por la parte entera

123,321 -> 321,123
23,0123 -> 0123,23

Si el numero ingresado tiene más de 1 coma, solo se considera la primera coma (todos los numeros tras la segunda se ignoran)

12,654,301 -> 654,12
"""

texto_numero = input(">> ")

cont_comas = 0

primera_parte = []
segunda_parte = []

new_number = ''

for letra in texto_numero:
    if (letra == ','):
        cont_comas +=1
    if (cont_comas > 1):
        break
    if (cont_comas == 0):
        if (letra.isdigit()):
            primera_parte.append(letra)
    else:
        if (letra.isdigit()):
            segunda_parte.append(letra)

for letra in segunda_parte:
    new_number += letra
new_number += ','
for letra in primera_parte:
    new_number += letra

print(new_number)
    

