from math import *
from Nodo import *
import numpy as np
import random
class Arbol:
    def __init__(self):
        self.x = 0
        self.raiz = Nodo()
        self.etiquetas = []

    def crearArbol(self, filas):
        self.etiquetas = filas[0]                       # guardo las etiquetas
        filas = np.delete(filas, 0, 0)                  # elimino las filas de las etiquetas
        self.raiz = self.crearSubArbol(self.raiz, filas, self.getEntropiaRaiz(filas), self.generarColumnas(np.size(filas,1)-1))

    def crearSubArbol(self, nodo, filas, entropia, columnas):

        mejorGanancia = self.mejorAtributo(filas,entropia, columnas)

        valores = self.valores_columna(filas, mejorGanancia)
        particiones = self.getParticiones(valores, filas, mejorGanancia)

        columnas.remove(mejorGanancia)
        nodo.etiqueta = self.etiquetas[mejorGanancia]
        """
        print("Entropia: ", entropia)
        print("Mejor atributo: ", mejorGanancia)
        print("Columnas: ", columnas)
        print("Filas: ", filas)
        print("Particiones", particiones)
        print("Len particiones: ", len(particiones))"""
        #--------------------------------------------    
        for particion in particiones:
            sub_entropia = self.getEntropiaRaiz(particion)
            if((sub_entropia==0) or (len(columnas) ==0)):
                nodo.agregarHoja(self.getValorReal(particion, mejorGanancia))
            else:
                subNodo = Nodo()
                subNodo = self.crearSubArbol(subNodo, particion, sub_entropia, columnas)
                nodo.agregarNodo(subNodo)
        #--------------------------------------------
        
        return nodo

    def getValorReal(self, filas,columna):
        ultimo = len(filas[0]) - 1
        valorAtributo = filas[0][columna]
        if(int(filas[0][ultimo]==1)):
            return [True, valorAtributo]
        else:
            return [False, valorAtributo]

    def mejorAtributo(self, filas, entropia, columnas):
        ganancia_maxima = 0
        atributo_seleccionado = 0

        for col in columnas:
            ganancia = self.gananciaInformacion(col,filas,entropia)
            if(ganancia > ganancia_maxima):
                ganancia_maxima = ganancia
                atributo_seleccionado = col
        #print("Mejor atributo: ", atributo_seleccionado)
        return atributo_seleccionado

    def generarColumnas(self, columnas):
        lista = []
        for i in range(columnas):
            lista = lista + [i]
        return lista

    def getEntropiaRaiz(self, filas):
        positivos = 0
        negativos = 0
        for fila in filas:
            columnas = len(fila)
            if(int(fila[columnas-1])==1):
                positivos += 1
            else:
                negativos += 1
        return self.entropia(positivos, negativos)

    def entropia(self, p, n):
        total = p + n
        if(p == 0 or n == 0):
            return 0
        else:
            return -1 * (((p/total)* log2(p/total)) + ((n/total)* log2(n/total)))

    # Cálculo de la ganancia, fórmula del libro
    def gananciaInformacion(self, atributo, filas, entropia):
        totalFilas = len(filas)                                         #total de filas
        valores = self.valores_columna(filas, atributo)                 #valores diferentes de la columna respectiva al atributo X
        particiones = self.getParticiones(valores, filas, atributo)     #separación de las filas respecto a los valores diferentes
        residuo = self.residuo(particiones, totalFilas)


        # ganancia(atributo) = entropia - residuo(atributo)
        return entropia - residuo

    # Cuenta cuantas filas (con un mismo valor de un atributo) tienen como resultado: positivo 
    def contarPositivos(self, particion):
        positivos = 0
        for fila in particion:
            ultimaPosicion = len(fila) - 1
            if(int(fila[ultimaPosicion])==1):
                positivos += 1
        return positivos

    # Otiene un arreglo de filas por cada valor diferente en la columna
    def getParticiones(self, valores, filas, atributo):
        particiones = []
        for valor in valores:
            listaSub = []
            for fila in filas:
                if(fila[atributo]==valor):
                    listaSub = listaSub + [fila]
            particiones = particiones + [listaSub]  
        return particiones 

    # Obtiene todos los valores diferentes de una columna en especifico
    def valores_columna(self, filas, columna):
        return set([fila[columna] for fila in filas])

    # Formula del residuo, es la del libro
    def residuo(self, particiones, totalFilas):
        # p/total * B(p,n)
        residuo = 0
        for particion in particiones:
            positivos = self.contarPositivos(particion)
            negativos = len(particion) - positivos
            residuo += ((len(particion) / totalFilas) * self.entropia(positivos, negativos))
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