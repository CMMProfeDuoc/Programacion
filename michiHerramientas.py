def PauseAndClean () -> None:
    from os import system
    system("pause")
    system("cls")

def GetProductList() -> list:
    lista = []
    file = open("productos.csv","r")
    for count,line in enumerate(file):
        if (count == 0):
            continue
        line = line.strip()
        aux_str = line.split(";")
        producto = {
            "nombre":aux_str[0],
            "precio":aux_str[1],
            "peso":aux_str[2],
            "cantidad":aux_str[3],
            "ingredientes":aux_str[4].split(",")
        }
        lista.append(producto)
    file.close()
    return lista

def GetUserList () -> list:
    lista = []
    file = open("users.csv","r")
    for count,line in enumerate(file):
        if (count == 0):
            continue
        line = line.strip()
        aux_str = line.split(";")
        producto = {
            "nombre":aux_str[0],
            "contraseña":aux_str[1],
        }
        lista.append(producto)
    file.close()
    return lista

def chekNumericInput (sel,max:int,min:int = 0) -> bool :
    if (sel.isnumeric()):
        if (int(sel) in range(min,max+1)):
            return True
    return False

def checkInput (sel:str,opciones:list) -> bool:
    if (sel in opciones):
        return True
    return False

def setMatrix (x_:int, y_:int, object=0) -> list :
    rows = [object] * x_
    matrix = [rows] * y_
    return matrix

def drawMatrix (matrix:list) -> None :
    pass
    