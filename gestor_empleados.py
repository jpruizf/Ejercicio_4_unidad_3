from Empleado_contratado import Emp_Contratado
from Empleado_externo import Emp_Externo
from Empleado_planta import Emp_Planta
from Clase_empleado import Empleado

class Gestor_empleados:
    __empleados: list
    __total_pago: float
    __ayuda_eco: list
    __empleado_cont: object
    __empleado_ext: object
    __empleado_pla: object
    def __init__(self):
        self.__empleados = []
        self.__total_pago = 0
        self.__ayuda_eco = []
    def setEmp_Contratado(self,un_empleado):
        self.__empleados.append(un_empleado)
    def registrar_hora(self):
        aux_dni = input("Ingrese un dni > ")
        empleado_encontrado = self.buscar(aux_dni)
        if empleado_encontrado:
            for empleado  in empleado_encontrado:
                if isinstance(empleado,Emp_Contratado):
                    empleado.registrar_horas()
                elif isinstance(empleado,Emp_Externo):
                    empleado.registrar_horas()
    def buscar(self,aux_dni):
        empleados_encontrados = []
        bandera = False
        for empleado in self.__empleados:
            if empleado.get_dni() == aux_dni:
                empleados_encontrados.append(empleado)
                bandera = True
        if not bandera:
            print("ERROR Inesperado :/")
        return empleados_encontrados
    def total_tarea(self):
        tarea = input("Ingrese una tarea >> ")
        for empleado in self.__empleados:
            if isinstance(empleado,Emp_Externo):
                if empleado.get_tarea() == tarea:
                    self.__total_pago =+ int(empleado.get_monto_viatico()) - int(empleado.get_monto_seguro())
                    empleado.mostrar_datos()
        print(self.__total_pago)
    def calcular_sueldo(self):
        total_emp_contratado = 0
        total_emp_planta = 0
        for empleado in self.__empleados:
            if isinstance(empleado,Emp_Contratado):
                total_emp_contratado += int(empleado.get_cantidad_horas) * int(empleado.get_valor_horas)
            elif isinstance(empleado,Emp_Planta):
                total_emp_planta += int(empleado.get_sueldo_basico()) + int(0.10 + empleado.get_sueldo_basico()) * int(empleado.get_antiguedad)
        print("Sueldos de los empleados >> Empleados contratados {} | Empleados en planta {} | Empleados externos {}".format(total_emp_contratado,total_emp_planta,self.__total_pago))
        self.ayuda_economica(total_emp_contratado,total_emp_planta)
    def ayuda_economica(self,sueldo_contratado,sueldo_planta):
        for empleado in self.__empleados:
            if sueldo_contratado < 150000 or sueldo_planta < 150000:
                self.__ayuda_eco.append(empleado)
        return self.__ayuda_eco
    def mostrar_ayuda(self):
        for empleado in self.__ayuda_eco:
            if isinstance(empleado,Empleado):
                empleado.mostrar_datos()
