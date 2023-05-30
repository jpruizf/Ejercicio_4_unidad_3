from Clase_empleado import Empleado

class Emp_Contratado(Empleado):
    __cant_horas: int
    __valor_horas: int
    def __init__(self,cant_horas,valor_horas,fecha_ini,fecha_fin,dni,nombre,direccion,telefono):
        super().__init__(dni,nombre,direccion,telefono,fecha_ini,fecha_fin)
        self.__cant_horas = cant_horas
        self.__valor_horas = valor_horas
    def mostrar_datos(self):
        super().mostrar_datos()
        print("< Datos Empleados Contratados >")
        print("Cantidad horas > {}".format(self.__cant_horas))
        print("Valor de las horas > ${}".format(self.__valor_horas))
    def registrar_horas(self):
        aux_horas = int(input("Ingrese cantidad de horas trabajadas > "))
        return aux_horas
    def get_cantidad_horas(self):
        return self.__cant_horas
    def get_valor_horas(self):
        return self.__valor_horas