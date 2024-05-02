from Producto import Producto

class Main():
    Lacteos = []
    Verduras = []
    Granos = []
    Aseo = []
    
    for i in range(12):
        nombreP = input("Ingrese el nombre del producto: ").lower()
        categoria = input("Ingrese la categoria: ").lower()
        precioN = int(input("Ingrese el precio neto(INT): "))
        precioTotal = int(input("Ingrese precio total(INT): "))
        iva = float(input("Ingrese el iva(float): "))
        
        if categoria == "lacteos":
            lacteosA = Producto(nombreP, categoria, precioN, precioTotal, iva)
            Lacteos.append(lacteosA)
            print("Se guardo correctamente a la lista de los lacteos")

        elif categoria == "verduras":
            verdurasA = Producto(nombreP, categoria, precioN, precioTotal, iva)
            Verduras.append(verdurasA)
            print("Se guardo correctamente a la lista de las verduras")

        elif categoria == "aseo":
            aseosA = Producto(nombreP, categoria, precioN, precioTotal, iva)
            Aseo.append(aseosA)
            print("Se guardo correctamente a la lista de los productos de aseo")

        elif categoria == "granos":
            granosA = Producto(nombreP, categoria, precioN, precioTotal, iva)
            Granos.append(granosA)
            print("Se guardo correctamente a la lista de los granos")

    # Luego de completar la entrada de productos, realizas los cálculos
    if "lacteosA" in locals():
        lacteosA.CalcularAcumuladoPNLacteos(Lacteos)
    if "granosA" in locals():
        granosA.CalcularAcumuladoPTGranos(Granos)
    if "verdurasA" in locals():
        verdurasA.CalcularPromedioPNVedrduras(Verduras)
    if "aseosA" in locals():
        aseosA.CalcularPromedioPTPAseo(Aseo)
