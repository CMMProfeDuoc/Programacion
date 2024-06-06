opciones_menu = {

    'salir'         : ['salir', 's'],
    'ver_animales'  : ['ver','v','mostrar'],
    'filtrar'       : ['f','filtro'],
    'agregar'       : ['a','agregar'],
    'ver_guardados' : ['g','ver_guardados','guardados'],
    'modificar'     : ['m','modificar']
}

def extraerDatos (nombre_archivo:str) -> list[dict]:
    lista_animales = []

    file = open(nombre_archivo,'r')
    lista_llaves = file.readline().replace('\n','').split(';')

    for linea in file.readlines():
        datos_mascota = linea.replace('\n','').split(';')
        
        mascota = {}
        for i in range(len(lista_llaves)):
            mascota[lista_llaves[i]] = datos_mascota[i]

        lista_animales.append(mascota)

    file.close()
    return lista_animales

def guardarDatos (archivo:str,lista_datos:list[dict],encabezado:list[str]) -> None:
    file = open(archivo,'w')
    
    for llave in encabezado:
        file.write(llave+';')
    file.write('\n')

    for elemento in lista_datos:
        for dato in elemento.values():
            file.write(dato+';')
        file.write('\n')

    file.close()
