"""
    Crear un sistema que permita el ingreso de varios
    usuarios
    Luego mostrar los usuarios por pantalla

    usuario tiene los sig atributos:
    nombre, apellido, edad, id, direccion, 
"""
default_dict = {
    'nombre':'NN',
    'apellido':'NN',
    'id':-1,
}
lista_usuarios = []

while (True):
    temp_dict = default_dict.copy()

    temp_dict.update({
            'id':str(len(lista_usuarios)+1)
    })

    lista_usuarios.append(temp_dict.copy())

    if (input('salir? ')=='s'):
        break

for user in lista_usuarios:
    print(user['id'],'=>',user['nombre'])