from math import *
from Nodo import *
import numpy as np
import random

class Arbol:
    def __init__(self):
        self.raiz = Nodo()

    # Función donde se crea al árbol,es una función de paso
    def crear_arbol(self, filas):
        numero_columnas = len(filas.columns) - 1
        self.raiz = self.crear_sub_arbol(self.raiz, filas, self.get_entropia_raiz(filas),"R")

    # Función donde se crean las ramas del árbol, y por consecuente las hojas
    def crear_sub_arbol(self, nodo, filas, entropia,enlace):

        # cantidad de columnas en valor random ###
        #cantidad_filas = random
        # Tomar en cuenta el valor random ###
        numeros_columnas = [col for col in range (len(filas.columns)-1)]
        # Generar
        nombre_columnas = self.get_nombre_columnas(filas, numeros_columnas)
        # Devuelve el nombre del atributo de mejor ganancia, en caso de empate el primero desde la izquierda
        mejorGanancia = self.mejor_atributo(filas,entropia, nombre_columnas)
        nodo.etiqueta = str(enlace) + "  ->  " +  mejorGanancia   
        # Todos los valores diferentes del atributo seleccionado
        valores_unicos = filas[mejorGanancia].unique()

        # nodo.agregarHoja(self.getValorReal(particion, mejorGanancia))
        for valor in valores_unicos:
            distribucion = filas.loc[(filas[mejorGanancia]==valor) & (filas['diagnosis'].isin([0,1]))]
            distribucion = distribucion.drop(mejorGanancia, axis = 1)
            sub_entropia = self.get_entropia_raiz(distribucion)
            
            if(sub_entropia==0):
                nodo.agregarHoja([self.get_prediccion(distribucion),valor])
            else:
                if(len(distribucion.columns)==2):
                    nombre = distribucion.columns[0]
                    subNodo = Nodo()
                    subNodo.etiqueta = str(valor) + "  ->  " +  nombre  
                    self.columna_unica(subNodo, distribucion, nombre)
                    nodo.agregarNodo(subNodo)
                else:
                    subNodo = Nodo()
                    sudNodo = self.crear_sub_arbol(subNodo, distribucion, sub_entropia,valor)
                    nodo.agregarNodo(subNodo) 
        return nodo

    # Tratamiento especial en caso de que solo quede una columna
    def columna_unica(self, nodo, distribucion, nombre ):
        valores_unicos = distribucion[nombre].unique()
        filas = len(distribucion.index)
        for valor in valores_unicos:
            sub_distribucion = distribucion.loc[(distribucion[nombre]==valor) & (distribucion['diagnosis'].isin([0,1]))]
            valores = sub_distribucion['diagnosis']
            positivos = sum(1 for v in valores if v == 1)
            negativos = len(sub_distribucion.index) - positivos
            self.definir_eleccion(positivos, negativos, valor, nodo)

    # En caso de que solo quede una columna se extraer las posibles elecciones de la misma
    def definir_eleccion(self, positivos, negativos, valor, nodo):
        if(positivos>negativos):
            nodo.agregarHoja([True, valor])
        else:
            if(negativos>positivos):
                nodo.agregarHoja([False, valor])
            else:
                decision = random.randint(0,1)
                if(decision==1):
                    nodo.agregarHoja([True, valor])
                else:
                    nodo.agregarHoja([False, valor])

    # Obtiene la predicción de un conjunto de filas 
    def get_prediccion(self, filas):
        valor = filas['diagnosis'].unique()
        if(valor[0]==1):
            return True
        else:
            return False

    # Obtiene el nombre de un conjunto de columnas
    def get_nombre_columnas(self,filas,columnas):
        nombres = []
        for col in columnas:
            nombres.append(filas.columns[col])
        return nombres    

    # Obtiene cuál es el mejor atributo de un lista de posibles mejores atributos
    def mejor_atributo(self, filas, entropia, columnas): 
        #print(filas)
        ganancia_maxima = -1 
        atributo_seleccionado = ""
        for col in columnas:
            datos_columnas = filas[[col,'diagnosis']]                       
            valores_unicos = datos_columnas[col].unique()           
            ganancia = self.ganancia_informacion(valores_unicos, datos_columnas,col,entropia)
            #print("Ganancia: ",ganancia)
            if(ganancia > ganancia_maxima):

                ganancia_maxima = ganancia
                atributo_seleccionado = col

        return atributo_seleccionado

    # Obtiene la entropía de un conjunto de filas
    def get_entropia_raiz(self, filas):
        positivos = self.contar_positivos(filas)
        negativos = len(filas.index) - positivos
        return self.entropia(positivos, negativos)

    # Cálculo de la entropia según la fórmula del libro
    def entropia(self, p, n):
        total = p + n
        if(p == 0 or n == 0):
            return 0
        else:
            return -1 * (((p/total)* log2(p/total)) + ((n/total)* log2(n/total)))

    # Cálculo de la ganancia, fórmula del libro
    def ganancia_informacion(self, valores_unicos, datos_columnas, col, entropia):
        residuo = self.residuo(valores_unicos, datos_columnas,col)
        return entropia - residuo

    # Cuenta cuantas filas (con un mismo valor de un atributo) tienen como resultado: positivo 
    def contar_positivos(self, distribucion):
        positivos = distribucion.loc[(distribucion['diagnosis']==1)]
        return len(positivos.index)

    # Otiene un arreglo de filas por cada valor diferente en la columna
    def residuo(self, valores_unicos, datos_columnas, nombre_columna):
        residuo = 0
        for valor in valores_unicos:
            distribucion = datos_columnas.loc[(datos_columnas[nombre_columna]==valor) & (datos_columnas['diagnosis'].isin([0,1]))]
            positivos = self.contar_positivos(distribucion)
            negativos = len(distribucion.index) - positivos
            residuo +=  (len(distribucion.index) / len(datos_columnas.index)) * self.entropia(positivos, negativos)
        return residuo 

    # Función de impresión del árbol, solo para tener una perspectiva clara
    def ver_arbol(self):
        print(self.raiz.etiqueta)
        self.ver_arbol_aux(1, self.raiz)

    # Función auxiliar de impresión del árbol
    def ver_arbol_aux(self, nivel, nodoRaiz):
        for hoja in nodoRaiz.listaHojas:
            print(" "*nivel,hoja.getEnlace(),  " -> ", hoja.getValor())

        for nodo in nodoRaiz.listaNodos:
            print(" "*nivel,nodo.etiqueta)
            self.ver_arbol_aux(nivel+3, nodo)