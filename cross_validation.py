from red_neuronal import *


class Cross_Validation:
    """
    def __init__(self, k, tipo_modelo, nombre_archivo, numero_capas,
                    numero_unidades, funcion_activacion):
        self.k = k
        self.tipo_modelo = tipo_modelo
        self.nombre_archivo = nombre_archivo
        self.definir_modelo(numero_capas, numero_unidades, funcion_activacion)
    """

    def __init__(self, tipo_modelo, porcentaje_pruebas, prefijo, argumentos):
        self.k = 5 #dejarlo fijo
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
            num_arboles = 5 # cambiar
            self.modelo = Random_Forest(num_arboles, self.modelo.da)
            
        self.modelo.leer_archivo(self.nombre_archivo)
        self.modelo.normalizar()
        self.datos_normalizados = self.modelo.datos_normalizados
        
    def cross_validation(self):
        fold_errT = 0
        fold_errV = 0
        n = len(self.datos_normalizados) // self.k
        n_pruebas= (round(n * porcentaje_pruebas))
        n_prediccion = n - n_pruebas
        for fold in range(self.k):
            self.particionar(fold, self.k, n_pruebas)
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
        self.datos_prediccion = []
        extremo_derecho = ((fold+1) * n) - 1
        extremo_izquierdo = extremo_derecho - n + 1
        for i in range(len(self.datos_normalizados)):
            if not (i >= extremo_izquierdo and i <= extremo_derecho):
                self.datos_entrenamiento.append(np.array(self.datos_normalizados.loc[i]))
            else:
                if (len(self.datos_prueba)==n):
                    self.datos_prediccion.append(np.array(self.datos_normalizados.loc[i]))
                else: 
                    self.datos_prueba.append(np.array(self.datos_normalizados.loc[i]))
