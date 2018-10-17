import csv
import pandas as pd


class Archivo:

    # Constructor
    def __init__(self, nombre):
        self.nombreArchivo = nombre

    # Obtener data_set
    def get_data_set(self):
        return self.data_set

    # Escribir un archivo csv, con un nombre y ciertos datos
    def escribir_archivo_csv(self, datos, nombre_archivo):
        datos.to_csv(nombre_archivo, sep=',')
        
    # Lee el data set de proyecto    
    def leer_data_set(self):
        self.data_set = pd.read_csv(self.nombreArchivo)                         
        columna_prediccion = self.data_set["diagnosis"]                         #se extrae la columna de resultado
        self.data_set = self.data_set.drop("id", axis = 1)                      #se elimina la columna de id
        self.data_set = self.data_set.drop("diagnosis", axis = 1)               #se elimina la columna de resultado "diagnosis"
        self.data_set["diagnosis"] = columna_prediccion                         #se inserta de nuevo la columna de resultado, pero al final (derecha)
        self.data_set.replace({'diagnosis': {"B": 1, "M": 0}},  inplace = True) #se reemplazan los valores de B y M por 1,0 respectivamente


