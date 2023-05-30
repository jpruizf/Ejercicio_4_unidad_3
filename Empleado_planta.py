from Clase_empleado import Empleado

class Emp_Planta(Empleado):
    __sueldo_basico: int
    __antiguedad: int
    def __init__(self,sueldo_basico,antiguedad,dni,nombre,direccion,telefono,fecha_ini,fecha_fin):
        super().__init__(dni,nombre,direccion,telefono,fecha_ini,fecha_fin)
        self.__sueldo_basico = sueldo_basico
        self.__antiguedad = antiguedad
    def mostrar_datos(self):
        super().mostrar_datos()
        print("< Datos Emplado Planta Permanente >")
        print("Sueldo basico = ${}".format(self.__sueldo_basico))
        print("Antiguedad > {}".format(self.__antiguedad))
    def get_sueldo_basico(self):
        return self.__sueldo_basico
    def get_antiguedad(self):
        return self.__antiguedad