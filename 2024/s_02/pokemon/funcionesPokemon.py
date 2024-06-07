def guardarDatos (pokemon:dict,nombre_archivo:str='datos_pokemon.txt') -> None:
    file = open(nombre_archivo,'w')
    
    file.write(str(pokemon['nombre']) + '\n')
    file.write(str(pokemon['especie']) + '\n')
    file.write(str(pokemon['tipo']) + '\n')
    file.write(str(pokemon['exp']) + '\n')
    file.write(str(pokemon['nivel']) + '\n')
    

    if (pokemon['items'] == []):
        file.write('<no items>\n')
    else:
        for item in pokemon['items']:
            file.write(str(item) + ';')
        file.write('\n')

    for valor in pokemon['attributos'].values():
        file.write(str(valor) + ';')
    file.write('\n')

    for valor in pokemon['stats'].values():
        file.write(str(valor) + ';')
    file.write('\n')

    if (pokemon['ataques'] == []):
        file.write('<no ataques>\n')
    else:
        for item in pokemon['ataques']:
            file.write(str(item) + ';')
        file.write('\n')


    file.close()

def initPokemon (nombre:str, tipo:str,especie:str, nombre_archivo:str) -> dict:
    """
    crea y guarda un pokemon en un archivo
    """
    pokemon = {
        'nombre':nombre,
        'especie':especie,
        'tipo':tipo,
        'items':[],
        'exp':0,
        'nivel':1,
        'attributos':{
                'hambre':0,
                'suenno':0,
                'sed':0,
                'diversion':0,
                'afecto':0,
                },
        'stats':{
                'hp':100,
                'atk':10,
                'def':5,
                },
        'ataques':['placaje']
        }
    guardarDatos(pokemon,nombre_archivo)
    return pokemon

def getPokemon (nombre_archivo:str) -> dict:
    pokemon = {}
    file = open(nombre_archivo,'r')
    pokemon['nombre'] = file.readline().replace('\n','')
    pokemon['especie'] = file.readline().replace('\n','')
    pokemon['tipo'] = file.readline().replace('\n','')
    pokemon['exp'] = file.readline().replace('\n','')
    pokemon['nivel'] = file.readline().replace('\n','')

    items = file.readline().replace('\n','')
    if (items == '<no items>'):
        pokemon['items'] = []
    else:
        pokemon['items'] = items.split(';')

    lista_attr = file.readline().replace('\n','').split(';')
    pokemon['attributos'] = {
        'hp':lista_attr[0]
    }


    file.close()

    return pokemon
    
def saludar (pkm:dict) -> None:
    print('hola soy',pkm['nombre'], 'soy tipo',pkm['tipo'])

