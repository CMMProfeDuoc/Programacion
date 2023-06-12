helados = []

salsa = {
    "nombre":"choco",
    "precio":10
}
agregados = [salsa]

lista_helados = ["vanilla","chocolate","frutilla","frambuesa","platano"]
lista_precios = [123,443]

for i in range(len(lista_helados)):

    if (i >= len(lista_precios)):
        precio = 200
    else:
        precio = lista_precios[i]

    h_dict = {
        "nombre":lista_helados[i],
        "precio":precio
    }
    helados.append(h_dict)

