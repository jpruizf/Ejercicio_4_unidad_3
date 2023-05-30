from Clase_empleado import Empleado

class Emp_Externo(Empleado):
    __tarea: str
    __monto_viatico: int
    __costo_obra: int
    __monto_seguro: int
    def __init__(self,tarea,monto_viatico,costo_obra,monto_seguro,dni,nombre,direccion,telefono,fecha_ini,fecha_fin):
        super().__init__(dni,nombre,direccion,telefono,fecha_ini,fecha_fin)
        self.__tarea = tarea
        self.__monto_viatico = monto_viatico
        self.__costo_obra = costo_obra
        self.__monto_seguro = monto_seguro
    def mostrar_datos(self):
        super().mostrar_datos()
        print("< Datos Empleados externos >")
        print("Tarea > {}".format(self.__tarea))
        print("Monto del viatico > ${}".format(self.__monto_viatico))
        print("Costo de la obra > ${}".format(self.__costo_obra))
        print("Monto del seguro de vida >{}".format(self.__monto_seguro))
    def registrar_horas(self):
        aux_horas = int(input("Ingrese cantidad de horas trabajadas > "))
        return aux_horas
    def get_tarea(self):
        return self.__tarea
    def get_monto_viatico(self):
        return self.__monto_viatico
    def get_monto_seguro(self):
        return self.__monto_seguro
