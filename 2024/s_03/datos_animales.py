lista_test = [
    {
        'nombre':'test',
        'tipo':'test',
        'peso':'999',
        'color':'test'
    },
    {
        'nombre':'1',
        'tipo':'2',
        'peso':'3',
        'color':'4'
    }
]

def obtenerDatos (nombre_archivo:str) -> list[dict]:
    archivo = open(nombre_archivo,'r')

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

    return lista_animales

def guardarDatos (lista : list[dict], archivo_objetivo:str) -> None:
    archivo = open(archivo_objetivo,'w')
    
    llaves = lista[0].keys()
    for elemento in llaves:
        archivo.write(str(elemento)+';')
    archivo.write('\n')

    for elemento in lista:
        for valor in elemento.values():
            archivo.write(str(valor)+';')
        archivo.write('\n')

    archivo.close()

