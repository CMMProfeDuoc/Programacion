"""
1. Cree una funcion que revise la lista y entrege el resultado de si la lista esta o no ordenada
"""

lista = [1,2,3,4,1,2,3]


ordenada = True

for i in range(len(lista)-1):
    if (lista[i+1] < lista[i]):
        ordenada = False
        break

if (ordenada):
    print('Lista Ordenada')
else:
    print('Lista desordenada')
