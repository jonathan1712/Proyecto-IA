import pandas as pd
from arbol import *


class Random_Forest:

    def __init__(self, arboles, filas):
        self.filas = filas
        self.numero_arboles = arboles
        self.forest = []
        #self.crear_bootstrapped()

    def crear_bootstrapped(self):
        self.bootstrapped = pd.DataFrame(columns=self.filas.columns)
        numero_filas = len(self.filas.index) - 1
        self.bootstrapped = self.filas.sample(n=numero_filas, replace=True)

    def crear_forest(self):
        self.crear_bootstrapped()
        for num in range(self.numero_arboles):
            arbol = Arbol()
            arbol.crear_arbol(self.bootstrapped)
            self.forest.append(arbol)

    def evaluar_fila_forest(self, fila):
        positivos = 0
        negativos = 0
        for arbol in self.forest:
            prediccion = arbol.evaluar_fila(fila)
            if(prediccion):
                positivos += 1
            else:
                negativos += 1
        if(positivos>=negativos):
            return "Benigno"
        else:
            return "Maligno"

    def print_forest(self):
        for arbol in self.forest:
            arbol.ver_arbol()


