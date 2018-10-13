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

    def separar_set_datos(self):
        self.entrenamiento_x = self.set_datos.iloc[:, 1:30]
        self.entrenamiento_y = self.set_datos.iloc[:, 30]

        self.prueba_x = self.set_datos.iloc[:, 1:30]
        self.prueba_y = self.set_datos.iloc[:, 30]

        #Codificando set de datos entrenamiento
        self.codificado_entrenamiento_y = np_utils.to_categorical(self.entrenamiento_y)

        #Codificando set de datos entrenamiento
        self.codificado_prueba_y = np_utils.to_categorical(self.prueba_y)

    def crear_modelo(self):
        self.modelo = Sequential()
        self.modelo.add(Dense(self.unidades_capa, input_dim=29, activation=self.funcion_activacion))
        for i in range (self.numero_capas-1):
            self.modelo.add(Dense(self.unidades_capa, activation=self.funcion_activacion))

    def entrenar_modelo(self):
        #Compilar el modelo
        self.modelo.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

        #Entrenar el modelo
        self.modelo.fit(self.entrenamiento_x, self.codificado_entrenamiento_y)

    def probar_modelo(self):
        scores = self.modelo.evaluate(self.prueba_x, self.codificado_prueba_y)
        print("\nAccuracy: %.2f%%" % (scores[1]*100))



    

