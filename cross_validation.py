from modelo import *


class Cross_Validation:
    def __init__(self, k, tipo_modelo, nombre_archivo="prueba.csv"):
        self.k = k
        self.tipo_modelo = tipo_modelo
        self.modelo = Modelo(tipo_modelo, nombre_archivo)
        self.datos_normalizados = self.modelo.datos_normalizados

    def cross_validation(self):
        fold_errT = 0
        fold_errV = 0
        n = len(self.datos_normalizados) // self.k
        print(n)
        for fold in range(self.k):
            self.particionar(fold, self.k, n)
            if (self.tipo_modelo != "prueba"):
                errT = self.modelo.red_neuronal(self.datos_entrenamiento,
                                                self.datos_prueba)
                fold_errT = fold_errT + errT
            else:
                print('********* k = ' + str(fold) + "********* ")
                print("Entrenamiento: " + str(self.datos_entrenamiento))
                print("Prueba: " + str(self.datos_prueba))
                print()
                fold_errT = 100 * self.k
        print("***Promedio acierto: " + str(fold_errT / self.k))

    def particionar(self, fold, k, n):
        self.datos_entrenamiento = []
        self.datos_prueba = []
        extremo_derecho = ((fold+1) * n) - 1
        extremo_izquierdo = extremo_derecho - n + 1
        for i in range(len(self.datos_normalizados)):
            if not (i >= extremo_izquierdo and i <= extremo_derecho):
                self.datos_entrenamiento.append(
                    list(self.datos_normalizados[i]))
            else:
                self.datos_prueba.append(list(self.datos_normalizados[i]))
