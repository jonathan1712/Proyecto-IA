import csv
import numpy as np
import pandas as pd
class Archivo:
    nombreArchivo = ""
    titulos = []
    datos = []
    
    ### Constructor
    def __init__(self, nombre):
        self.nombreArchivo = nombre

    ### Set Valores
    def setValores(self, titulos, datos):
        self.titulos = titulos
        self.datos =  datos

    ### Get Datos
    def getDatos(self):
        return self.data_set

    def escribirArchivoM(self, datos):
        f = open("demofile.txt", "w")
        for fila in datos:
            f.write(str(fila))
        
    def leerArchivo(self):
        self.data_set = pd.read_csv(self.nombreArchivo)                         #se carga el archivo
        columna_prediccion = self.data_set["diagnosis"]                         #se extrae la columna de resultado
        self.data_set = self.data_set.drop("id", axis = 1)                      #se elimina la columna de id
        self.data_set = self.data_set.drop("diagnosis", axis = 1)               #se elimina la columna de resultado "diagnosis"
        self.data_set["diagnosis"] = columna_prediccion                         #se inserta de nuevo la columna de resultado, pero al final (derecha)
        self.data_set.replace({'diagnosis': {"B": 1, "M": 0}},  inplace = True) #se reemplazan los valores de B y M por 1,0 respectivamente

    ### Ver el contenido del archivo
    def verArchivo(self):
        print (self.titulos)
        for fila in self.datos:
            print(fila)

