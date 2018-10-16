from Nodo import *
def main():
    """
    arreglo = [[1,2,3,1],
               [4,8,6,1],
               [4,8,6,1],
               [4,1,2,0]]
    """
    arreglo = [[1,2,6,7,3,2,0],
               [4,2,6,1,3,5,1],
               [4,2,6,7,3,5,0],
               [4,1,2,5,2,5,1],
               [7,1,2,7,1,2,1],
               [4,2,3,1,3,2,1],
               [7,1,6,6,2,5,0],
               [4,1,2,6,2,2,1]]

    particiones = [[[1,2,3,1]],[[1,2,3,1]],[[3,4,5,0],[3,4,5,1]]]
    nombre = "prueba"
    nodo = Nodo()
    nodo.agregarElemento(particiones,nombre)
    nodo.verHojas()



if __name__ == "__main__":
    main()
