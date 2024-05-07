
"""
    Considere la lista a continuacion (palabras aleatorias)
    Recorra la lista e indique:

    -> La (o las) palabras con más vocales    
"""

lista = ['hola','pepito','Paralelepido','OrnItorrinCo','AcuEducto','AABCCAABC','holanda','queTal']

pal_max_vocales = []
max_vocales = 0

vocales = 'aeiou'

for palabra in lista:
    cuenta_vocales = 0
    for letra in palabra:
        if (letra.lower() in vocales):
            cuenta_vocales += 1
    print(palabra,'vocales:',cuenta_vocales)

    if (cuenta_vocales == max_vocales):
        pal_max_vocales.append(palabra)

    if (cuenta_vocales > max_vocales):
        max_vocales = cuenta_vocales
        pal_max_vocales = []
        pal_max_vocales.append(palabra)

print('max vocales:',max_vocales)
print(pal_max_vocales)
