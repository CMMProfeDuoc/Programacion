vacas_filtradas = []

busqueda = input("ingrese letras para busqueda: ").lower()

for letra in busqueda:
    print("Buscando para:",letra)
    i = 0
    while (len(nombres_vacas) > 0):
        #print(i, nombres_vacas[i])
        if (letra in nombres_vacas[i].lower()):
            vacas_filtradas.append(nombres_vacas.pop(i))
            continue
        i += 1
        if (i > len(nombres_vacas)-1):
            break

print(vacas_filtradas)

# Mostra Vacas enumeradas
# Poder selecciona vacas y colocar a nueva lista <- MENU
# Poder salir al escribir 'salir'
# Mostrar vacas seleccionadas
