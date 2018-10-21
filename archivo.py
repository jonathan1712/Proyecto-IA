import pandas as pd


class Archivo:

    # Constructor
    def __init__(self, nombre):
        self.nombre_archivo = nombre

    def get_data_set(self):
        """ get_data_set
        Retorna el data_set del actual archivo
        """
        return self.data_set

    def escribir_archivo_csv(self, datos, nombre_archivo):
        """ escribir_archivo_csv
        Dado un dataframe se escribe en un archivo
        """

        try:
            datos.to_csv(nombre_archivo, sep=',')
            return True
        except:
            return False

    def leer_data_set(self):
        """ leer_data_set
        Abre el archivo del dataset y hace el tratamiento respectivo
        para poderlo procesar y normalizarlo
        """

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

    def abrir_archivo(self):
        """ abrir_archivo
        Crea un puntero a un archivo, en el cual se va a escribir
        estádisticas
        """

        self.puntero = open(self.nombre_archivo, 'w')

    def escribir_linea(self, contenido):
        """ escribir_linea
        Escribe una línea en un archivo dado un puntero
        """

        self.puntero.writelines(contenido)

    def cerrar_archivo(self):
        """ cerrar_archivo
        Cierra un archivo dado un puntero
        """

        self.puntero.close()
