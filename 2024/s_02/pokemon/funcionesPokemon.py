def guardarDatos (pokemon:dict,nombre_archivo:str='datos_pokemon.txt') -> None:
    file = open(nombre_archivo,'w')
    
    file.write(pokemon['nombre'] + '\n')
    file.write(pokemon['tipo'] + '\n')

    if (pokemon['items'] == []):
        file.write('<no items>\n')
    else:
        for item in pokemon['items']:
            file.write(str(item) + ';')
        file.write('\n')

    for valor in pokemon['attributos'].values():
        file.write(str(valor) + ';')
    #file.write('\n')

    file.close()

def initPokemon (nombre:str, tipo:str, nombre_archivo:str) -> dict:
    """
    crea y guarda un pokemon en un archivo
    """
    pokemon = {
        'nombre':nombre,
        'tipo':tipo,
        'items':[],
        'attributos':
            {
            'hambre':0,
            'suenno':0,
            'sed':0,
            'diversion':0,
            'afecto':0,
            },
        }
    guardarDatos(pokemon,nombre_archivo)
    return pokemon

def saludar (pkm:dict) -> None:
    print('hola soy',pkm['nombre'], 'soy tipo',pkm['tipo'])

