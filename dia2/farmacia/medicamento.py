class Medicamento():
    #atributos de clase
    descuento = 0.05
    IVA = 0.18

    @staticmethod
    def validar_mayor_a_cero(numero: int):
        return numero > 0
    
    #los metodos estaticos no pueden modificar los atributos
    @staticmethod
    def modificar_atributo():
        #la clase esta modificando
        Medicamento.IVA = 0.19

        