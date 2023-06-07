pepito = {
    "nombre":"Pepito",
    "edad":4,
    "peso":20,
    "armas":6,
    "tipo":"Gato",
    "HP":1000,
    "genero":"no binario"
}

"""
Ej:
Imprimir datos de pepito de la siguiente forma

<nombre> <edad> <HP> <genero>

el print debe verse asi: print(pepito[llave],end=" ")
"""

lista_llaves = ["nombre","edad","HP","genero"]
for llave in lista_llaves:
    print(pepito[llave],"/",sep=" ",end =" ")

