import numpy as np
import pandas as pd
from scipy import stats


class Normalizador:

    def __init__(self, datos=None, num_rangos=None):
        self.datos = datos
        self.num_rangos = np.array(num_rangos)

    def normalizar(self):
        """ normalizar
        Para cada fila del data_set se aplica la funcian zscore.
        Cada valor de cada fila es redondeado a dos decimales
        antes de ser normalizado.
        """

        # -1 para no normalizar la columna de la respuesta
        columnas = len(self.datos.columns) - 1
        for i in range(columnas):
            nombre_columna = self.datos.columns[i]
            columna = self.datos[nombre_columna]
            # redonde los datos a dos dagitos
            columna = [round(float(ind), 2) for ind in columna]
            # normalize la columna
            columna = self.zcore(columna)
            self.datos[nombre_columna] = columna

    def zcore(self, columna):
        """ zscore
        Aplica la funcian zscore de stats a una columna (lista)
        """

        columna = stats.zscore(columna)
        return columna

    def clasificar_columnas(self):
        """ clasificar_columnas
        Toma las columnas ya normalizadas y las clasifica segan
        la cantidad de rangos solicitados.
        No clasifica la columna de diagnosis.
        """

        # -1 para no tomar en cuenta la columna de la respuesta
        columnas = len(self.datos.columns) - 1
        for i in range(columnas):
            nombre_columna = self.datos.columns[i]
            columna = self.datos[nombre_columna]
            minimo = round(columna.min(), 2)
            maximo = round(columna.max(), 2)
            media = columna.mean()
            rango = self.num_rangos[i]
            etiq_rangos = self.generar_rangos(media, minimo, maximo, rango)
            columna = self.clasificar_columna(columna, etiq_rangos)
            self.datos[nombre_columna] = columna

    def generar_rangos(self, media, minimo, maximo, rangos):
        """ generar_rangos
        Dado los valores flotantes de media, manimo, maximo de una columna,
        genera un cantidad n de rangos, para ello se calcula la distancia
        del manimo al maximo y ese es el intervalo de cada rango.
        Hace distincian entre lamite del tipo "<x, >x" y a <= x < b
        """

        lista_rangos = []
        if(rangos == 2):
            lista_rangos.append("< " + str(round(float(media), 2)))
            lista_rangos.append(str(round(float(media), 2)) + " <")
        else:
            # Determina el tamano de cada rango
            pivote = round((maximo-minimo)/rangos, 2)
            paso = minimo + pivote
            for indice in range(rangos - 1):
                paso = round(paso, 2)
                paso_pi = round(paso + pivote, 2)
                if(indice == 0):
                    lista_rangos.append("< " + str(paso))
                    lista_rangos.append(str(paso) + " - " + str(paso_pi))
                else:
                    if(indice == rangos - 2):
                        lista_rangos.append(str(paso) + " <")
                    else:
                        lista_rangos.append(str(paso) + " - " + str(paso_pi))
                paso = round(paso + pivote, 2)
        return lista_rangos

    def clasificar_columna(self, columna, etiquetas):
        """ clasificar_columna
        Clasifica todos los elementos de una columna con base en las
        etiquetas que se generaron para la misma segan el namero de
        rangos solicitados.
        """

        columna_nueva = []
        largo = len(etiquetas) - 1
        for indice, n in enumerate(columna):
            for etiqueta in etiquetas:
                if(self.evaluar_limite(0, etiqueta, n)):
                    columna_nueva += [etiqueta]
                    break
                if(self.evaluar_limite(1, etiquetas[largo], n)):
                    columna_nueva += [etiquetas[largo]]
                    break
                if(self.evaluar_acote(etiqueta, n)):
                    columna_nueva += [etiqueta]
                    break
        return columna_nueva

    def evaluar_acote(self, expresion, num):
        """ evaluar_acote
        Evalua expresiones en string del tipo 10 - 11, donde implica
        que 10 <= x < 11, y en caso de ser correcto retorn True o False
        """

        lim = expresion.split(" - ")
        if(("<" not in expresion) and (float(lim[0]) <= num < float(lim[1]))):
            return True
        else:
            return False

    def evaluar_limite(self, tipo, expresion, numero):
        """ evaluar_limite
        Evalua expresiones en string del tipo numero < x, x < numero, y
        retorna True o False dependiendo de la evaluacian.
        """

        # limite inferior donde numero < eval(expresion)
        if(tipo == 0):
            if(("<" in expresion) and (eval(str(numero) + expresion))):
                return True
            else:
                return False
        else:
            # limite superior numero > eval(expresion)
            if(tipo == 1):
                if(("<" in expresion) and (eval(expresion + str(numero)))):
                    return True
                else:
                    return False

    def ver_datos(self):
        print(self.datos)
