def getList (file_name:str) -> list:
    lista_nombres = []
    file = open(file_name,"r")
    for line in file:
        lista_nombres.append(line.strip())
    file.close()
    return lista_nombres

def generateNameFile () -> None:
    pass