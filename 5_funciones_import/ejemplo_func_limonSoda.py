def imprimirLista (lista_cosas:list, nombre_lista:str) -> None:
    print('Imprimiendo',nombre_lista)
    for i,cosa in enumerate(lista_cosas):
        print(i,cosa)

def palabraLarga (lista_palabras:list) -> str:
    lenMaxPalabra = 0
    palabraMax = ''
    for palabra in lista_palabras:
        if (len(palabra) > lenMaxPalabra):
            palabraMax = palabra
            lenMaxPalabra = len(palabra)
    return palabraMax

    

lista_comida = [
    'churrasco','sopaipilla','mcDondald','choripan'
]

lista_desayuno = [
    'te','cafe','pan'
]

lista_bebidas = [
    'cocacola','pepsi','fanta','limon soda lo mejor','pap'
]

palabraMasLarga = palabraLarga(lista_bebidas)

print(palabraMasLarga)
