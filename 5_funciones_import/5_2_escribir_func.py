"""
Escribamos una funcion
"""

def imprimirPalabra (palabra) -> None:
    print(palabra)

"""
La funcion se escribe de la siguiente forma

def <nombre_funcion> (parametros) -> tipo_de_dato_salida :
    codigo
"""

def sumar (a:int,b:int) -> int :
    c = a+b
    return c

"""
Las funciones pueden retornar un tipo de dato especifico
(int) (float) (bool) etc...
Para eso se usa la palabra "return"
Cuando usamos return, la funcion "devuelve" de inmediato el valor
y se termina al instante (como un break)

Tambien, en los parametros podemos especificar que tipo de dato se ingresa usando
la siguiente sintaxis
nombre_variable:tipo_dato
"""