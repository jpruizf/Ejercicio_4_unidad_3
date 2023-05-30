
class Persona(object):
    __dni: str
    __nombre: str
    __direccion: str
    __telefono: int
    def __init__(self,dni,nombre,direccion,telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
    def mostrar_datos(self):
        print("Datos Persona >")
        print("DNI > {0.9d}".format(self.__dni))
        print("Nombre > {}".format(self.__nombre))
        print("Direccion > {}".format(self.__direccion))
        print("Telefono > {}".format(self.__telefono))
    def get_dni(self):
        return self.__dni
    
class Empleado(Persona):
    __fecha_ini: str
    __fecha_fin: str
    def __init__(self,dni,nombre,direccion,telefono,fecha_ini,fecha_fin):
        super().__init__(dni,nombre,direccion,telefono)
        self.__fecha_ini = fecha_ini
        self.__fecha_fin = fecha_fin
    def mostrar_datos(self):
        super().mostrar_datos()
        print("Datos Empleado >")
        print("Fecha_inicio > {}".format(self.__fecha_ini))
        print("Fecha fin del contrato > {}".format(self.__fecha_fin))