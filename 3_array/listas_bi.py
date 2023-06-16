"""
Podemos tener listas de listas, con esto podemos ordenar mejor los datos.
Dado que las listas contienen cualquier tipo de dato, podemos crear
una lista que contenga los datos que queramos

En este caso las liastas contienen
["nombre",edad,km_recorridos,estado_licencia] -> [str, int, int, bool]
"""

choferes = [["Panchito",35,600,True],["Karol",43,1302,True]]

#Podemos insertar elementos a la lista de la siguiente forma
choferes.append(["Andre",40,1000,True])
choferes.append(["Juanito",56,1200,True])
choferes.append(["Huaiquipan",45,1300,False])
choferes.append(["Tolosa",38,1000,True])

#para imprimir la lista podemos hacer lo siguiente
for i in range(len(choferes)):
    print(choferes[i])

#esto imprime todos los datos
#si queremos imprimir solo 1 datos de nuestras listas más pequeñas 
#Por ejemplo, solo el nombre

for i in range(len(choferes)):
    print(choferes[i][0])
    #esto es porque en nuestras listas dentro de la lista,
    #el dato [0] corresponde al nombre

"""
Ahora haga lo siguiente:
1. Imprima todos los choferes con los siguientes datos:
nombre, edad, estado_licencia

2. Busque a un chofer por su nombre
"""