import pandas as pd
from arbol import *
from modelo import *


class Random_Forest (Modelo):

    def __init__(self, arboles, filas=None):
        self.filas = filas
        self.numero_arboles = arboles
        self.forest = []
    
    def learner(self, filas):
        self.filas = filas
        self.crear_bootstrapped()
        self.crear_forest()

    def probar_modelo(self, filas):
        filas.reset_index(inplace=True)
        aciertos = 0 
        for indice in range(len(filas.index)):
            sub_fila = filas.loc[indice]
            columnas = len(filas.columns)
            lista_fila = []
            for i in range(columnas):
                lista_fila.append(sub_fila[i])
            lista_fila = lista_fila[1:]
            fila = pd.DataFrame(columns=filas.columns[1:])
            fila.loc[0] = lista_fila
            respuesta_pre = self.evaluar_fila_forest(fila)
            respuesta_real = self.get_valor_real(fila)
            if(respuesta_pre == respuesta_real):
                aciertos += 1

        return aciertos / len(filas.index)

    def get_valor_real(self, fila):
        valor_real = fila['diagnosis'][0]
        if (valor_real == 1):
            return True
        else:
            return False

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
        positivos = 0   # Benigno
        negativos = 0   # Maligno
        for arbol in self.forest:
            prediccion = arbol.evaluar_fila(fila)
            if(prediccion):
                positivos += 1
            else:
                negativos += 1
        if(positivos>=negativos):
            return True     # Benigno
        else:
            return False    # Maligno

    def print_forest(self):
        for arbol in self.forest:
            arbol.ver_arbol()


