class Producto():

    def __init__(self, nombre, categoria, precioNeto, precioTotal, iva):
        self.__nombre=nombre
        self.__categoria=categoria
        self.__precioNeto=precioNeto
        self.__precioTotal=precioTotal
        self.__iva=iva

    def getNombre(self):
        return self.__nombre
    def getCategoria(self):
        return self.__categoria
    def getPrecioNeto(self):
        return self.__precioNeto
    def getPrecioTotal(self):
        return self.__precioTotal
    def getIva(self):
        return self.__iva
    
    def setNombre(self, nombre):
        self.__nombre=nombre
    def setCategoria(self, categoria):
        self.__categoria=categoria
    def setPrecioNeto(self, precioNeto):
        self.__precioNeto=precioNeto
    def setPrecioTotal(self, precioTotal):
        self.__precioTotal=precioTotal
    def setIva(self, iva):
        self.__iva=iva

    def CalcularAcumuladoPTGranos(self, Granos):
        categoria="granos"
        acumulado=0
        for producto in Granos:
            if producto.getCategoria() ==categoria:
                acumulado+= producto.getPrecioTotal()

        print("El acumulado del precio total de la categoria granos corresponde a: {}".format(acumulado))


    def CalcularAcumuladoPNLacteos(self, Lacteos):
        categoria="lacteos"
        acumulado=0
        for producto in Lacteos:
            if producto.getCategoria() == categoria:
                acumulado+= producto.getPrecioNeto()
                if acumulado > 13000:
                    print("El acumulado de la categoria lacteos categoria = {}".format(acumulado))

                else:
                    pass

    def CalcularPromedioPNVedrduras(self, Verduras):
        categoria="verduras"
        acumulado=0
        for producto in Verduras:
            if producto.getCategoria() == categoria:
                acumulado+= producto.getPrecioNeto()
        promedio=acumulado/len(Verduras)
        print("El promedio teniendo en cuenta solo el precio neto de las verduras = {}".format(promedio))

    def CalcularPromedioPTPAseo(self, Aseo):
        categoria="aseo"
        acumulado=0
        for producto in Aseo:
            if producto.getCategoria() == categoria:
                acumulado+= producto.getPrecioTotal()
                if producto.getPrecioTotal() < 20000:
                    promedio= acumulado/len(Aseo)
        print("El promdio teniendo en cuenta el precio total de los productos de aseo = {}".format(promedio))
    