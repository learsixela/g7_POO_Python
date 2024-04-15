class Ram():
    def __init__(self,velocidad,bite):
        self.velocidad= velocidad
        self.bite = bite

class DiscoDuro():
    def __init__(self,capacidad):
        self.capacidad=capacidad
        self.__tipo="ssd"

class Teclado():
    def __init__(self,idioma: str,cant_teclas: int ):
        self.idioma = idioma
        self.cant_teclas= cant_teclas

class Mouse():
    def __init__(self,tipo: str,conectividad: str):
        self.tipo = tipo
        self.conectividad = conectividad

class Computador():
    def __init__(self, teclado: Teclado, mouse: Mouse,velocidad_ram: int, capacidad_dd: int):
        #el computador esta compuesta de 
        self.ram = Ram(velocidad_ram,32) #composicion
        self.disco_duro = DiscoDuro(capacidad_dd) #composicion

        self.teclado = teclado #agregacion
        self.mouse = mouse #agregacion

#instancias de clase
teclado = Teclado("latino", 120)
mouse = Mouse("Gamer", "bluetooth")

computador_gamer = Computador(teclado,mouse,2300,500)

print(computador_gamer.ram.velocidad)
print(computador_gamer.teclado.cant_teclas)