import tkinter as tk

class ContadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador App")

        self.contador = 0

        # Etiqueta para mostrar el contador
        self.label_contador = tk.Label(root, text="Contador: 0")
        self.label_contador.pack(pady=10)

        # Botón para incrementar el contador
        self.boton_incrementar = tk.Button(root, text="Incrementar", command=self.incrementar_contador)
        self.boton_incrementar.pack()

    def incrementar_contador(self):
        # Incrementa el contador y actualiza la etiqueta
        self.contador += 1
        self.label_contador.config(text=f"Contador: {self.contador}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContadorApp(root)
    root.mainloop()

