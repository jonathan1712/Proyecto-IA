from modelo import *


def main():
    modelo = Modelo("red_neuronal", "prueba.csv")
    datos_entrenamiento = modelo.datos_normalizados[50:]
    datos_prueba = modelo.datos_normalizados[0:50]
    modelo.red_neuronal(datos_entrenamiento, datos_prueba)

if __name__ == "__main__":
    main()
