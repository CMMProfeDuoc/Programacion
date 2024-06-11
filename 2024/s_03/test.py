
archivo = open('datos_animales.csv','r')

lista_animales = []

llaves = archivo.readline().replace('\n','').split(';')

datos = archivo.readlines()
for linea in datos:
    animal = linea.replace('\n','').split(';')
    dict_animal = {
        llaves[0] : animal[0],
        llaves[1] : animal[1],
        llaves[2] : animal[2],
        llaves[3] : animal[3],
    }
    lista_animales.append(dict_animal)

archivo.close()

for cosa in lista_animales:
    print(cosa)