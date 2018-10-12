from red_neuronal import *
def main():
    red_neuronal = Red_Neuronal(8,2,"relu")
    red_neuronal.leer_archivo()
    red_neuronal.normalizar()
    red_neuronal.crear_set_datos()


if __name__ == "__main__":
    main()
