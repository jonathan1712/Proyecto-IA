from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
import numpy
import pandas as pd
from modelo import *


class Red_Neuronal (Modelo):
    def __init__(self, numero_capas, unidades_capa, funcion_activacion):
        self.numero_capas = numero_capas
        self.unidades_capa = unidades_capa
        self.funcion_activacion = funcion_activacion

    def learner(self, datos_entrenamiento):
        self.crear_modelo()
        self.entrenar_modelo(datos_entrenamiento)
        
    def probar(self, modelo, datos_prueba):
        self.probar_modelo(datos_prueba)

    def crear_modelo(self):
        self.modelo = Sequential()
        self.capas = self.numero_capas-2
        self.modelo.add(Dense(units = self.unidades_capa,
                              input_shape=(30,), 
                              activation=self.funcion_activacion))
        
        while(self.capas>0):
            self.modelo.add(Dense(units = self.unidades_capa,
                                  activation=self.funcion_activacion))
            self.capas = self.capas - 1

        self.modelo.add(Dense(units = 2,
                            activation=self.funcion_activacion))

    def entrenar_modelo(self, datos_entrenamiento):
        self.datos_entrenamiento = datos_entrenamiento
        self.crear_set_datos_entrenamiento()
        # Compilar el modelo
        self.modelo.compile(loss='binary_crossentropy',
                            optimizer='rmsprop', metrics=['accuracy'])

        # Entrenar el modelo
        self.modelo.fit(self.datos_entrenamiento_x,
                        self.codificado_datos_entrenamiento_y,
                        epochs=300, batch_size=10)

    def probar_modelo(self, datos_prueba):
        self.datos_prueba = datos_prueba
        self.crear_set_datos_prueba()
        scores = self.modelo.evaluate(self.datos_prueba_x,
                                     self.codificado_datos_prueba_y)
        return scores[1] * 100

    def predecir(self):
        print("-*-*-*-*-*-")
        prediccion = self.modelo.predict(self.datos_prueba_x, batch_size=None, verbose=1, steps=None)
        normalizar = Normalizador(prediccion)
        normalizar.normalizar()
        normalizar= normalizar.datos
        print(np_utils.to_categorical(normalizar))
        print("-*-*-*-*-*-")

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
        
        self.datos_entrenamiento_x = self.set_datos_entrenamiento.iloc[:, 0:30].values
        self.datos_entrenamiento_y = self.set_datos_entrenamiento.iloc[:, 30].values
        
        # Codificando set de datos entrenamiento
        self.codificado_datos_entrenamiento_y = np_utils.to_categorical(self.datos_entrenamiento_y)

    def crear_set_datos_prueba(self):
        self.set_datos_prueba = pd.DataFrame(
            self.datos_prueba, columns=self.nombres_columnas)
        
        self.datos_prueba_x = self.set_datos_prueba.iloc[:, 0:30].values
        self.datos_prueba_y = self.set_datos_prueba.iloc[:, 30].values

        # Codificando set de datos entrenamiento
        self.codificado_datos_prueba_y = np_utils.to_categorical(self.datos_prueba_y)