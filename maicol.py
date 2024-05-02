from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from tkinter import ttk
import re

def obtener_fecha_nacimiento(): 
    def seleccionarFecha():
        fechaSelect = calendario.selection_get()
        entry_fecha_nacimiento.delete(0, "end")
        entry_fecha_nacimiento.insert(0, fechaSelect.strftime("%d-%m-%Y"))
        ventana_calendario.destroy()

    ventana_calendario = Toplevel(root) 
    ventana_calendario.title("Seleccionar Fecha de Nacimiento")
    calendario = Calendar(ventana_calendario, year=2000, background="darkblue", foreground="white", date_pattern="dd-mm-yyyy")
    calendario.pack(pady=10)

    btnSelect = Button(ventana_calendario, text="Seleccionar", command=seleccionarFecha)
    btnSelect.pack(pady=10)

def Generardatos(event=None):
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    sexo = entry_sexo.get()
    email=entry_email.get()
    fecha_nacimiento= entry_fecha_nacimiento.get()

    if not nombre or not apellido or not edad or not sexo or not email or not fecha_nacimiento:
        messagebox.showerror("Error", "Complete todos los campos")
        return

    ventanaDeLosdatos=Toplevel()
    ventanaDeLosdatos.title("Sus datos")
    ventanaDeLosdatos.geometry("300x300")
    lblFrame=LabelFrame(ventanaDeLosdatos, text="Mira")
    lblFrame.grid(row=0, column=0, padx=10, pady=10)
    lblNombre=Label(lblFrame, text=nombre)
    lblNombre.grid(row=1, column=0, padx=10, pady=10)
    lblApellido=Label(lblFrame, text=apellido)
    lblApellido.grid(row=2, column=0, padx=10, pady=10)
    lblSexo=Label(lblFrame, text=sexo)
    lblSexo.grid(row=3, column=0, padx=10, pady=10)
    lblEmail=Label(lblFrame, text=email)
    lblEmail.grid(row=4, column=0, padx=10, pady=10)
    lblFN=Label(lblFrame, text=fecha_nacimiento)
    lblFN.grid(row=5, column=0, padx=10, pady=10)

def generarFecha(event=None):
    fecha_nacimiento= entry_fecha_nacimiento.get()
    if not re.match(r"^\d{2}-\d{2}-\d{4}$", fecha_nacimiento):
        labelErrorFecha.config(text="El orden de la fecha está mal", fg="red")
    else:
        labelErrorFecha.config(text="")

def Genero(event=None):
    sexo = entry_sexo.get()
    if sexo not in ["H", "M", "Otro"]:
        labelErrorSexo.config(text="Géneros permitidos: H o M u Otro", fg="red")
    else:
        labelErrorSexo.config(text="")

def validar_correo(event=None):
    email = entry_email.get()
    if '@' not in email:
        labelErrorEmail.config(text="Correo inválido", fg="red")
    else:
        labelErrorEmail.config(text="")

def funcionValidadNAE(event=None):
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()

    if nombre or apellido or edad:
        if not nombre.isalpha() or not apellido.isalpha():
            labelErrorNAE.config(text="Nombre y apellido solo deben contener letras", fg="red")
        else:
            labelErrorNAE.config(text="")

        if not edad.isdigit():
            labelErrorEdad.config(text="La edad debe ser un valor numérico", fg="red")
        elif int(edad) < 0:
            labelErrorEdad.config(text="Edad >= 0", fg="red")
        else:
            labelErrorEdad.config(text="")

def habilitarCampos(event=None):
    entry_nombre.config(state="normal")
    entry_apellido.config(state="normal")
    entry_edad.config(state="normal")
    entry_sexo.config(state="normal")
    entry_email.config(state="normal")
    entry_fecha_nacimiento.config(state="normal")
    messagebox.showinfo("Alerta", "Proceda a completarlos.")

root = Tk()
root.title("Formulario")
root.resizable(0,0)
frame = Frame(root)
frame.grid(row=0, column=0)
lblTitulo = LabelFrame(frame, text="Ingrese sus datos básicos")
lblTitulo.grid(row=0, column=0)

label_nombre = Label(frame, text="Nombre*:")
label_nombre.grid(row=0, column=0)
entry_nombre = Entry(frame)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

labelErrorNAE=Label(frame, text="", fg="red")
labelErrorNAE.grid(row=0, column=2, rowspan=2, padx=5)

label_apellido = Label(frame, text="Apellido*:")
label_apellido.grid(row=1, column=0)
entry_apellido = Entry(frame)
entry_apellido.grid(row=1, column=1, padx=10, pady=10)

label_edad = Label(frame, text="Edad*:")
label_edad.grid(row=2, column=0)
entry_edad = Entry(frame)
entry_edad.grid(row=2, column=1, padx=10, pady=10)
labelErrorEdad=Label(frame, text="", fg="red")
labelErrorEdad.grid(row=2, column=2)

label_email = Label(frame, text="E-mail*:")
label_email.grid(row=3, column=0)
entry_email = Entry(frame)
entry_email.grid(row=3, column=1, padx=10, pady=10)
labelErrorEmail= Label(frame, text="", fg="red")
labelErrorEmail.grid(row=3, column=2)

label_sexo = Label(frame, text="Sexo*:")
label_sexo.grid(row=4, column=0)
entry_sexo = ttk.Combobox(frame, values=[ "H", "M", "Otro"])
entry_sexo.grid(row=4, column=1, padx=10, pady=10)
labelErrorSexo=Label(frame, text="", fg="red")
labelErrorSexo.grid(row=4, column=2)

label_fecha_nacimiento = Label(frame, text="Fecha de nacimiento*:")
label_fecha_nacimiento.grid(row=5, column=0, padx=10, pady=10)
entry_fecha_nacimiento = Entry(frame)
entry_fecha_nacimiento.insert(0, "dd-mm-yyyy")
entry_fecha_nacimiento.grid(row=5, column=1, padx=10, pady=10)
btnNacimiento = Button(frame, text="Inserta la fecha", command=obtener_fecha_nacimiento)
btnNacimiento.grid(row=5, column=2, padx=10, pady=10)

labelErrorFecha=Label(frame, text="", fg="red")
labelErrorFecha.grid(row=6, column=1)

entry_nombre.bind('<KeyRelease>', funcionValidadNAE)
entry_apellido.bind('<KeyRelease>', funcionValidadNAE)
entry_edad.bind('<KeyRelease>', funcionValidadNAE)
entry_fecha_nacimiento.bind('<KeyRelease>', generarFecha)
entry_sexo.bind('<KeyRelease>', Genero)
entry_email.bind('<KeyRelease>', validar_correo)

root.bind('<Return>', Generardatos)
root.bind('<Button-3>', habilitarCampos)

root.mainloop()