"""
Cree un programa de heladeria
El programa tiene una lista de helados
Cada helado tiene:
nombre, precio

Además existe una lista de agregados
cada agregado tiene
nombre, precio

HELADOS Y AGREGADOS INVENTADOS POR USUARIO

El programa preguntara al usuario que sabor de helado quiere,
luego, si quiere agregar otro (u otros) sabores
Despues, preguntara para añadir los agregados

El programa guardara cada pedido en una lista
Preguntara por más de un helado
"""
import listaHelados

def imprimir_lista (nombre_lista:str,lista:list) -> None :
    print("---",nombre_lista,"---")
    for element in lista:
        print(element["nombre"]," $",element["precio"])

def verificarSeleccion (sel:str,lista:list) -> bool:
    for element in lista:
        if (sel == element["nombre"]):
            return True
    return False

helados = listaHelados.helados
agregados = listaHelados.agregados

while (True):
    #seleccionar helados
    imprimir_lista("Helados",helados)
    sel = input("Seleccione Helado: ")
    if (verificarSeleccion(sel,helados)):
        print("Seleccion Valid")

    #seleccionar agregados
    imprimir_lista("Agregados",agregados)
    sel = input("Seleccion Agregado")
    if (verificarSeleccion(sel,agregados)):
        print("Agregado valido")

    #preguntar si quiere repetir ?
    salir = input("Quiere salir?")
    if (salir == "si"):
        break