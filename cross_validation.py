from red_neuronal import *
from random_forest import *
import pandas as pd


class Cross_Validation:

    def __init__(self, tipo_modelo, porcentaje_pruebas, prefijo, argumentos):
        self.k = 3 #dejarlo fijo
        self.tipo_modelo = tipo_modelo
        self.nombre_archivo = "data_set.csv" #Dejarlo fijo también
        self.porcentaje_pruebas = porcentaje_pruebas
        self.prefijo = prefijo
        self.definir_modelo(argumentos)

    def definir_modelo(self,  argumentos):
        # Red Neuronal es tipo 1
        if (self.tipo_modelo == 1):
            numero_capas = argumentos[0]
            numero_unidades = argumentos[1]
            funcion_activacion = argumentos[2]
            self.modelo = Red_Neuronal(numero_capas, 
                            numero_unidades, funcion_activacion)
        else:
            num_arboles = argumentos[0]
            poda = argumentos[1]    # no utilizable por el momento
            self.modelo = Random_Forest(num_arboles)
            
        self.modelo.leer_archivo(self.nombre_archivo)
        self.modelo.normalizar(self.tipo_modelo)            
        self.datos_normalizados = self.modelo.datos_normalizados
        
    def cross_validation(self):
        self.sacar_prediccion()
        fold_errT = 0
        fold_errV = 0
        n = len(self.datos_normalizados) // self.k
        for fold in range(self.k):
            self.particionar(fold, self.k, n)
            self.modelo.learner(self.datos_entrenamiento)
            errV = self.modelo.probar_modelo(self.datos_entrenamiento)
            errT = self.modelo.probar_modelo(self.datos_prueba)
            fold_errT = fold_errT + errT
            fold_errV = fold_errV + errV
        print("***Promedio acierto Testing: " + str(fold_errT / self.k))
        print("***Promedio acierto Validation: " + str(fold_errV / self.k))

    def particionar(self, fold, k, n):
        if(self.tipo_modelo == 1):
            self.particionar_red(fold, k,n)
        else:
            if(self.tipo_modelo == 0):
                self.particionar_forest(fold, k, n)

    def particionar_forest(self, fold, k, n):
        self.datos_entrenamiento = pd.DataFrame(columns=self.datos_normalizados.columns)
        self.datos_prueba = pd.DataFrame(columns=self.datos_normalizados.columns)
        extremo_derecho = ((fold+1) * n) - 1
        extremo_izquierdo = extremo_derecho - n + 1
        for i in range(len(self.datos_normalizados)):
            if not (i >= extremo_izquierdo and i <= extremo_derecho):
                self.datos_entrenamiento.loc[i] = self.datos_normalizados.iloc[i]
            else:
                self.datos_prueba.loc[i] = self.datos_normalizados.iloc[i]

    def particionar_red(self, fold, k, n):
        self.datos_entrenamiento = []
        self.datos_prueba = []
        extremo_derecho = ((fold+1) * n) - 1
        extremo_izquierdo = extremo_derecho - n + 1
        for i in range(len(self.datos_normalizados)):
            if not (i >= extremo_izquierdo and i <= extremo_derecho):
                self.datos_entrenamiento.append(np.array(self.datos_normalizados.iloc[i]))
            else:
                self.datos_prueba.append(np.array(self.datos_normalizados.iloc[i]))
    
    def sacar_prediccion(self):
        if(self.tipo_modelo==1):
            self.sacar_prediccion_red()
        else:
            self.sacar_prediccion_forest()

    def sacar_prediccion_red(self):
        self.datos_prediccion = []
        n = (round(len(self.datos_normalizados) * self.porcentaje_pruebas))
        for i in range (n):
            numero = random.randint(0, len(self.datos_normalizados) - 1)
            self.datos_prediccion.append(np.array(self.datos_normalizados.iloc[numero]))
            self.datos_normalizados = self.datos_normalizados.drop(self.datos_normalizados.index[[numero]])

    def sacar_prediccion_forest(self):
        self.datos_prediccion = pd.DataFrame(columns=self.datos_normalizados.columns)
        n = (round(len(self.datos_normalizados) * self.porcentaje_pruebas))
        for i in range (n):
            numero = random.randint(0, len(self.datos_normalizados) - 1)
            self.datos_prediccion.loc[i] = self.datos_normalizados.iloc[numero]
            self.datos_normalizados = self.datos_normalizados.drop(self.datos_normalizados.index[[numero]])
