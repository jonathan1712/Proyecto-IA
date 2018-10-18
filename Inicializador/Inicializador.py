import argparse


def inicializador():
    parser = argparse.ArgumentParser(description='Inicializador del ' + 
                                    ' cross validation.')
    grupo_raiz = parser.add_mutually_exclusive_group()

    grupo_arbol = grupo_raiz.add_mutually_exclusive_group()
    grupo_arbol.add_argument("-rf", "--random-forest", action="store_true",
                            help="Ejecutar el Random Forest")
    sub_grupo_arbol = grupo_arbol.add_argument_group()
    sub_grupo_arbol.add_argument("-na", "--numero-arboles", type=int,
                        help="Cantidad de arboles para el Random Forest",
                        default=51)
    sub_grupo_arbol.add_argument("-pp", "--porcentaje-pruebas", type=float,
                        help="Porcentaje de datos a utilizar para pruebas",
                        default=0.3)
    sub_grupo_arbol.add_argument("-up", "--umbral-poda", type=float,
                        help="Cantidad minima de ganancia de informacion",
                        default=-1)

    grupo_red = grupo_raiz.add_mutually_exclusive_group()
    grupo_red.add_argument("-rn", "--red-neuronal", action="store_true",
                        help="Ejecutar la red neuronal")
    sub_grupo_red = grupo_red.add_argument_group()
    sub_grupo_red.add_argument("-nc", "--numero-capas", type=int,
                        help="Cantidad de capas",
                        default=10)
    sub_grupo_red.add_argument("-upc", "--unidades-por-capa", type=int,
                        help="Numero unidades por capa",
                        default=4)
    sub_grupo_red.add_argument("-fa", "--funcion-activacion", type=str,
                        help="Seleccionar la funcion de activacion",
                        default="softmax")
    
    args = parser.parse_args()

    if args.red_neuronal:
        red_neuronal(args.numero_capas, 
                     args.unidades_por_capa,
                     args.funcion_activacion)
    else:
        random_forest(args.numero_arboles, args.umbral_poda)


def random_forest(arboles, umbral_poda):
    if umbral_poda == -1:
        print("llamar funcion de random forest con "+ str(arboles) + " cantidad de arboles")
    else:
        print("llamar funcion de random forest con {} cantidad de arboles y un umbral poda poda de {}".format(arboles, umbral_poda))


def red_neuronal(capas, unidades, funcion):
    print("llamar funcion red neuronal con {} capas, {} unidades y {} funcion".format(
            capas, unidades, funcion))


if __name__ == "__main__":
    inicializador()

