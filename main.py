from inicializador import *
from cross_validation import *

def main():
    parametros = obtener_parametros()
    cross_validation = Cross_Validation(parametros[0],
                                        parametros[1],
                                        parametros[2],
                                        parametros[3])
    cross_validation.cross_validation()

if __name__ == "__main__":
    main()