from red_neuronal import *
from random_forest import *
import pandas as pd


class Cross_Validation:

    def __init__(self, tipo_modelo, porcentaje_pruebas, prefijo, argumentos):
        # dejarlo fijo
        self.k = 3
        self.tipo_modelo = tipo_modelo
        # dejarlo fijo también
        self.nombre_archivo = "data_set.csv"
        self.porcentaje_pruebas = porcentaje_pruebas
        self.prefijo = prefijo
        self.definir_modelo(argumentos)

    def definir_modelo(self, argumentos):
        """ definir_modelo
        Según los parámetros enviados al programa se selecciona
        el tipo de modelo que corresponde. Esto es posible gracias
        a la herencia implementada
        """

        # Red Neuronal es tipo 1
        if (self.tipo_modelo == 1):
            numero_capas = argumentos[0]
            numero_unidades = argumentos[1]
            funcion_activacion = argumentos[2]
            self.modelo = Red_Neuronal(numero_capas,
                                       numero_unidades,
                                       funcion_activacion)
        else:
            num_arboles = argumentos[0]
            poda = argumentos[1]    # no utilizable por el momento
            self.modelo = Random_Forest(num_arboles)

        self.modelo.leer_archivo(self.nombre_archivo)
        self.modelo.normalizar(self.tipo_modelo)
        self.datos_normalizados = self.modelo.datos_normalizados

    def cross_validation(self):
        """ cross_validation
        Es la función principal, en primer lugar se encarga de resguardar
        los datos de las predicciones, y posteriormente con los datos
        restantes aplica el proceso conocido como K-Fold cross validation
        El objetivo de la función es determinar los porcentajes de error
        de las pruebas, de evaluación y primordialmente de las predicciones
        """

        self.sacar_prediccion()
        fold_errT = 0
        fold_errV = 0
        n = len(self.datos_normalizados) // self.k
        archivo = Archivo(self.prefijo + "_datos_estadisticos.txt")
        archivo.abrir_archivo()
        archivo.escribir_linea("Modelo: " + self.modelo.__class__.__name__ + "\n")
        archivo.escribir_linea("K-Fold Validation de: " + str(self.k) + "\n")

        for fold in range(self.k):
            archivo.escribir_linea("** K-Fold: " + str(fold) + " **" + "\n")
            self.particionar(fold, self.k, n)
            self.modelo.learner(self.datos_entrenamiento)
            errV = self.modelo.probar_modelo(self.datos_entrenamiento)
            errT = self.modelo.probar_modelo(self.datos_prueba)
            fold_errT = fold_errT + errT
            fold_errV = fold_errV + errV
            archivo.escribir_linea("    Error de Validacion             -> " + str(errV) + "\n")
            archivo.escribir_linea("    Error de Testing                -> " + str(errT) + "\n")
            archivo.escribir_linea("    Fold error validacion actual    -> " + str(fold_errV) + "\n")
            archivo.escribir_linea("    Fold error testing actual       -> " + str(fold_errT) + "\n")

        resultados_predicciones = self.modelo.predecir(self.datos_prediccion)
        archivo.escribir_linea("-------------------------------------------------------------\n")
        archivo.escribir_linea("-> Promedio error testing:    " + str(fold_errT / self.k) + "\n")
        archivo.escribir_linea("-> Promedio error validacion: " + str(fold_errV / self.k) + "\n")
        archivo.escribir_linea("-> Promedio error prediccion: " + str(resultados_predicciones[0]) + "\n")
        archivo.cerrar_archivo()
        print("***Promedio error Testing: " + str(fold_errT / self.k))
        print("***Promedio error Validation: " + str(fold_errV / self.k))
        print("***Promedio error Predicción: " + str(resultados_predicciones[0]))
        self.escribir_archivo_prediccion(resultados_predicciones[1])

    def escribir_archivo_prediccion(self, predicciones):
        """ escribir_archivo_prediccion
        Agrega una columna extra al dataframe de pandas donde se maneja el
        resultado de las predicciones, de forma que se puede comparar el
        valor real con el predicho
        """

        self.datos_prediccion = self.datos_prediccion.drop('index', axis=1)
        self.datos_prediccion['Prediccion'] = predicciones
        archivo = Archivo(self.prefijo + "_prediccion.csv")
        archivo.escribir_archivo_csv(self.datos_prediccion, archivo.nombre_archivo)

    def particionar(self, fold, k, n):
        """ particionar
        Crea un dataframe para datos de entrenamiento y datos de pruebas,
        de manera que, su manejo pueda ser llevado a cabo por el modelo
        """

        self.datos_entrenamiento = pd.DataFrame(columns=self.datos_normalizados.columns)
        self.datos_prueba = pd.DataFrame(columns=self.datos_normalizados.columns)
        extremo_derecho = ((fold+1) * n) - 1
        extremo_izquierdo = extremo_derecho - n + 1
        for i in range(len(self.datos_normalizados)):
            if not (i >= extremo_izquierdo and i <= extremo_derecho):
                self.datos_entrenamiento.loc[i] = self.datos_normalizados.iloc[i]
            else:
                self.datos_prueba.loc[i] = self.datos_normalizados.iloc[i]

    def sacar_prediccion(self):
        """ sacar_prediccion
        Dado un modelo se obtienen las predecciones
        de la misma, y se normalizan los resultados
        """

        self.datos_prediccion = pd.DataFrame(columns=self.datos_normalizados.columns)
        n = (round(len(self.datos_normalizados) * self.porcentaje_pruebas))
        for i in range(n):
            numero = random.randint(0, len(self.datos_normalizados) - 1)
            self.datos_prediccion.loc[i] = self.datos_normalizados.iloc[numero]
            self.datos_normalizados = self.datos_normalizados.drop(self.datos_normalizados.index[[numero]])
