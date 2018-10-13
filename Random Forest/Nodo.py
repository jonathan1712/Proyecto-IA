from Hoja import *
class Nodo:
    def __init__(self):
        self.listaNodos = []
        self.listaHojas = []
        self.etiqueta = ""
        self.enlace = ""

    def getEntropia(self):
        print("Hola")

    def getListaHojas(self):
        return self.listaHojas

    def getListaNodos(self):
        return self.listaNodos

    def getEtiqueta(self):
        return etiqueta
    
    def getEnlace(self):
        return enlace

    def getValorPeso(self):
        return valorPeso
    """
    def agregarElemento(self, particiones, nombre):
        for particion in particiones:
            print(particion)
            if(len(particion)==1):
                ultimo = len(particion[0]) -1
                if(particion[0][ultimo]==1):
                    self.agregarHoja(True)
                else:
                    self.agregarHoja(False)
            else:
                self.agregarNodo(filas)
    """

    def agregarNodo(self, nodito):
        self.listaNodos.append(nodito)

    def agregarHoja(self, datos):
        hoja = Hoja(datos[0], datos[1])
        self.listaHojas.append(hoja)

    def verHojas(self):
        for g in self.listaHojas:
            print(g.getValor())

    def verNodos(self):
        for f in self.listaNodos:
            print(f)