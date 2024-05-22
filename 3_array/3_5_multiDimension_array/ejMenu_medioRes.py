menu = [
    ['cazuela',3000],
    ['sopaipilla',100],
    ['porotos',3000],
]

menu.append(['completo',1000])

#imprimir lista
for i,item in enumerate(menu):
    nombre = item[0]
    precio = item[1]
    print(i+1,'. ',nombre,' $',precio)

# Hacer menu
    # 1. Crear menu para 'seleccionar' item

pedido = []
while (True):
    print("Seleccione Item:")
    print("0 para salir")
    sel = int(input(">> ")) - 1
    if (sel < 0):
        break
    print("Ha seleccionado")
    print(menu[sel])
    pedido.append(menu[sel])
print("Su pedido:")
for item in pedido:
    print(item)
    # 2. Dar opcion para agregar cosas al menu (con verificacion de datos)