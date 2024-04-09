#import pelota
from pelota import Pelota

#INSTANCIAR o CREAR OBJETO
#pelota_de_andy = pelota.Pelota()
pelota_de_andy = Pelota()

print(pelota_de_andy)#<pelota.Pelota object at 0x104ea9ca0>
print(type(pelota_de_andy))#<class 'pelota.Pelota'>
print(pelota_de_andy.forma)#redondeada
print(pelota_de_andy.material)#
pelota_de_andy.material = "Plastico"
print(pelota_de_andy.material)

pelota_tenis = Pelota()
print(pelota_tenis.material)
pelota_tenis.material = "Caucho"
print("material pelota tenis ",pelota_tenis.material)
print(pelota_tenis.posiciones)

#Métodos estaticos
#no se necesita crear un objeto para invocar al metodo
print(Pelota.crear_rebote)#<function Pelota.crear_rebote at 0x106529580>
print(Pelota.crear_rebote())#[5, 0, 4, 0, 3, 0, 2, 0, 1, 0]

#modificando el valor del atributo por medio de la clase
Pelota.posiciones = [2,4,6]
Pelota.imprimir_posiciones()
print(Pelota.posiciones)
print("")

pelota_futbol = Pelota()
print(pelota_futbol.posiciones)#[2, 4, 6]

#METODOS NO ESTATICOS
pelota_futbol.rebotar()
print(pelota_futbol.posiciones)#[5, 0, 4, 0, 3, 0, 2, 0, 1, 0]

pelota_basket = Pelota()
print(pelota_basket.posiciones)#[2, 4, 6]
#metodo no estatico, permiten crear atributos(variables)
# de tipo "atributo de instancia"
pelota_basket.nuevo_atributo()
print(pelota_basket.color)#blanco
#print(pelota_futbol.color)#AttributeError: 'Pelota' object has no attribute 'color'
