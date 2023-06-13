"""
Este es un ejemplo de una clase en Python
Una clase es un constructor 
"""

class Animal :
    def __init__(self,nombre:str,patas:int,ojos:int) -> None:
        self.patas = patas
        self.ojos = ojos
        self.nombre = nombre

    def comer (self,comida:"str") -> None:
        print("Ñom Ñom que rico",comida)

    def decirNombre (self) -> None:
        print("Mi nombre es",self.nombre)

perrito = Animal("Huaquipan",4,1)

perrito.decirNombre()