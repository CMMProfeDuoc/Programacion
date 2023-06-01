lista_animales = ["gatito","perrito","pajarito","canarito","tiranosaurito Rex","koala","koala pero grande","panda","hormiga","otra hormiga","un ornitorrinco","¡¡Perry el ornitorrinco!!","🎵Peeeerry🎵","iguana"]

def getListaAnimales () -> list:
    animales = []
    for a in lista_animales:
        animal = {
            "nombre":a,
            "cantidad":0,
        }
        animales.append(animal)
        return animales
    