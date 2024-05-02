class Estudiante():
    def __init__(self, nombre, edad, sexo, nota):
        self.__nombre=nombre
        self.__edad=edad
        self.__sexo=sexo
        self.__nota=nota
    
    def getNombre(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad
    def getSexo(self):
        return self.__sexo
    def getNota(self):
        return self.__nota
    
    def setNombre(self, nombre):
        self.__nombre=nombre
    def setEdad(self, edad):
        self.__edad=edad
    def setSexo(self, sexo):
        self.__sexo=sexo
    def setNota(self, nota):
        self.__nota=nota

listaEstudiantes1 = []
listaEstudiantes2 = []
listaEstudiantes3 = []
contadorF = 0
contadorM = 0

for estudiante in range(8):
    nombre = input("Ingrese el nombre del estudiante: ").lower()
    edad = int(input("Ingrese la edad del estudiante: "))
    sexo = input("Ingrese el sexo. Tenga en cuenta 'M'--> Masculino 'F'--> Femenino: ").lower()
    nota = float(input("Ingrese la nota del alumno: "))
    estudianteGuardadoEnLista = Estudiante(nombre, edad, sexo, nota)
    
    if estudiante <= 4:
        listaEstudiantes1.append(estudianteGuardadoEnLista)
    else:
        listaEstudiantes2.append(estudianteGuardadoEnLista)
    
for estudiante in listaEstudiantes1 + listaEstudiantes2:
    if estudiante.getNota() >= 4.5:
        if estudiante.getSexo() == 'm':
            contadorM += 1
        elif estudiante.getSexo() == 'f':
            contadorF += 1
        listaEstudiantes3.append(estudiante)

print("Estudiantes que lograron tener notas >= 4.5:")
for estudiante in listaEstudiantes3:
    print(estudiante.getNombre())


print("N° de estudiantes con sexo masculino con nota >= 4.5:", contadorM)
print("N° de estudiantes con sexo femenino con nota >= 4.5:", contadorF)





