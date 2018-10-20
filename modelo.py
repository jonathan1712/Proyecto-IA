import pandas as pd
from archivo import *
from normalizador import *


class Modelo:
    def leer_archivo(self, nombre_archivo):
        archivo = Archivo(nombre_archivo)
        archivo.leer_data_set()
        self.archivo = archivo.get_data_set()
        return self.archivo

    def normalizar(self, tipo_modelo):
        datos = Normalizador(self.archivo)
        datos.normalizar()
        if(tipo_modelo == 0): # class random_forest
            datos.num_rangos = [5 for i in range(32)]
            datos.clasificar_columnas()
        self.datos_normalizados = datos.datos
        return self.datos_normalizados

    
