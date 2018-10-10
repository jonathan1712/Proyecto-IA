import numpy as np
import pandas as pd
from scipy import stats
class Normalizador:
    
    def __init__(self, datos):
        self.datos = np.array(datos)
    
    def normalizar(self):
        columnas = np.size(self.datos,1)
        for i in range(columnas-1):                 # -1 para no normalizar la columna de la respuesta
            columna = np.array([])
            columna = self.datos[:,[i]]
            columna = [float(ind) for ind in columna]
            columna = np.array(columna)
            columna = self.zcore(columna)
            self.datos[:,i] = columna

    def zcore(self, columna):
        media = np.mean(columna)
        desviacion = np.std(columna)
        columna = stats.zscore(columna)
        return columna

    def eliminarColumnas(self):
        self.datos = np.delete(self.datos, 0,1)

    def verDatos(self):
        print (self.datos)
    


 
