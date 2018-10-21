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
        """ learner
        Función de aprendizaje, dado un conjunto de datos de
        entrenamiento la red neuronal se entrena
        """

        self.crear_modelo()
        self.entrenar_modelo(datos_entrenamiento)

    def crear_modelo(self):
        """ crear_modelo
        Se configuran las características de la red, esto implica
        asignar la cantidad de capas y unidades por capa
        Se hace un ciclo, donde cada iteración se crea una nueva
        capa
        """

        self.modelo = Sequential()
        self.capas = self.numero_capas - 2
        self.modelo.add(Dense(units=self.unidades_capa,
                              input_shape=(30, ),
                              activation=self.funcion_activacion))
        while(self.capas > 0):
            self.modelo.add(Dense(units=self.unidades_capa,
                                  activation=self.funcion_activacion))
            self.capas = self.capas - 1
        self.modelo.add(Dense(units=2,
                              activation=self.funcion_activacion))

    def entrenar_modelo(self, datos_entrenamiento):
        """ entrenar_modelo
        Una vez creado el modelo, se seleccionan los datos de
        entrenamiento y son ingresados en la red, de manera que,
        esta sea capaz, posteriormente de dar resultados óptimos.
        El primer paso antes de entrenar es compilar el modelo.
        """

        self.set_datos_entrenamiento = datos_entrenamiento
        self.crear_set_datos_entrenamiento()
        # Compilar el modelo
        self.modelo.compile(loss='binary_crossentropy',
                            optimizer='rmsprop', metrics=['accuracy'])
        # Entrenar el modelo
        self.modelo.fit(self.datos_entrenamiento_x,
                        self.codificado_datos_entrenamiento_y,
                        epochs=300, batch_size=10)

    def probar_modelo(self, datos_prueba):
        """ probar_modelo
        Se brindan los datos de prueba y se evaluan sobre el modo creado
        previamente. El retorno de la función es un porcentaje de error
        de la prueba
        """

        self.set_datos_prueba = datos_prueba
        self.crear_set_datos_prueba()
        scores = self.modelo.evaluate(self.datos_prueba_x,
                                      self.codificado_datos_prueba_y)
        return (1- scores[1])

    def predecir(self, datos_prediccion):
        """ predecir
        Dado un conjunto de datos de predicción, estos se aplican al
        modelo y se obtiene su respuesta y la tasa de error de
        predicción
        """

        pred_error = 0
        res = []
        pred = []
        self.datos_prediccion_x = datos_prediccion.iloc[:, 0:30].values
        self.datos_prediccion_y = datos_prediccion.iloc[:, 30].values
        prediccion = self.modelo.predict(self.datos_prediccion_x, batch_size=None,
                                         verbose=1, steps=None)
        pred = self.normalizar_datos_prediccion(prediccion)
        lista_a = []
        for b in pred:
            if(b==0):
                lista_a.append("M")
            else:
                lista_a.append("B")
        for i in range(len(pred)):
            if not(pred[i] == self.datos_prediccion_y[i]):  # prediccion ok?
                pred_error = pred_error + 1
        res.append(pred_error / len(pred))
        res.append(lista_a)

        return res

    def normalizar_datos_prediccion(self, prediccion):
        """
        Recibe el arreglo de prediccion [[0.999],[0.321111]]
        y lo normaliza a binario [[1][0]]
        """
        pred = []

        for i in range(len(prediccion)):
            prediccion[i] = np.round(prediccion[i]*10, decimals=-1)
            prediccion[i] = prediccion[i]/10
            pred.append(prediccion[i][1])
        return pred

    def crear_set_datos_entrenamiento(self):
        """ crear_set_datos_entrenamiento
        Se toma los datos de entrenamiento del modelo para generar un
        dataframe de pandas, el cual permite manipular los datos con
        mayor facilidad
        """

        self.datos_entrenamiento_x = self.set_datos_entrenamiento.iloc[:, 0:30].values
        self.datos_entrenamiento_y = self.set_datos_entrenamiento.iloc[:, 30].values
        # Codificando set de datos entrenamiento
        self.codificado_datos_entrenamiento_y = np_utils.to_categorical(self.datos_entrenamiento_y)

    def crear_set_datos_prueba(self):
        """ crear_set_datos_prueba
        Se toman los datos de prueba del modelo para generar un
        dataframe de pandas, el cual permite manipular los datos con
        mayor facilidad
        """

        self.datos_prueba_x = self.set_datos_prueba.iloc[:, 0:30].values
        self.datos_prueba_y = self.set_datos_prueba.iloc[:, 30].values
        # Codificando set de datos entrenamiento
        self.codificado_datos_prueba_y = np_utils.to_categorical(self.datos_prueba_y)
