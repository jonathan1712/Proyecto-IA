from Archivo import *
from Normalizador import *
from Arbol import *
def main():
    archivo = Archivo("data1.csv")
    archivo.leerArchivo()
    d = archivo.getDatos()
    #print(archivo.getDatos())
    lista = []
    for i in range(32):
        lista.append(3)


    x = Normalizador(archivo.getDatos(),lista)
    x.normalizar()
    #x.verDatos()
    x.clasificarColumnas()
    #x.verDatos()
    """archivo.escribirArchivoM(x.datos)
    """
    arbol = Arbol()
    arbol.crear_arbol(x.datos)
    arbol.ver_arbol()
    #archivo.escribirArchivoM(x.datos)


if __name__ == "__main__":
    main()