from red_neuronal import *


class Cross_Validation:
    def __init__(self, k, tipo_modelo, nombre_archivo, numero_capas,
                    numero_unidades, funcion_activacion):
        self.k = k
        self.tipo_modelo = tipo_modelo
        self.nombre_archivo = nombre_archivo
        self.definir_modelo(numero_capas, numero_unidades, funcion_activacion)

    def definir_modelo(self, numero_capas, 
                        numero_unidades, funcion_activacion):
        # Red Neuronal es tipo 1
        if (self.tipo_modelo == 1):
            self.modelo = Red_Neuronal(numero_capas, 
                            numero_unidades, funcion_activacion)
            
        self.modelo.leer_archivo(self.nombre_archivo)
        self.modelo.normalizar()
        self.datos_normalizados = self.modelo.datos_normalizados

    def cross_validation(self):
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
        self.datos_entrenamiento = []
        self.datos_prueba = []
        extremo_derecho = ((fold+1) * n) - 1
        extremo_izquierdo = extremo_derecho - n + 1
        for i in range(len(self.datos_normalizados)):
            if not (i >= extremo_izquierdo and i <= extremo_derecho):
                self.datos_entrenamiento.append(np.array(self.datos_normalizados.loc[i]))
            else:
                self.datos_prueba.append(np.array(self.datos_normalizados.loc[i]))
