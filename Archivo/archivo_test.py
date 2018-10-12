from Archivo import *
def main():
    archivo = Archivo("prueba.csv")
    archivo.leerArchivo()
    d = archivo.getDatos()
    print(archivo.getDatos())
    


if __name__ == "__main__":
    main()
