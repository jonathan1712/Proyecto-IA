import numpy as np
import pandas as pd
from scipy import stats

class Normalizador:
    

    def __init__(self, datos, num_rangos=0):
        self.datos = datos
        self.num_rangos = np.array(num_rangos)
    
    def normalizar(self):
        columnas = len(self.datos.columns)
        for i in range(columnas - 1):                             # -1 para no normalizar la columna de la respuesta
            nombre_columna = self.datos.columns[i]
            columna = self.datos[nombre_columna]
            columna = [round(float(ind), 2) for ind in columna]   # redonde los datos a dos dígitos
            columna = self.zcore(columna)                         # normalize la columna
            self.datos[nombre_columna] = columna

    def zcore(self, columna):
        columna = stats.zscore(columna)
        return columna

    def ver_datos(self):
        print(self.datos)
    
    def clasificar_columnas(self):
        columnas = len(self.datos.columns)
        for i in range(columnas - 1):                               # -1 para no tomar en cuenta la columna de la respuesta
            nombre_columna = self.datos.columns[i]
            columna = self.datos[nombre_columna]
            minimo = round(columna.min(), 2)
            maximo = round(columna.max(), 2)
            media = columna.mean()
            etiquetas_rangos = self.generar_rangos(media, minimo, maximo, self.num_rangos[i])
            columna = self.clasificar_columna(columna, etiquetas_rangos)
            self.datos[nombre_columna] = columna

    def generar_rangos(self, media, minimo, maximo, rangos):
        lista_rangos = []
        if(rangos == 2):
            lista_rangos.append("< " + str(round(float(media), 2)))
            lista_rangos.append(str(round(float(media), 2)) + " <")
        else:
            pivote = round((maximo-minimo)/rangos, 2)               # Determina el tamaño de cada rango
            paso = minimo + pivote
            for indice in range(rangos - 1):
                if(indice == 0):
                    lista_rangos.append("< " + str(round(paso, 2)))
                    lista_rangos.append(str(round(paso, 2))+ " - " + str(round(paso + pivote, 2)))
                else:
                    if(indice == rangos - 2):
                        lista_rangos.append(str(round(paso, 2)) + " <")  
                    else:
                        lista_rangos.append(str(round(paso, 2)) + " - " + str(round(paso + pivote, 2)))
                paso = round(paso + pivote, 2)
        return lista_rangos

    def clasificar_columna(self, columna, etiquetas):
        columna_nueva = []
        largo = len(etiquetas) - 1
        for indice, n in enumerate(columna):
            for etiqueta in etiquetas:
                if(self.evaluar_limite(0, etiqueta, n)):
                    columna_nueva += [etiqueta]
                    break
                if(self.evaluar_limite(1,etiquetas[largo], n)):
                    columna_nueva += [etiquetas[largo]]
                    break
                if(self.evaluar_acote(etiqueta, n)):               
                    columna_nueva += [etiqueta]
                    break
        return columna_nueva

    def evaluar_acote(self, expresion, numero):
        limites = expresion.split(" - ")
        if(("<" not in expresion) and (float(limites[0]) <= numero < float(limites[1]))):
            return True
        else:
            return False
        
    def evaluar_limite(self, tipo, expresion, numero):
        if(tipo == 0):                                              #limite inferior
            if(("<" in expresion) and (eval(str(numero) + expresion))):
                return True
            else:
                return False
        else:
            if(tipo == 1):                                          #limite superior
                if(("<" in expresion) and (eval(expresion + str(numero)))):
                    return True
                else:
                    return False
