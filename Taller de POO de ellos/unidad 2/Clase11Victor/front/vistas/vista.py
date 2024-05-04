from tkinter import *
from controladores.controlador import Validaciones
from modelos.usuario import Usuario
import re

class Interfaz():
    def mostrar_interfaz():
        
    
        def eventoVnombre(event):
            global nombre
            if Validaciones.validarNombre(usuario.nombre):
                textoVnombre=""
            else:
                textoVnombre="Nombre debe tener solo letras"
            labelErrorNombre.config(text=textoVnombre)

        def eventoVApellido(event):
            global apellido
            if Validaciones.validarApellido(usuario.apellido):
                textoVapellido=""
            else:
                textoVapellido="Apellido debe tener solo letras"
            labelErrorApellido.config(text=textoVapellido)

        def eventoVEstatura(event):
            global estatura
            valor_estatura = txtAtr3.get() 
            if Validaciones.validarEstatura(usuario.estatura):
                textoVEstatura=""
            else:
                textoVEstatura="Estatura no cumple con lo establesido"
            lblErrorEstatura.config(text=textoVEstatura)

        def eventoVPeso(event):
            global peso
            valorPeso = txtAtr4.get() 
            if Validaciones.validarPeso(usuario.peso):
                textoVpeso=""
            else:
                textoVpeso="Peso no cumple con lo establesido"
            lblErrorPeso.config(text=textoVpeso)

        
        root=Tk()
        root.title("Clase persona")
        root.resizable(0,0)
        usuario=Usuario(root)

        marcotitulo=LabelFrame(root)
        marcotitulo.grid(row=0, column=1, padx=5, pady=5)

        lblTitulo=Label(marcotitulo, text="Clase-Persona")
        lblTitulo.grid(row=0, column=0, padx=10, pady=10)

        marcoAtr1=LabelFrame(root)
        marcoAtr1.grid(row=1, column=0, padx=5, pady=5)

        lblAtr1=Label(marcoAtr1, text="Ingrese el 1er atributo de Cl/Persona(Nombre)*\nTenga en cuenta que solo son letras, sin caracteres especiales o números:")
        lblAtr1.grid(row=0, column=0)
        txtAtr1=Entry(marcoAtr1, textvariable=usuario.nombre)
        txtAtr1.grid(row=0,column=1, padx=10, pady=10)
        labelErrorNombre=Label(marcoAtr1, text="", fg="red")
        labelErrorNombre.grid(row=1, column=1)

        marcoAtr2=LabelFrame(root)
        marcoAtr2.grid(row=2, column=0, padx=5, pady=5)

        lblAtr2=Label(marcoAtr2, text="Ingrese el 2do atributo de Cl/Persona(Apellido)*\nTenga en cuenta que solo son letras, sin caracteres especiales o números:")
        lblAtr2.grid(row=0,column=0)
        txtAtr2=Entry(marcoAtr2, textvariable=usuario.apellido)
        txtAtr2.grid(row=0, column=1, padx=10, pady=10)
        labelErrorApellido=Label(marcoAtr2, text="", fg="red")
        labelErrorApellido.grid(row=1, column=1)

        marcoAtr3=LabelFrame(root)
        marcoAtr3.grid(row=1, column=2, padx=5, pady=5)

        lblAtr3=Label(marcoAtr3, text="Ingrese el 3er atributo de Cl/Persona(Estatura(metros)/Decimal)\nTenga en cuenta esta forma de inserción\nd--> dígito; 1d unico antes del punto y max 2d después de este:")
        lblAtr3.grid(row=0,column=0)
        txtAtr3=Entry(marcoAtr3, textvariable=usuario.estatura)
        txtAtr3.grid(row=0, column=1, padx=10, pady=10)
        lblErrorEstatura=Label(marcoAtr3, text="", fg="red")
        lblErrorEstatura.grid(row=1, column=1)

        marcoAtr4=LabelFrame(root)
        marcoAtr4.grid(row=2,column=2, padx=5, pady=5)

        lblAtr4=Label(marcoAtr4, text="Ingrese el 4to atributo de Cl/Persona(Peso(Kg)/Decimal)*\nTenga en cuenta esta forma de inserción\nd--> dígito max 3d antes del . y max 2d después de este:")
        lblAtr4.grid(row=0,column=0)
        txtAtr4=Entry(marcoAtr4, textvariable=usuario.peso)
        txtAtr4.grid(row=0, column=1, padx=10, pady=10)
        lblErrorPeso=Label(marcoAtr4, text="", fg="red")
        lblErrorPeso.grid(row=1, column=1)
        btnGuardar=Button(root, text="Guardar", padx=10, pady=10, command=Validaciones.validarInformacion)
        btnGuardar.grid(row=3, column=1, padx=10, pady=10)

        txtAtr1.bind("<KeyRelease>", eventoVnombre)
        txtAtr2.bind("<KeyRelease>", eventoVApellido)
        txtAtr3.bind("<KeyRelease>", eventoVEstatura)
        txtAtr4.bind("<KeyRelease>", eventoVPeso)
        root.mainloop()
