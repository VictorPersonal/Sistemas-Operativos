import re
from tkinter import *
from modelos.usuario import Usuario
import requests
from tkinter import messagebox
class Validaciones():

    
    def __init__(self):
        pass
    def validarNombre(valor):
        patronN = re.compile("^[A-Za-zñÑ ]*$")
        resultadoN = patronN.match(valor.get()) is not None
        if not resultadoN:
            return False
        return True
    
    def validarApellido(valorApellido):
        patronA = re.compile("^[A-Za-zñÑ ]*$")
        resultadoN = patronA.match(valorApellido.get()) is not None
        if not resultadoN:
            return False
        return True
    
    def validarEstatura(valor):
        patronA = re.compile(r"^\d{1}(\.\d{0,2})?$")
        resultadoN = patronA.match(valor.get()) is not None
        if not resultadoN:
            return False
        return True
    

    def validarPeso(valor):
        patronA = re.compile(r"^\d{1,3}(\.\d{0,2})?$")
        resultadoN = patronA.match(valor.get()) is not None
        if not resultadoN:
            return False
        return True
    

    def validarInformacion():
        root=Tk()
        usuario=Usuario(root)
        nombreV = re.match(r"^[A-Za-zñÑ ]*$", usuario.nombre.get())
        apellidoV = re.match(r"^[A-Za-zñÑ ]*$", usuario.apellido.get())
        estaturaV = re.match(r"^\d{1}(\.\d{0,2})?$", usuario.estatura.get())
        pesoV = re.match(r"^\d{1,3}(\.\d{0,2})?$", usuario.peso.get())


        if nombreV and apellidoV and estaturaV and pesoV:
            
            data = {
                "nombre": usuario.nombre.get(),
                "apellido": usuario.apellido.get(),
                "estatura": usuario.estatura.get(),
                "peso": usuario.peso.get()
            }
            respuesta = requests.post("http://127.0.0.1:8000/v1/persona", data)
            print(respuesta.status_code)
            print(respuesta.content)
            
            messagebox.showinfo("Informacion", "Se guardo correctamente")
        else:
            messagebox.showerror("Informacion", "No se pudo guardar, confirme si está correcto")