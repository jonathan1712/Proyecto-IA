from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
import numpy
import pandas as pd
from Archivo.Archivo import *
from Normalizador.Normalizador import *


class Red_Neuronal:
    def __init__(self, numero_capas, unidades_capa, funcion_activacion):
        self.numero_capas = numero_capas
        self.unidades_capa = unidades_capa
        self.funcion_activacion = funcion_activacion

    def leer_archivo(self):
        self.archivo = Archivo("prueba.csv")
        self.archivo.leerArchivo()

    def normalizar(self):
        datos = Normalizador(self.archivo.getDatos())
        datos.normalizar()
        self.datos_normalizados = datos.datos

    def crear_set_datos(self):
        nombres_columnas= ["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst","diagnosis"]
        self.set_datos= pd.DataFrame(self.datos_normalizados, columns=nombres_columnas);

