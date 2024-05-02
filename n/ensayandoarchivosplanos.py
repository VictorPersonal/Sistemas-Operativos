with open("archivo_texto_plano.txt", "r") as archivo:
    contenido=archivo.read()
    print("contenido actual:\n"+ contenido)

# Solicitar al usuario que ingrese el texto
texto_usuario = input("Ingrese el texto que desea agregar al archivo de texto plano: ")

# Abrir el archivo en modo de añadir ('a')
with open('archivo_texto_plano.txt', 'a') as archivo:
    # Escribir el texto ingresado por el usuario al final del archivo
    archivo.write(texto_usuario + "\n")

print("¡El texto se ha agregado correctamente al archivo de texto plano!")

