class Usuario():
    def __init__(self, nombre, cedula, sexo,telefono, edad, email, direccion):
        self.nombre = nombre
        self.cedula = cedula
        self.sexo = sexo
        self.telefono = telefono
        self.edad = edad
        self.email = email
        self.direccion = direccion
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre=nombre
    def getCedula(self):
        return self.cedula
    def setCedula(self, cedula):
        self.cedula=cedula
    def getSexo(self):
        return self.sexo
    def setSexo(self, sexo):
        self.sexo=sexo
    def getTelefono(self):
        return self.telefono
    def setTelefono(self, telefono):
        self.telefono=telefono
    def getEdad(self):
        return self.edad
    def setEdad(self, edad):
        self.edad=edad
    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email=email
    def getDireccion(self):
        return self.direccion
    def setDireccion(self, direccion):
        self.direccion=direccion

