def getNameList (file_name:str="lista_nombres.txt") -> list:
    lista_nombres = []
    file = open(file_name,"r")
    for line in file:
        lista_nombres.append(line)
    return lista_nombres