import pandas as pd
from Archivo.Archivo import *
from Normalizador.Normalizador import *
from red_neuronal import *

class Cross_Validation:
    def __init__(self, k, modelo):
        self.k = k
        self.tipo_modelo = modelo

    def leer_archivo(self):
        self.archivo = Archivo("prueba.csv")
        self.archivo.leerArchivo()
        self.archivo = self.archivo.getDatos()

    def normalizar(self):
        datos = Normalizador(self.archivo)
        datos.normalizar()
        self.datos_normalizados = datos.datos

    def crear_set_datos_entrenamiento(self):
        nombres_columnas= ["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst","diagnosis"]
        self.set_datos_entrenamiento= pd.DataFrame(self.entrenamiento, columns=nombres_columnas)

    def crear_set_datos_prueba(self):
        nombres_columnas= ["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst","diagnosis"]
        self.set_datos_prueba= pd.DataFrame(self.prueba, columns=nombres_columnas)

    def separar_set_datos(self):
        self.entrenamiento_x = self.set_datos_entrenamiento.iloc[:, 1:30]
        self.entrenamiento_y = self.set_datos_entrenamiento.iloc[:, 30]

        self.prueba_x = self.set_datos_prueba.iloc[:, 1:30]
        self.prueba_y = self.set_datos_prueba.iloc[:, 30]

        #Codificando set de datos entrenamiento
        self.codificado_entrenamiento_y = np_utils.to_categorical(self.entrenamiento_y)

        #Codificando set de datos entrenamiento
        self.codificado_prueba_y = np_utils.to_categorical(self.prueba_y)
 
    def cross_validation(self):
        fold_errT = 0
        fold_errV = 0
        n=len(self.datos_normalizados) // self.k
        print(n)
        for fold in range(self.k):
            self.particionar(fold, self.k, n)
            if (self.tipo_modelo == "red_neuronal"):
                self.red()
            else:
                print('********* k = ' + str(fold) + "********* ")
                print("Entrenamiento: " + str(self.entrenamiento))
                print("Prueba: " + str(self.prueba))
                print()
                
    def particionar(self, fold, k, n):
        self.entrenamiento = []
        self.prueba = []
        extremo_derecho = ((fold+1) * n) -1
        extremo_izquierdo = extremo_derecho - n +1
        for i in range(len(self.datos_normalizados)):
            if not (i >= extremo_izquierdo and i <= extremo_derecho):
                self.entrenamiento.append(list(self.datos_normalizados[i]))
            else:
                self.prueba.append(list(self.datos_normalizados[i]))
            
    def red(self):
        self.crear_set_datos_entrenamiento()
        self.crear_set_datos_prueba()
        self.separar_set_datos()
        red_neuronal = Red_Neuronal(2,2,"softmax")
        red_neuronal.entrenamiento_x = self.entrenamiento_x
        red_neuronal.entrenamiento_y = self.entrenamiento_y
        red_neuronal.prueba_x = self.prueba_x
        red_neuronal.prueba_y = self.prueba_y
        red_neuronal.codificado_entrenamiento_y = self.codificado_entrenamiento_y
        red_neuronal.codificado_prueba_y = self.codificado_prueba_y
        
        red_neuronal.crear_modelo()
        red_neuronal.entrenar_modelo()
        red_neuronal.probar_modelo()
        
    
