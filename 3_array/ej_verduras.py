"""
    Considere que tiene una lista de sabores
    de verduras y su peso en kg.
    Indique cuantos kilos de cada verdura hay.
    Usted sabe que solo hay 3 verduras.
        apio, lechuga, rabano

    El peso solo puede ser un numero positivo, de un digito (entre 0 y 9)
"""

lista_verduras = ['lechuga 5','apio 6','lechuga 1','rabano 3','apio 2', 'apio 1','papa 1','rabano 5','apio 7']

peso_verduras = [0,0,0]
# indice - > verdura
# 0 -> lechuga
# 1 -> apio
# 2 -> rabano

for verdura in lista_verduras:
    peso = int(verdura[-1])
    if ('lechuga' in verdura):
        peso_verduras[0] += peso

    if ('apio' in verdura):
        peso_verduras[1] += peso
        
    if ('rabano' in verdura):
        peso_verduras[2] += peso

print('kg lechugas',peso_verduras[0])
print('kg apio',peso_verduras[1])
print('kg rabano',peso_verduras[2])
