class Madre():
    def __init__(self, color: str,**parametros):
        super().__init__(**parametros)
        self.__color = color

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

class Padre():
    def __init__(self, tamanio: int,**parametros):
        super().__init__(**parametros)
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
    
    def __init__(self, deuda = 0, **parametros ):
        super().__init__(**parametros)

        #atributo de instancia propio de Hija
        self.deuda = deuda

class Nieto(Hija):
    pañal = "XL"
    
#objeto
#princesa = Hija("Azul",80)
princesa = Hija(color = "Azul",tamanio = 80,deuda = 350)

print(princesa.tamanio, princesa.color, princesa.deuda)

#ISINSTANCE isinstance(objeto, clase_a_comparar)
print(f"princesa es intancia de Hija: {isinstance(princesa,Hija)}")
print(f"princesa es intancia de Padre: {isinstance(princesa,Padre)}")
print(f"princesa es intancia de Madre: {isinstance(princesa,Madre)}")