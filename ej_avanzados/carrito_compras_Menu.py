#no cambiar estas lineas ------------------
import michiHerramientas as Michi
lista_productos = Michi.GetProductList()
#editar de aqui en adelante ---------------

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

def comprarProducto (lista_prod:list,sel:int,cant:int = 1) -> int:
    total_compra = 0
    for i in range(cant):
        if (sel in range(len(lista_prod))):
            if (lista_prod[sel]["cantidad"] > 0):
                lista_prod[sel]["cantidad"] -= 1
                total_compra += lista_prod[sel]["precio"]
            else:
                return total_compra
    return total_compra

def seleccionarProducto (lista_prod:list, sel:int) -> dict:

def buscarProductoNombre (lista_prod:list, nombre_producto:str) -> dict:
    for p in lista_prod:
        if (p["nombre"] == nombre_producto.lower()):
            return p
    return None

def buscarProductKey (lista_prod:list,search_q:str, prod_key:str = "nombre") -> dict:
    for p in lista_prod:
        if (p[prod_key] == search_q):
            return p
    return None

def validateOptionInt (options:list, sel:int) -> bool:
    if (sel in range(len(options))):
        return True
    return False

def validateOption (options:list, sel) -> bool:
    if (sel.isnumeric()):
        if (int(sel) in range(len(options))):
            return True
    return False

#----------------------

menu = ["Mostrar Productos","Buscar Producto","Comprar Producto"]

print("Bienvenido!")

usuario = {
    "nombre":input("Ingrese su nombre: "),
    "productos":[],
    "total_compra":0
}

for i in range(len(menu)):
    print(i+1,menu[i])

while True:
    selec = input("Seleccione una opcion: ")
    if (validateOption(menu,selec)):
        selec = int(selec)-1
        break

if (selec == 0):
    imprimirLista(lista_productos)

if (selec == 1):
    nombre_producto = input("Ingrese el nombre del producto que desea buscar: ")
    prod = buscarProductoNombre(lista_productos,nombre_producto)
    if (prod != None):
        imprimirProductoSimple(prod)

if (selec == 2):
    usuario["total_compra"] += comprarProducto(lista_productos,selec)