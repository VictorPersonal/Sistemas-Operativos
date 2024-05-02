from Usuario import Usuario

class Empleado(Usuario):
    def __init__(self, nombre, cedula, sexo, telefono, edad, email, direccion, cargo, departamento):
        Usuario.__init__(self, nombre, cedula, sexo, telefono, edad, email, direccion)
        self.cargo=cargo
        self.departamento=departamento
    
    def getCargo(self):
        return self.cargo
    def setCargo(self, cargo):
        self.cargo=cargo
    def getDepartamento(self):
        return self.departamento
    def setDepartamento(self, departamento):
        self.departamento=departamento

