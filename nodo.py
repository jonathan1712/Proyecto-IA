from hoja import *


class Nodo:

    def __init__(self):
        self.lista_nodos = []
        self.lista_hojas = []
        self.etiqueta = ""
        self.enlace = ""
        self.nombre = ""

    def hojas(self):
        """ hojas
        Retorna las hojas asociadas al nodo actual
        """

        return self.lista_hojas

    def nodos(self):
        """ nodos
        Retorna los nodos asociadas al nodo actual
        """

        return self.lista_nodos

    def g_etiqueta(self):
        """ etiqueta
        Retorna la etiqueta del nodo actual
        """

        return self.etiqueta

    def g_enlace(self):
        """ enlace
        Retorna el enlace del nodo actual
        """

        return self.enlace

    def g_nombre(self):
        """ nombre
        Retorna el nombre del atributo propietario del nodo
        """

        return self.nombre

    def agregar_nodo(self, nodo):
        """ agregar_nodo
        Agrega un nodo a la lista de nodos hijos del actual nodo
        """

        self.lista_nodos.append(nodo)

    def agregar_hoja(self, datos):
        """ agregar_hoja
        Agregar una hoja a la lista de hojas del nodo actual
        """

        hoja = Hoja(datos[0], datos[1])
        self.lista_hojas.append(hoja)

    def obtener_valor_hoja(self, valor):
        """ obtener_valor_hoja
        Obtener el valor de una hoja en particular, dado el enlace de la misma
        """

        valor_hoja = ""
        for hoja in self.lista_hojas:
            if(hoja.g_enlace() == valor):
                valor_hoja = hoja.g_valor()
                break
        return valor_hoja

    def contiene_hoja(self, valor):
        """ contiene_hoja
        Verifica si un nodo posee una hoja, dado un enlace particular
        """

        estado = False
        for hoja in self.lista_hojas:
            if(hoja.g_enlace() == valor):
                estado = True
                break
        return estado

    def contiene_nodo(self, valor):
        """ contiene_nodo
        Verifica si un nodo contiene un nodo, dado el nombre de un atributo
        """

        estado = False
        for nodo in self.lista_nodos:
            if(nodo.g_enlace() == valor):
                estado = True
                break
        return estado

    def obtener_nodo_siguiente(self, valor):
        """ obtener_nodo_siguiente
        Obtener un nodo de la lista de nodos del objeto actual, dado
        el nombre del atributo
        """

        nodo_siguiente = Nodo()
        for nodo in self.lista_nodos:
            if(nodo.g_enlace() == valor):
                nodo_siguiente = nodo
                break
        return nodo_siguiente
