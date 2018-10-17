from Normalizador import *
def main():
    archivo = [[3,4,5,6,1],
               [1,5,1,8,0],
               [2,3,4,3,1],
               [3,5,6,4,0],
               [1,5,1,8,0],
               [2,3,4,3,1],
               [3,5,6,4,0]]
    
    prueba = Normalizador(archivo)
    prueba.normalizar()
    print(prueba.datos)


if __name__ == "__main__":
    main()
