import pandas as pd
from Archivo.Archivo import *
from Normalizador.Normalizador import *
from red_neuronal import *


class Modelo:
    def __init__(self, tipo_modelo, nombre_archivo):
        self.tipo_modelo = tipo_modelo
        self.archivo = self.leer_archivo(nombre_archivo)
        self.datos_normalizados = self.normalizar()

    def leer_archivo(self, nombre_archivo):
        archivo = Archivo(nombre_archivo)
        archivo.leerArchivo()
        return archivo.getDatos()

    def normalizar(self):
        datos = Normalizador(self.archivo)
        datos.normalizar()
        return datos.datos

    def red_neuronal(self, datos_entrenamiento, datos_prueba):
        self.datos_entrenamiento = datos_entrenamiento
        self.datos_prueba = datos_prueba
        self.crear_sets()
        red_neuronal = Red_Neuronal(10, 2, "softmax")
        red_neuronal.datos_entrenamiento_x = self.datos_entrenamiento_x
        red_neuronal.datos_entrenamiento_y = self.datos_entrenamiento_y
        red_neuronal.datos_prueba_x = self.datos_prueba_x
        red_neuronal.datos_prueba_y = self.datos_prueba_y
        red_neuronal.codificado_datos_entrenamiento_y = self.codificado_datos_entrenamiento_y
        red_neuronal.codificado_datos_prueba_y = self.codificado_datos_prueba_y

        red_neuronal.crear_modelo()
        red_neuronal.entrenar_modelo()
        scores = red_neuronal.probar_modelo()

        # print("\nAccuracy: %.2f%%" % (scores[1] * 100))
        return scores[1] * 100

    def crear_sets(self):
        self.crear_set_datos_entrenamiento()
        self.crear_set_datos_prueba()
        self.separar_set_datos()

    def crear_set_datos_entrenamiento(self):
        self.nombres_columnas = ["radius_mean", "texture_mean",
                                 "perimeter_mean", "area_mean",
                                 "smoothness_mean", "compactness_mean",
                                 "concavity_mean", "concave points_mean",
                                 "symmetry_mean", "fractal_dimension_mean",
                                 "radius_se", "texture_se", "perimeter_se",
                                 "area_se", "smoothness_se", "compactness_se",
                                 "concavity_se", "concave points_se",
                                 "symmetry_se", "fractal_dimension_se",
                                 "radius_worst", "texture_worst",
                                 "perimeter_worst", "area_worst",
                                 "smoothness_worst", "compactness_worst",
                                 "concavity_worst", "concave points_worst",
                                 "symmetry_worst", "fractal_dimension_worst",
                                 "diagnosis"]
        self.set_datos_entrenamiento = pd.DataFrame(
            self.datos_entrenamiento, columns=self.nombres_columnas)

    def crear_set_datos_prueba(self):
        self.set_datos_prueba = pd.DataFrame(
            self.datos_prueba, columns=self.nombres_columnas)

    def separar_set_datos(self):
        self.datos_entrenamiento_x = self.set_datos_entrenamiento.iloc[:, 0:30].values
        self.datos_entrenamiento_y = self.set_datos_entrenamiento.iloc[:, 30].values

        self.datos_prueba_x = self.set_datos_prueba.iloc[:, 0:30].values
        self.datos_prueba_y = self.set_datos_prueba.iloc[:, 30].values

        # Codificando set de datos entrenamiento
        self.codificado_datos_entrenamiento_y = np_utils.to_categorical(self.datos_entrenamiento_y)

        # Codificando set de datos entrenamiento
        self.codificado_datos_prueba_y = np_utils.to_categorical(self.datos_prueba_y)
