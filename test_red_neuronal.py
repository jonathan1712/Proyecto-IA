from red_neuronal import *


def main():
    red_neuronal = Red_Neuronal(2,2,"softmax")
    red_neuronal.leer_archivo()
    red_neuronal.normalizar()
    red_neuronal.crear_set_datos()
    #red_neuronal.separar_set_datos()
    #red_neuronal.crear_modelo()
    #red_neuronal.entrenar_modelo()
    #red_neuronal.probar_modelo()

if __name__ == "__main__":
    main()
