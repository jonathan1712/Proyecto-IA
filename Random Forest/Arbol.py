import math
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
        cantidad_columnas = len(filas.columns) - 1
        # cantidad de columnas random sobre las que se elige el mejor atributo
        #cantidad_columnas_random = random.randint(1,cantidad_columnas)
        cantidad_columnas_random = math.floor(math.sqrt(cantidad_columnas))
        # numeros de columnas seleccionadas en el valor random
        numeros_columnas = self.generar_columnas(cantidad_columnas_random, cantidad_columnas)
        # nombre de la columnas seleccionadas de donde se elige el mejor atributo
        nombre_columnas = self.get_nombre_columnas(filas, numeros_columnas)
        # Devuelve el nombre del atributo de mejor ganancia, en caso de empate el primero desde la izquierda
        mejor_ganancia = self.mejor_atributo(filas,entropia, nombre_columnas)
        nodo.etiqueta = str(enlace) + "  ->  " +  mejor_ganancia
        nodo.nombre = mejor_ganancia
        nodo.enlace = enlace   
        # Todos los valores diferentes del atributo seleccionado
        valores_unicos = filas[mejor_ganancia].unique()
        for valor in valores_unicos:
            distribucion = filas.loc[(filas[mejor_ganancia]==valor) & (filas['diagnosis'].isin([0,1]))]
            distribucion = distribucion.drop(mejor_ganancia, axis = 1)
            sub_entropia = self.get_entropia_raiz(distribucion)    
            if(sub_entropia==0):
                nodo.agregar_hoja([self.get_prediccion(distribucion),valor])
            else:
                if(len(distribucion.columns)==2):
                    nombre = distribucion.columns[0]
                    sub_nodo = Nodo()
                    sub_nodo.etiqueta = str(valor) + "  ->  " +  nombre
                    sub_nodo.nombre = nombre
                    sub_nodo.enlace = valor  
                    self.columna_unica(sub_nodo, distribucion, nombre)
                    nodo.agregar_nodo(sub_nodo)
                else:
                    sub_nodo = Nodo()
                    sud_nodo = self.crear_sub_arbol(sub_nodo, distribucion, sub_entropia,valor)
                    nodo.agregar_nodo(sub_nodo)
        return nodo

    def generar_columnas(self, cantidad, atributos):
        lista_columnas = []
        while cantidad > 0:
            col = random.randint(0,atributos - 1)
            if(col not in lista_columnas):
                lista_columnas.append(col)
                cantidad += - 1
        return lista_columnas

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
            nodo.agregar_hoja([True, valor])
        else:
            if(negativos>positivos):
                nodo.agregar_hoja([False, valor])
            else:
                decision = bool(random.getrandbits(1))
                nodo.agregar_hoja([decision, valor])

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
        ganancia_maxima = -1 
        atributo_seleccionado = ""
        for col in columnas:
            datos_columnas = filas[[col,'diagnosis']]                       
            valores_unicos = datos_columnas[col].unique()           
            ganancia = self.ganancia_informacion(valores_unicos, datos_columnas,col,entropia)
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
            return -1 * (((p/total)* math.log2(p/total)) + ((n/total)* math.log2(n/total)))

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
    def ver_arbol_aux(self, nivel, nodo_raiz):
        for hoja in nodo_raiz.obtener_hojas():
            print(" "*nivel,hoja.obtener_enlace(),  " -> ", hoja.obtener_valor())

        for nodo in nodo_raiz.obtener_nodos():
            print(" "*nivel,nodo.etiqueta)
            self.ver_arbol_aux(nivel+3, nodo)

    # Dada una fila, obtiene el valor de un atributo
    def obtener_valor_fila(self, fila, atributo):
        indice = fila.loc[[0]]
        return indice[atributo][0]
    
    # Función donde se evalua una fila en el árbol, es completamente de paso
    def evaluar_fila(self, fila):
        return self.evaluar_fila_aux(self.raiz, fila)

    # Función donde se evalua a profundidad una fila en el árbol, retorna True o False
    def evaluar_fila_aux(self, nodo, fila):
        nombre_atributo = nodo.obtener_nombre()
        valor = self.obtener_valor_fila(fila, nombre_atributo)
        if(nodo.contiene_hoja(valor)):
            return nodo.obtener_valor_hoja(valor)
        else:
            if(nodo.contiene_nodo(valor)):
                nodo_siguiente = nodo.obtener_nodo_siguiente(valor)
                return self.evaluar_fila_aux(nodo_siguiente, fila)
            else:
                return bool(random.getrandbits(1))