from Usuario import Usuario
from Administrador import Administrador
class Main():
    def main():
        admin = Administrador("Andres", "11123904555", "M", "3124657888", "22", "andres@gmail.com","Cra 14")
        listaEmpleados=[]
        opcion=999
        while(opcion!=0):
            opcion=int(input("\nIngrese una opción: \n1. Agregar empleado.\n2. Eliminar empleado\n3. Calcular el promedio de edad de todos los empleados del dpto. de ventas y marketing.\n4. Obtener cuántos empleados tienen una edad >= 25 años y <= 45 y son del dpto. de tecnología.\n5. Obtener cuántos empleados tienen una edad >= 40 y son del departamento de recursos humanos.\n-->"))
            if(opcion==1):
                admin.agregarEmpleado(listaEmpleados)
            elif(opcion==2):
                admin.eliminarEmpleado(listaEmpleados)
            elif(opcion==3):
                admin.calcularPromedio(listaEmpleados)
            elif(opcion==4):
                admin.calcularedadTecnologia(listaEmpleados)        
            elif(opcion==5):
                admin.calcularEdadRecursosHumanos(listaEmpleados)
    main()

