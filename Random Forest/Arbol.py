from math import *
from Nodo import *
import numpy as np
import random

class Arbol:
    def __init__(self):
        self.raiz = Nodo()

    def crearArbol(self, filas):
        numero_columnas = len(filas.columns) - 1
        self.raiz = self.crearSubArbol(self.raiz, filas, self.getEntropiaRaiz(filas))

    def crearSubArbol(self, nodo, filas, entropia):
        ### cantidad de columnas en valor random ###
        #cantidad_filas = random

        ### Tomar en cuenta el valor random ###
        numeros_columnas = [col for col in range (len(filas.columns)-1)]
        
        ### Generar
        nombre_columnas = self.getNombreColumnas(filas, numeros_columnas)

        ### Devuelve el nombre del atributo de mejor ganancia, en caso de empate el primero desde la izquierda
        mejorGanancia = self.mejorAtributo(filas,entropia, nombre_columnas)

        nodo.etiqueta = mejorGanancia

        ### Todos los valores diferentes del atributo seleccionado
        valores_unicos = filas[mejorGanancia].unique()

        ### nodo.agregarHoja(self.getValorReal(particion, mejorGanancia))
        for valor in valores_unicos:
            distribucion = filas.loc[(filas[mejorGanancia]==valor) & (filas['R'].isin([0,1]))]
            distribucion = distribucion.drop(mejorGanancia, axis = 1)
            sub_entropia = self.getEntropiaRaiz(distribucion)
            if(sub_entropia==0):
                nodo.agregarHoja([self.getPrediccion(distribucion),valor])
            else:
                if(len(distribucion.index)==1):
                    print("ajustar")
                else:
                    subNodo = Nodo()
                    sudNodo = self.crearSubArbol(subNodo, distribucion, sub_entropia)
                    nodo.agregarNodo(subNodo)
        return nodo
    def getPrediccion(self, filas):
        valor = filas['R'].unique()
        if(valor[0]==1):
            return True
        else:
            return False

    def getNombreColumnas(self,filas,columnas):
        nombres = []
        for col in columnas:
            nombres.append(filas.columns[col])
        return nombres    

    def mejorAtributo(self, filas, entropia, columnas): 
        ganancia_maxima = 0
        atributo_seleccionado = 0
        for col in columnas:
            datos_columnas = filas[[col,'R']]                                               #extraigo la columna
            valores_unicos = datos_columnas[col].unique()                                   #luego los valores únicos de esa columna
            ganancia = self.gananciaInformacion(valores_unicos, datos_columnas,col,entropia)
            if(ganancia > ganancia_maxima):
                ganancia_maxima = ganancia
                atributo_seleccionado = col
        return atributo_seleccionado

    def getEntropiaRaiz(self, filas):
        positivos = self.contarPositivos(filas)
        negativos = len(filas.index) - positivos
        return self.entropia(positivos, negativos)

    def entropia(self, p, n):
        total = p + n
        if(p == 0 or n == 0):
            return 0
        else:
            return -1 * (((p/total)* log2(p/total)) + ((n/total)* log2(n/total)))

    # Cálculo de la ganancia, fórmula del libro
    def gananciaInformacion(self, valores_unicos, datos_columnas, col, entropia):
        residuo = self.residuo(valores_unicos, datos_columnas,col)
        return entropia - residuo

    # Cuenta cuantas filas (con un mismo valor de un atributo) tienen como resultado: positivo 
    def contarPositivos(self, distribucion):
        positivos = distribucion.loc[(distribucion['R']==1)]
        return len(positivos.index)

    # Otiene un arreglo de filas por cada valor diferente en la columna
    def residuo(self, valores_unicos, datos_columnas, nombre_columna):
        residuo = 0
        for valor in valores_unicos:
            distribucion = datos_columnas.loc[(datos_columnas[nombre_columna]==valor) & (datos_columnas['R'].isin([0,1]))]
            positivos = self.contarPositivos(distribucion)
            negativos = len(datos_columnas.index) - positivos
            residuo +=  (len(distribucion.index) / len(datos_columnas.index)) * self.entropia(positivos, negativos)
        return residuo 

    def verArbol(self):
        print(self.raiz.etiqueta)
        self.verArbolAux(1, self.raiz)

    def verArbolAux(self, nivel, nodoRaiz):
        for hoja in nodoRaiz.listaHojas:
            print(" "*nivel,hoja.getEnlace(),  " -> ", hoja.getValor())

        for nodo in nodoRaiz.listaNodos:
            print(" "*nivel,nodo.etiqueta)
            self.verArbolAux(nivel+3, nodo)