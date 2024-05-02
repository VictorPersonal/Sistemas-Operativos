from Usuario import Usuario
from Empleado import Empleado
class Administrador(Usuario):
    def __init__(self, nombre, cedula, sexo, telefono, edad, email, direccion):
        Usuario.__init__(self, nombre, cedula, sexo, telefono, edad, email, direccion)
        
    def agregarEmpleado(self, listaEmpleados):
        nombre=input("Ingrese el nombre del empleado: ")
        cedula=input("Ingrese la cédula del empleado: ")
        sexo=input("Ingrese el sexo del empleado/TENGA EN CUENTA QUE F PARA FEMENINO Y M PARA MASCULINO: ")
        telefono=input("Ingrese el teléfono del empleado: ")
        edad=int(input("Ingrese la edad del empleado: "))
        email=input("Ingrese el email del empleado: ")
        direccion=input("Ingrese la dirección del empleado: ")
        cargo=input("Ingrese el cargo del empleado: ")
        departamento=input("Ingrese el departamento del empleado: ").lower()
        
        empleadoNuevo=Empleado(nombre, cedula, sexo, telefono, edad, email, direccion, cargo, departamento)
        listaEmpleados.append(empleadoNuevo)
        print("Empleado agregado correctamente")



    def eliminarEmpleado(self, listaEmpleados):
        encontrado=None
        cedula=input("Ingrese la cédula del empleado a eliminar: ")
        for empleado in listaEmpleados:
            if cedula == empleado.getCedula():
                encontrado=empleado
                listaEmpleados.remove(empleado)
                print("¡Empleado eliminado exitosamente!")
            else:
                print("El empleado no fue encontrado")


    def calcularPromedio(self, listaEmpleados):
        acumulador=0
        departamento="marketing"
        for empleado in listaEmpleados:
            if departamento == empleado.getDepartamento():
                acumulador+=empleado.getEdad()
        promedio=acumulador/len(listaEmpleados)#Se coloca el promedio por fuera del bucle for para que marque el promedio con todos los empleados que estan dentro de la lista.
        print("Promedio de edad de empleados de la categoría marketing: {}".format(promedio))

    def calcularedadTecnologia(self, listaEmpleados):
        acumulador=0
        acumulador2=0
        departamento="tecnologia"
        for empleado in listaEmpleados:
            if empleado.getEdad() >= 25 and empleado.getEdad() < 45:
                acumulador+=1
            if empleado.getEdad() >= 25 and empleado.getEdad() < 45 and departamento==empleado.getDepartamento():
                acumulador2+=1
        print("Cantidad de empleados con edad entre 25 y 45 años: {}".format(acumulador))
        print("Cantidad de empleados con edad entre 25 y 45 años y del depto. de tecnología: {}".format(acumulador2))
    
    def calcularEdadRecursosHumanos(self, listaEmpleados):
        acumulador=0
        acumulador2=0
        departamento="recursos humanos"
        for empleado in listaEmpleados:
            if empleado.getEdad() >= 40:
                acumulador+=1
            if  empleado.getEdad() >= 40 and empleado.getDepartamento()==departamento:
                acumulador2+=1
        print("Cantidad de empleados con edad mayor a 40 años: {}".format(acumulador))
        print("Cantidad de empleados con edad mayor a 40 años y del depto. de recursos humanos: {}".format(acumulador2))

