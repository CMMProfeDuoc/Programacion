helados = ["yogur con cereza","vainilla","soya","arrollao","frutilla","pistacho","ginda","menta","pasta de diente","whisky","chicle","gominola","oreja de chancho"]
nombres = ["pepito","javierito","juanito","canelita","gustava","anacleta"]
cosas_para_pan = ["queso","chancho","mortadela","huevo","huevo","palta","pasta muro","pate","pate de palmera","pate de lentejas","kechu","poroto"]

def imprimirLista (lista:list, nombre_lista:str) -> None:
    print(nombre_lista)
    for elemento in lista:
        print(lista.index(elemento)+1,elemento)

def sumaSimple (a:int, b:int) -> int :
    c = a + b
    return c
#-------------------------------

resultado = sumaSimple(10,23)
print(resultado)