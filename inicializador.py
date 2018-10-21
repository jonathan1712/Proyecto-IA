import argparse



def obtener_parametros():
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
    sub_grupo_arbol.add_argument("-pop", "--porcentaje-prueba", type=float,
                        help="Porcentaje de datos a utilizar para pruebas",
                        default=0.3)
    sub_grupo_arbol.add_argument("-up", "--umbral-poda", type=float,
                        help="Cantidad minima de ganancia de informacion",
                        default=-1)
    sub_grupo_arbol.add_argument("-prea", "--prefijo-a", type=str,
                        help="Prefijo de archivos intermedios",
                        default="archivo_inter_a.txt")

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
    sub_grupo_red.add_argument("-pp", "--porcentaje-pruebas", type=float,
                        help="Porcentaje de datos a utilizar para pruebas",
                        default=0.3)
    sub_grupo_red.add_argument("-fa", "--funcion-activacion", type=str,
                        help="Seleccionar la funcion de activacion",
                        default="softmax")
    sub_grupo_red.add_argument("-prer", "--prefijo-r", type=str,
                        help="Prefijo de archivos intermedios",
                        default="archivo_inter_r.txt")
    
    args = parser.parse_args()

    if args.red_neuronal:
        return red_neuronal(args.numero_capas, 
                     args.unidades_por_capa,
                     args.funcion_activacion,
                     args.porcentaje_pruebas,
                     args.prefijo_r)
    else:
        return random_forest(args.numero_arboles,
                      args.umbral_poda,
                      args.porcentaje_prueba,
                      args.prefijo_a)


def random_forest(arboles, umbral_poda, porcentaje_pruebas, prefijo):
    return [0, porcentaje_pruebas, prefijo, [arboles, umbral_poda]]


def red_neuronal(capas, unidades, funcion, porcentaje_pruebas, prefijo):
    return [1, porcentaje_pruebas, prefijo, [capas, unidades, funcion]]
