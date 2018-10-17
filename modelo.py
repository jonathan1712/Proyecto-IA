import pandas as pd
from Archivo.archivo import *
from Normalizador.Normalizador import *
from red_neuronal import *


class Modelo:
    def __init__(self, tipo_modelo, nombre_archivo):
        self.tipo_modelo = tipo_modelo
        
    def leer_archivo(self, nombre_archivo):
        archivo = Archivo(nombre_archivo)
        archivo.leer_data_set()
        self.archivo = archivo.get_data_set()

    def normalizar(self):
        datos = Normalizador(self.archivo)
        datos.normalizar()
        self.datos_normalizados = datos.datos

    
