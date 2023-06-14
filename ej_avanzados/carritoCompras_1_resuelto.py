"""
Cree un carrito de compras online
para esto usted debe registrar los siguientes datos de un usuario

string nombre
lista <string> productos
int precio_total

Su programa debe mostrar al usuario la lista de productos (entregada a usted como "lista_productos")
La lista_productos contiene diccionarios que tiene las siguientes llaves:
nombre
precio
cantidad
peso
ingredientes <- este es una lista

El usuario puede seleccionar todos los productos que desee, luego se
mostrara el precio final
"""

#no cambiar estas lineas ------------------
import michiHerramientas as Michi
lista_productos = Michi.GetProductList()
#editar de aqui en adelante ---------------

lista_productos2 = Michi.GetProductList("productos2.csv")

#funcion para imprimir la lista de forma ordenada
#Michi.printDict(lista_productos)

def imprimirProductoSimple (producto:dict) -> None:
    print(producto["nombre"]," $",producto["precio"])

def imprirProductosCantidad (producto:dict) -> None:
    print(producto["nombre"]," cant:",producto["precio"])

def imprimirLista (lista_prod:list, tipo_print:str="simple") -> None:
    for producto in lista_prod:
        print(lista_prod.index(producto)+1,end=". ")
        if (tipo_print == "simple"):
            imprimirProductoSimple(producto)
        if (tipo_print == "cantidad"):
            imprirProductosCantidad(producto)

def comprarProducto (producto:dict, cantidad:int=1) -> int:
    total_compra = 0
    for i in range(cantidad):
        #print("DEBUG:",producto["cantidad"])
        if (producto["cantidad"] > 0):
            print("Se ha comprado 1",producto["nombre"])
            producto["cantidad"] -= 1
            total_compra += producto["precio"]
        else:
            print("No quedan",producto["nombre"])
    return total_compra

#-------------------------------------------

print("Bienvenido")

total_cliente = 0
while(True):
    imprimirLista(lista_productos,"simple")

    sel = int(input(">> "))-1 #verificar ingreso correcto

    total_cliente += comprarProducto(lista_productos[sel])
    print("Su total es:",total_cliente)

    salir = input("Quiere comprar otro producto? <s> <n>")
    if (salir.lower() == "n"):
        break

    