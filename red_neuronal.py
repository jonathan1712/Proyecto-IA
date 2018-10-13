from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
import numpy
import pandas as pd

class Red_Neuronal:
    def __init__(self, numero_capas, unidades_capa, funcion_activacion):
        self.numero_capas = numero_capas
        self.unidades_capa = unidades_capa
        self.funcion_activacion = funcion_activacion
        
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



    

