metralleta = {
    "nombre":"Metralleta",
    "tipo":"Gato",
}

guarencin = {
    "nombre":"Guarencin III de Cataluña",
    "tipo":"pajaro",
    "color":"azul"
}

juan = {
    "tipo":"Caballo",
    "nombre":"Juan",
    "debilidad":"Fuego",
}

charqui = {
    "edad":"30",
    "tipo":"Cuy",
    "nombre":"Charquican"
}

lista_mascotas = [metralleta,guarencin,juan,charqui]

for mascota in lista_mascotas:
    print(mascota["edad"]) #si no existe la llave el programa falla

"""
Ejercicio 1
Cree un programa que reciba "mascotas" por parte del usuario,
este ingresa el nombre y la edad
Si ingresa nombre = salir, se detiene el ingreso
Luego, imprima todos los nombres
"""


"""
Ejercicio 2
El usuario ingresa 1 letra,
el programa muestra todas las mascotas con esa letra
"""