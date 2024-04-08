from medicamento import Medicamento

#instancia de la clase o creacion de un objeto
paracetamol  = Medicamento()
aspirina = Medicamento()

print(paracetamol.descuento)
print(aspirina.descuento)

paracetamol.descuento = 0.06

print(paracetamol.descuento)
print(aspirina.descuento)