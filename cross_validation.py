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
        self.k = 3 #dejarlo fijo
        self.tipo_modelo = tipo_modelo
        self.nombre_archivo = "data_set.csv" #Dejarlo fijo tambian
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
            poda = argumentos[1]
            self.modelo = Random_Forest(num_arboles, self.modelo.da)
            
        self.modelo.leer_archivo(self.nombre_archivo)
        self.modelo.normalizar()
        #if(self.tipo_modelo != 1):
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
            print(self.modelo.predecir())
        print("***Tasa de error Testing: {}".format(fold_errT / self.k))
        print("***Tasa de error Validation: {}".format(fold_errV / self.k))

    def particionar(self, fold, k, n):
        self.datos_entrenamiento = []
        self.datos_prueba = []
        self.datos_prediccion = []
        n_pruebas= (round(n * self.porcentaje_pruebas))
        extremo_derecho = ((fold+1) * n) - 1
        extremo_izquierdo = extremo_derecho - n + 1
        for i in range(len(self.datos_normalizados)):
            if not (i >= extremo_izquierdo and i <= extremo_derecho):
                self.datos_entrenamiento.append(np.array(self.datos_normalizados.loc[i]))
            else:
                if (len(self.datos_prueba)==n_pruebas):
                    self.datos_prediccion.append(np.array(self.datos_normalizados.loc[i]))
                else: 
                    self.datos_prueba.append(np.array(self.datos_normalizados.loc[i]))
