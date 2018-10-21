import pandas as pd
from arbol import *
from modelo import *


class Random_Forest (Modelo):

    def __init__(self, arboles, filas=None):
        self.filas = filas
        self.numero_arboles = arboles
        self.forest = []

    def learner(self, filas):
        """ learner
        Se configura y se crea el modelo de random forest
        """
        self.filas = filas
        self.crear_bootstrapped()
        self.crear_forest()

    def probar_modelo(self, filas):
        """ probar_modelo
        Dado un conjunto de filas se prueba el modelo
        obteniendo como respuesta la tasa de error de dichas
        pruebas
        """

        filas.reset_index(inplace=True)
        errores = 0
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
            if(respuesta_pre != respuesta_real):
                errores += 1

        return errores / len(filas.index)

    def get_valor_real(self, fila):
        """ get_valor_real
        Obtiene el valor real de una fila, el "y"
        Retorna True si es 1 (Benigno), y sino False
        """

        valor_real = fila['diagnosis'][0]
        if (valor_real == 1):
            return True
        else:
            return False

    def crear_bootstrapped(self):
        """ crear_bootstrapped
        Crea el bootstrapped del random forest, seleccionando
        filas al azar del conjunto de entrada
        """

        self.bootstrapped = pd.DataFrame(columns=self.filas.columns)
        numero_filas = len(self.filas.index) - 1
        self.bootstrapped = self.filas.sample(n=numero_filas, replace=True)

    def crear_forest(self):
        """ crear_forest
        Se crea el bootstrapped del random forest y se crean
        todos los árboles solicitados
        """

        self.crear_bootstrapped()
        for num in range(self.numero_arboles):
            arbol = Arbol()
            arbol.crear_arbol(self.bootstrapped)
            self.forest.append(arbol)

    def evaluar_fila_forest(self, fila):
        """ evaluar_fila_forest
        Toma una fila en particular y la evalua en el
        random forest. Devuelve True si es Benigno y
        False si es maligno
        """

        positivos = 0   # Benigno
        negativos = 0   # Maligno
        for arbol in self.forest:
            prediccion = arbol.evaluar_fila(fila)
            if(prediccion):
                positivos += 1
            else:
                negativos += 1
        if(positivos >= negativos):
            return True     # Benigno
        else:
            return False    # Maligno

    def predecir(self, filas):
        """ predecir
        Toma un conjunto de filas y se las aplica al random
        forest, devolviendo la predicciones generadas y la tasa de error
        de las mismas
        """

        filas.reset_index(inplace=True)
        errores = 0
        lista_resultados = []
        lista_reales = []
        conta = 0
        for indice in range(len(filas.index)):
            fila = self.crear_fila(filas, indice)
            respuesta_pre = self.evaluar_fila_forest(fila)
            respuesta_real = self.get_valor_real(fila)
            if(respuesta_pre != respuesta_real):
                conta += 1
                errores += 1
            lista_reales.append(respuesta_real)
            if(respuesta_pre is True):
                lista_resultados.append('B')
            else:
                lista_resultados.append('M')
        return [errores / len(filas.index), lista_resultados]

    def crear_fila(self, filas, indice):
        """ crear_fila
        Toma un grupo de datos y los transforma en una fila para
        poderlos evaluar posteriormente
        """

        sub_fila = filas.loc[indice]
        columnas = len(filas.columns)
        lista_fila = []
        for i in range(columnas):
            lista_fila.append(sub_fila[i])
        lista_fila = lista_fila[1:]
        fila = pd.DataFrame(columns=filas.columns[1:])
        fila.loc[0] = lista_fila
        return fila

    def print_forest(self):
        """ print_forest
        Muestra todos los árboles del random forest
        """

        for arbol in self.forest:
            arbol.ver_arbol()
