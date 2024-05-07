"""
Cree un programa que reciba numeros positivos, del 0 al 15. el programa se detiene cuando se ingresa un numero negativo. Luego muestre cuanto se repite cada numero.

DESAFIO: Maximo 2 ciclos.
"""
# Crear lista con 16 0's
lista_numeros = []
for i in range(16):
    lista_numeros.append(0)

while (True):
    n = int(input(">> ")) #asumimos que el usuario no es mono
    if (n < 0):
        break
    if (n > 15):
        continue
    
    lista_numeros[n] += 1

for i in range(len(lista_numeros)):
    print(i,'>',lista_numeros[i])