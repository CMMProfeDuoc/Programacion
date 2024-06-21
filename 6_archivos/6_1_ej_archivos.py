"""
Cree un programa que tenga lo siguiente:
Una funcion que abra un archivo y cuente cada letra del archivo y la guarde en un diccionario
El archivo es un .txt

Luego, replique esta funcion para varios archivos en la carpeta.
"""

def contarLetras (nombre_archivo:str) -> dict:
    frec_letras = {}
    archivo = open(nombre_archivo, 'r')

    for letra in archivo.read():
        if letra in frec_letras.keys():
            frec_letras[letra] += 1
        else:
            frec_letras[letra] = 1

    archivo.close()
    return frec_letras

import os

lista_archivos = os.listdir('.')
#os.listdir('.') -> entrega la lista de todos los archivos de la carpeta actual
for archivo in lista_archivos:
    if ('.txt' in archivo):
        print(archivo, ': ')
        print(contarLetras(archivo))
        print()
