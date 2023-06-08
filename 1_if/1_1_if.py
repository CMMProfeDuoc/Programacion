"""
La sentencia IF permite "preguntar" cosas
funciona analizando lo que este dentro del if y dividiendo el flujo de acciones segun la respuesta

if (<sentencia_logica>) :
    TRUE
FALSE
"""

#ejemplo de programa que analiza si un numero es mayor que 10

numero = int(input("Ingrese un numero: "))

if (numero > 10):
    print("El numero es mayor que 10")


#Ahora, modifique el programa para que "detecte" numeros positivos solamente