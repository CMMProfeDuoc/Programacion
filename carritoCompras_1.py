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

print (lista_productos)