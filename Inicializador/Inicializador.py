import argparse


def inicializador():
    parser = argparse.ArgumentParser(description='Inicializador del ' + 
                                    ' cross validation.')
    grupo_raiz = parser.add_mutually_exclusive_group()

    grupo_arbol = grupo_raiz.add_mutually_exclusive_group()
    grupo_arbol.add_argument("-na", "--numero-arboles", type=int,
                        help="Cantidad de arboles para el Random Forest",
                        default=0)

    grupo_red = grupo_raiz.add_mutually_exclusive_group()
    grupo_red.add_argument("-rn", "--red-neuronal", action="store_true",
                        help="Ejecutar la red nueronal")
    sub_grupo_red = grupo_red.add_argument_group()
    sub_grupo_red.add_argument("-nc", "--numero-capas", type=int,
                        help="Cantidad de capas",
                        default=0)
    sub_grupo_red.add_argument("-upc", "--unidades-por-capa", type=int,
                        help="Numero unidades por capa",
                        default=0)
    sub_grupo_red.add_argument("-fa", "--funcion-activacion", type=int,
                        help="Seleccionar la funcion de activacion",
                        default=0)
    
    args = parser.parse_args()

    if args.red_neuronal:
        red_neuronal(args.numero_capas, 
                     args.unidades_por_capa,
                     args.funcion_activacion)
    else:
        random_forest(args.numero_arboles)


def random_forest(arboles):
    print("llamar funcion de random forest con "+ str(arboles) + " cantidad de arboles")


def red_neuronal(capas, unidades, funcion):
    print("llamar funcion red neuronal con {} capas, {} unidades y {} funcion".format(
            capas, unidades, funcion))


if __name__ == "__main__":
    inicializador()

