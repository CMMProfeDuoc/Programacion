lista_prueba = [
    {
        'nombre': 'pepito',
        'tipo' : 'gato',
        'peso' : 7.2, 
        'color' : 'naranjo',
    },
    {
        'nombre': 'jaimico',
        'tipo' : 'mandril',
        'peso' : 20.2, 
        'color' : 'plomo',
    },
]

def extraerDatosAnimales (nombre_archivo:str) -> list[dict]:
    lista_datos_animales = []

    archivo = open(nombre_archivo,'r')

    lista_llaves = archivo.readline().replace('\n','').split(';')

    lista_animales = archivo.readlines()

    for animal in lista_animales:
        datos_animal = animal.replace('\n','').split(';')
        dict_animal = {
            'nombre':datos_animal[0],
            'tipo':datos_animal[1],
            'peso':datos_animal[2],
            'color':datos_animal[3],
        }
        lista_datos_animales.append(dict_animal)

    archivo.close()
    return lista_datos_animales

def guardarDatosAnimales (lista_animales:list[dict] ,nombre_archivo:str) -> None:
    archivo = open(nombre_archivo,'w')

    archivo.write('nombre;tipo;peso;color\n')

    for animal in lista_animales:
        for dato in animal.values():
            archivo.write(str(dato)+';')
        archivo.write('\n')

    archivo.close() 
