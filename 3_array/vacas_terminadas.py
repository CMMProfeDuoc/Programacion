"""
    En un campo hay muchas vacas con nombres distintos.
    El granjero ha registrado todos los nombre de las vacas en una lista.
    Su trabajo es crear un programa que reciba una letra y muestre todos los nombres que tengan esa letra.
    El programa debe mostrar las vacas de forma enumerada, ya que el granjero luego puede seleccionar (usando el numero) una vaca.
    Cuando el granjero selecciona la vaca, sale un mensaje que dice '<nombre de vaca> ha sido seleccionada'
    Este proceso se puede repetir varias veces para crear una lista de las vacas seleccionadas.
    Cuando el granejero ingrese 'salir'. Se muestran todas las vacas seleccionadas y termina el programa.
"""

nombres_vacas = [
    "Juan Daniel",
    "Achraf",
    "Jessica",
    "Bernardo",
    "Rosario",
    "Alexis",
    "Ariana",
    "Sacramento",
    "Patrocinio",
    "Patroclo",
    "Viviana",
    "Aroa",
    "Remedios",
    "Luis",
    "David",
    "Urko",
    "Rosa",
    "Isabel",
    "Gael",
    "Josep",
    "Oriol",
    "Maria",
    "Josefa",
    "Elsa",
]

vacas_filtradas = []
vacas_guardadas = []

while (True):
    letra = input("ingrese letra para busqueda: ")
    if (letra == 'salir'):
        break
    else:
        letra = letra[0].lower()
    
    vacas_filtradas = []
    for nombre in nombres_vacas:
        if (letra in nombre.lower()):
            vacas_filtradas.append(nombre)
        
    for n, v in enumerate(vacas_filtradas):
        print (n+1, v)

    sel = input("sel vaca: (salir) >> ")
    print(sel)
    if (sel.lower() == 'salir'):
        break
    if (sel.isdigit()):
        sel = int(sel)-1
        if (sel in range(len(vacas_filtradas))):
            print("Ha seleccionado a",vacas_filtradas[sel])
            nombres_vacas.pop(nombres_vacas.index(vacas_filtradas[sel]))
            vacas_guardadas.append(vacas_filtradas.pop(sel))
        else:
            print("error de seleccion! ERROR DE RANGO")
            continue
    else:
        print("error de seleccion! NO NUMBER")
        continue

print("VACAS GUARDADAS:")
for i, v in enumerate(vacas_guardadas):
    print(i+1,v)