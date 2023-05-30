from gestor_empleados import Gestor_empleados
if __name__ == '__main__':
    gestor_empleados = Gestor_empleados()
    gestor_empleados.registrar_hora()
    gestor_empleados.total_tarea()
    gestor_empleados.calcular_sueldo()