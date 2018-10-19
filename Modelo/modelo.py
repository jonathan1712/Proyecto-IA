import pandas as pd
from Archivo.archivo import *
from Normalizador.normalizador import *


class Modelo:
    def leer_archivo(self, nombre_archivo):
        print(nombre_archivo)
        archivo = Archivo(nombre_archivo)
        archivo.leer_data_set()
        self.archivo = archivo.get_data_set()
        return self.archivo

    def normalizar(self):
        datos = Normalizador(self.archivo)
        datos.normalizar()
        self.datos_normalizados = datos.datos
        return self.datos_normalizados

    
