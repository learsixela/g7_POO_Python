class Madre():
    def __init__(self, color: str):
        self.__color = color

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

class Padre():
    def __init__(self, tamanio: int):
        self.__tamanio = tamanio

    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio: int):
        self.__tamanio = tamanio

class Hija(Madre,Padre):
    """ sobreescritura de los constructores"""
    #def __init__(self, color: str, tamanio: int ):
    #    Madre.__init__(self,color)
    #    Padre.__init__(self,tamanio)


#objeto
princesa = Hija("Azul",80)

print(princesa.tamanio, princesa.color)