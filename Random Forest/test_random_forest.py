from random_forest import *
import pandas as pd


def test_crear_bootstrapped():
    are = [0, 0, 1, 2, 2, 2, 1, 0, 0, 2, 0, 1, 1, 2]
    pre = [0, 0, 0, 1, 2, 2, 2, 1, 2, 1, 1, 1, 0, 1]
    hum = [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0]
    rad = [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1]
    dia = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0]
    df = pd.DataFrame({'area': are,
                       'perimeter': pre,
                       'hum': hum,
                       'radio': rad,
                       'diagnosis': dia})
    # En el constructor se llama a crear_bootstrapped
    random_forest = Random_Forest(10, df)
    random_forest.crear_bootstrapped()

    # Se prueba que el bootstrapped no está vacío
    assert(len(random_forest.bootstrapped.index) != 0)
    # Prueba: el bootstrapped tiene el mismo tamaño que el data frame original
    assert(len(random_forest.bootstrapped.index == len(df.index)))


def test_crear_forest():
    are = [0, 0, 1, 2, 2, 2, 1, 0, 0, 2, 0, 1, 1, 2]
    pre = [0, 0, 0, 1, 2, 2, 2, 1, 2, 1, 1, 1, 0, 1]
    hum = [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0]
    rad = [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1]
    dia = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0]
    df = pd.DataFrame({'area': are,
                       'perimeter': pre,
                       'hum': hum,
                       'radio': rad,
                       'diagnosis': dia})
    # 10 = Número de cantidad de árboles
    random_forest = Random_Forest(10, df)
    random_forest.crear_forest()

    # Se prueba que el arreglo de árboles no está vacío
    assert(len(random_forest.forest) != 0)
    # El random.forest posee exactamente la cantidad de árboles solicitados
    assert(len(random_forest.forest) == 10)
    # El random.forest posee exactamente la cantidad de árboles solicitados
    assert(len(random_forest.forest) != 9)


def test_evaluar_fila_forest():
    # La prueba es un poco compleja, asi que se supone un # de árboles = 1
    # Para efectos prácticos True = Benigno, False = Maligno
    # Se genera el siguiente
    """
    R  ->  Windy
        0  ->  Hum
            1  ->  True
            0  ->  False
        1  ->  Outlook
            1  ->  False
            0  ->  True
    """
    # Creación del Random Forest
    random_forest = Random_Forest(0, None)

    # Creación manual del árbol
    arbol = Arbol()

    # Raiz
    nodo_raiz = Nodo()
    nodo_raiz.etiqueta = "R  ->  Windy"
    nodo_raiz.nombre = "Windy"

    # Hum
    nodo_hum = Nodo()
    nodo_hum.etiqueta = "0  ->  Hum"
    nodo_hum.nombre = "Hum"
    nodo_hum.enlace = 0

    nodo_hum.agregar_hoja([True, 1])
    nodo_hum.agregar_hoja([False, 0])

    # Outlook
    nodo_out = Nodo()
    nodo_out.etiqueta = "1  ->  Outlook"
    nodo_out.nombre = "Outlook"
    nodo_out.enlace = 1

    nodo_out.agregar_hoja([True, 0])
    nodo_out.agregar_hoja([False, 1])

    # Agregar nodos
    nodo_raiz.agregar_nodo(nodo_hum)
    nodo_raiz.agregar_nodo(nodo_out)
    arbol.raiz = nodo_raiz

    # Línea evaluar
    de = pd.DataFrame({'Outlook': [0],
                       'Temp': [2],
                       'Hum': [1],
                       'Windy': [0],
                       'diagnosis': [0]})
    resultado = random_forest.evaluar_fila_forest(de)

    # Se verifica el resultado esperado
    assert(resultado == 'Benigno')
    # Se verifica que efectivamente el resultado es correcto
    assert(resultado != 'Maligno')
