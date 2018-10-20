import math
from nodo import *
import numpy as np
import random


class Arbol:

    def __init__(self):
        self.raiz = Nodo()

    def crear_arbol(self, filas):
        """crear_arbol
        Inicia el proceso recursivo de creacion con la raiz
        """

        self.raiz = self.crear_sub_arbol(
                                        self.raiz, filas,
                                        self.get_entropia_raiz(filas),
                                        "R")

    def crear_sub_arbol(self, nodo, filas, entropia, enlace):
        """crear_sub_arbol
        Construye el arbol con base en n filas seleccionadas al azar,
        sigue el algoritmo describo en el libro, buscando siempre
        el atributo con mejor ganancia
        """

        # cantidad de columnas en valor random
        cantidad_col = len(filas.columns) - 1
        # cantidad de columnas random sobre las que se elige el mejor atributo
        cantidad_col_ran = math.floor(math.sqrt(cantidad_col))
        # numeros de columnas seleccionadas en el valor random
        numeros_cols = self.generar_columnas(cantidad_col_ran, cantidad_col)
        # nombre de la columnas seleccionadas de donde se elige el mejor atributo
        nombre_cols = self.get_nombre_columnas(filas, numeros_cols)
        # devuelve el nombre del atributo de mejor ganancia
        m_ganan = self.mejor_atributo(filas, entropia, nombre_cols)
        nodo.etiqueta = str(enlace) + "  ->  " + m_ganan
        nodo.nombre = m_ganan
        nodo.enlace = enlace
        # todos los valores diferentes del atributo seleccionado
        valores_unicos = filas[m_ganan].unique()
        for val in valores_unicos:
            dist = filas.loc[(filas[m_ganan] == val) & (filas['diagnosis'].isin([0, 1]))]
            dist = dist.drop(m_ganan, axis=1)
            s_entropia = self.get_entropia_raiz(dist)
            if(s_entropia == 0):
                nodo.agregar_hoja([self.get_prediccion(dist), val])
            else:
                if(len(dist.columns) == 2):
                    nombre = dist.columns[0]
                    s_nodo = Nodo()
                    s_nodo.etiqueta = str(val) + "  ->  " + nombre
                    s_nodo.nombre = nombre
                    s_nodo.enlace = val
                    self.columna_unica(s_nodo, dist, nombre)
                    nodo.agregar_nodo(s_nodo)
                else:
                    s_nodo = Nodo()
                    sud_nodo = self.crear_sub_arbol(s_nodo, dist, s_entropia, val)
                    nodo.agregar_nodo(s_nodo)
        return nodo

    def generar_columnas(self, cantidad, atributos):
        """generar_columnas
        Genera una lista de tamano n, con numeros random
        entre 0 y atributos, esta lista representa las
        columnas a evaluar
        """

        lista_columnas = []
        while cantidad > 0:
            col = random.randint(0, atributos - 1)
            if(col not in lista_columnas):
                lista_columnas.append(col)
                cantidad += -1
        return lista_columnas

    def columna_unica(self, nodo, dist, nombre):
        """ columna_unica
        En caso de que solo quede una columna, se calcula el resultado
        del grupo de datos pertinente
        """

        valores_unicos = dist[nombre].unique()
        filas = len(dist.index)
        for val in valores_unicos:
            sub_dist = dist.loc[(dist[nombre] == val) & (dist['diagnosis'].isin([0, 1]))]
            valores = sub_dist['diagnosis']
            positivos = sum(1 for v in valores if v == 1)
            negativos = len(sub_dist.index) - positivos
            self.definir_eleccion(positivos, negativos, val, nodo)

    def definir_eleccion(self, positivos, negativos, valor, nodo):
        """ definir_eleccion
        En caso de que solo quede una columna se extraer las posibles
        elecciones de la misma
        """

        if(positivos > negativos):
            nodo.agregar_hoja([True, valor])
        else:
            if(negativos > positivos):
                nodo.agregar_hoja([False, valor])
            else:
                decision = bool(random.getrandbits(1))
                nodo.agregar_hoja([decision, valor])

    def get_prediccion(self, filas):
        """ get_prediccion
        Retorna True si la prediccion de un grupo de filas es 1 sino False
        """

        valor = filas['diagnosis'].unique()
        if(valor[0] == 1):
            return True
        else:
            return False

    def get_nombre_columnas(self, filas, columnas):
        """get_nombre_columnas
        Obtiene el nombre de un conjunto de columnas
        """

        nombres = []
        for col in columnas:
            nombres.append(filas.columns[col])
        return nombres

    def mejor_atributo(self, filas, entropia, columnas):
        """mejor_atributo
        Obtiene cual es el mejor atributo de un lista
        de posibles mejores atributos
        """

        ganancia_maxima = -1
        atributo_seleccionado = ""
        for col in columnas:
            d_cols = filas[[col, 'diagnosis']]
            v_unicos = d_cols[col].unique()
            ganancia = self.ganancia_informacion(v_unicos, d_cols, col, entropia)
            if(ganancia > ganancia_maxima):
                ganancia_maxima = ganancia
                atributo_seleccionado = col
        return atributo_seleccionado

    def get_entropia_raiz(self, filas):
        """ get_entropia_raiz
        Obtiene la entropia de un conjunto de filas
        """

        positivos = self.contar_positivos(filas)
        negativos = len(filas.index) - positivos
        return self.entropia(positivos, negativos)

    def entropia(self, p, n):
        """ entropia
        Calculo de la entropia segun la formula del libro
        """

        total = p + n
        if(p == 0 or n == 0):
            return 0
        else:
            cal_p = ((p / total) * math.log2(p / total))
            cal_n = ((n / total) * math.log2(n / total))
            return -1 * (cal_p + cal_n)

    def ganancia_informacion(self, v_unicos, datos_columnas, col, entropia):
        """ ganancia_informacion
        Retorna la diferencia entre la entropia del nodo padre
        y el residuo del atributo
        """

        residuo = self.residuo(v_unicos, datos_columnas, col)
        return entropia - residuo

    def contar_positivos(self, distribucion):
        """ contar_positivos
        Cuenta cuantas filas (con un mismo valor de un atributo)
        tienen como resultado: positivo
        """

        positivos = distribucion.loc[(distribucion['diagnosis'] == 1)]
        return len(positivos.index)

    def residuo(self, v_unicos, datos, n_columna):
        """residuo
        Para cada atributo obtiene su residuo, que esta dado por
        la suma de la entropia * (p/total + n/total) de
        cada valor diferente.
        """

        residuo = 0
        for val in v_unicos:
            dist = datos.loc[(datos[n_columna] == val) & (datos['diagnosis'].isin([0, 1]))]
            positivos = self.contar_positivos(dist)
            negativos = len(dist.index) - positivos
            entropia = self.entropia(positivos, negativos)
            residuo += (len(dist.index) / len(datos.index)) * entropia
        return residuo

    def ver_arbol(self):
        print(self.raiz.etiqueta)
        self.ver_arbol_aux(1, self.raiz)

    def ver_arbol_aux(self, nivel, nodo_raiz):
        for hoja in nodo_raiz.hojas():
            print(" " * nivel, hoja.g_enlace(), " -> ", hoja.g_valor())

        for nodo in nodo_raiz.nodos():
            print(" " * nivel, nodo.g_etiqueta())
            self.ver_arbol_aux(nivel + 3, nodo)

    def obtener_valor_fila(self, fila, atributo):
        """ obtener_valor_fila
        Dada una fila, obtiene el valor de un atributo
        """

        indice = fila.loc[[0]]
        return indice[atributo][0]

    def evaluar_fila(self, fila):
        """ evaluar_fila
        Inicia el proceso recursivo de evaluacion de una funcion
        """

        return self.evaluar_fila_aux(self.raiz, fila)

    def evaluar_fila_aux(self, nodo, fila):
        """ evaluar_fila_aux
        Funcion donde se evalua a profundidad una fila en el arbol.
        Retorna True o False
        """

        nombre_atributo = nodo.g_nombre()
        valor = self.obtener_valor_fila(fila, nombre_atributo)
        if(nodo.contiene_hoja(valor)):
            return nodo.obtener_valor_hoja(valor)
        else:
            if(nodo.contiene_nodo(valor)):
                nodo_siguiente = nodo.obtener_nodo_siguiente(valor)
                return self.evaluar_fila_aux(nodo_siguiente, fila)
            else:
                return bool(random.getrandbits(1))
