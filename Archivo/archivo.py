import csv
import pandas as pd


class Archivo:

    # Constructor
    def __init__(self, nombre):
        self.nombre_archivo = nombre

    # Obtener data_set
    def get_data_set(self):
        return self.data_set

    # Escribir un archivo csv, con un nombre y ciertos datos
    def escribir_archivo_csv(self, datos, nombre_archivo):
        try:
            datos.to_csv(nombre_archivo, sep=',')
            return True
        except:
            return False

    # Lee el data set de proyecto
    def leer_data_set(self):
        try:
            self.data_set = pd.read_csv(self.nombre_archivo)
            columna_prediccion = self.data_set["diagnosis"]
            # Se extrae la columna de resultado
            self.data_set = self.data_set.drop("id", axis=1)
            # Se elimina la columna de id
            self.data_set = self.data_set.drop("diagnosis", axis=1)
            # Se elimina la columna de resultado "diagnosis"
            self.data_set["diagnosis"] = columna_prediccion
            # Se inserta de nuevo la columna de resultado (final)
            ultima_fila = {'diagnosis': {"B": 1, "M": 0}}
            self.data_set.replace(ultima_fila, inplace=True)
            # Se reemplazan los valores de B y M por 1,0 respectivamente
            return True
        except:
            return False
