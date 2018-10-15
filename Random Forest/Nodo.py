from Hoja import *
class Nodo:
    def __init__(self):
        self.lista_nodos = []
        self.lista_hojas = []
        self.etiqueta = ""
        self.enlace = ""
        self.nombre = ""

    def obtener_hojas(self):
        return self.lista_hojas

    def obtener_nodos(self):
        return self.lista_nodos

    def obtener_etiqueta(self):
        return self.etiqueta
    
    def obtener_enlace(self):
        return self.enlace

    def obtener_nombre(self):
        return self.nombre

    def agregar_nodo(self, nodito):
        self.lista_nodos.append(nodito)

    def agregar_hoja(self, datos):
        hoja = Hoja(datos[0], datos[1])
        self.lista_hojas.append(hoja)

    def obtener_valor_hoja(self, valor):
        valor_hoja = ""
        for hoja in self.lista_hojas:
            if(hoja.obtener_enlace() == valor):
                valor_hoja = hoja.obtener_valor()
                break
        return valor_hoja

    def contiene_hoja(self, valor):
        estado = False
        for hoja in self.lista_hojas:
            if(hoja.obtener_enlace() == valor):
                estado = True
                break
        return estado

    def contiene_nodo(self, valor):
        estado = False
        for nodo in self.lista_nodos:
            if(nodo.obtener_enlace() == valor):
                estado = True
                break
        return estado

    def obtener_nodo_siguiente(self, valor):
        nodo_siguiente = Nodo()
        for nodo in self.lista_nodos:
            if(nodo.obtener_enlace() == valor):
                nodo_siguiente = nodo
                break
        return nodo_siguiente