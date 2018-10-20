from arbol import *
import pandas as pd


def test_crear_arbol():
    assert(1 == 1)

def test_crear_sub_arbol():
    assert(1 == 1)

def test_generar_columnas():
    arbol = Arbol()
    cantidad = 3
    atributos = 32
    lista1 = arbol.generar_columnas(cantidad, atributos)
    lista2 = arbol.generar_columnas(cantidad, atributos)

    assert(lista1 != lista2)
    assert(len(lista1) == cantidad)
    assert(len(lista2) == cantidad)
    assert(0 <= max(lista1) < atributos)
    assert(0 <= max(lista2) < atributos)
    assert(0 <= min(lista1) < atributos)
    assert(0 <= min(lista2) < atributos)
    assert(1 == 1)


def test_columna_unica():
    arbol = Arbol()
    nodo = Nodo()
    refund = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    diagnosis = [1, 1, 0, 1, 1, 0, 1, 0, 1, 1]
    df = pd.DataFrame({'refund': refund,
                       'diagnosis': diagnosis})

    arbol.columna_unica(nodo, df, "refund")
    r1 = nodo.obtener_valor_hoja(1)
    r2 = nodo.obtener_valor_hoja(0)

    assert(r1 is True)
    assert(r2 is True)


def test_definir_eleccion():
    arbol = Arbol()
    nodo = Nodo()

    positivos1 = 10
    negativos1 = 20
    valor1 = 1

    positivos2 = 20
    negativos2 = 10
    valor2 = 2

    positivos3 = 10
    negativos3 = 10
    valor3 = 3

    arbol.definir_eleccion(positivos1, negativos1, valor1, nodo)
    arbol.definir_eleccion(positivos2, negativos2, valor2, nodo)
    arbol.definir_eleccion(positivos3, negativos3, valor3, nodo)

    valor_hoja1 = nodo.obtener_valor_hoja(valor1)
    valor_hoja2 = nodo.obtener_valor_hoja(valor2)
    valor_hoja3 = nodo.obtener_valor_hoja(valor3)

    assert(valor_hoja1 is False)
    assert(valor_hoja2 is True)
    assert(valor_hoja3 in [True, False])


def test_get_prediccion():
    arbol = Arbol()
    refund = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    marital = [0, 1, 0, 1, 2, 1, 2, 0, 1, 0]

    diag1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    df1 = pd.DataFrame({'refund': refund,
                        'marital': marital,
                        'diagnosis': diag1})

    diag2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    df2 = pd.DataFrame({'refund': refund,
                        'marital': marital,
                        'diagnosis': diag2})

    assert(arbol.get_prediccion(df1) is True)
    assert(arbol.get_prediccion(df2) is False)


def test_get_nombre_columnas():
    arbol = Arbol()
    refund = [1, 0, 0, 1, 0]
    marital = [0, 1, 0, 1, 2]
    texture = [1, 0, 0, 1, 0]
    radio = [0, 1, 0, 1, 2]
    diag = [1, 0, 1, 0, 1]

    df = pd.DataFrame({'refund': refund,
                       'marital': marital,
                       'texture': texture,
                       'radio': radio,
                       'diagnosis': diag})

    respuesta1 = ['refund', 'marital', 'texture']
    respuesta2 = ['diagnosis']
    respuesta3 = ['texture', 'radio']

    assert(arbol.get_nombre_columnas(df, [0, 1, 2]) == respuesta1)
    assert(arbol.get_nombre_columnas(df, [4]) == respuesta2)
    assert(arbol.get_nombre_columnas(df, [2, 3]) == respuesta3)


def test_mejor_atributo():
    arbol = Arbol()
    lista_a = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    lista_b = [0, 1, 0, 1, 2, 1, 2, 0, 1, 0]
    lista_c = [0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
    diagnosis = [0, 0, 0, 0, 1, 0, 0, 1, 0, 1]

    df1 = pd.DataFrame({'refund': lista_a,
                        'marital': lista_b,
                        'texture': lista_c,
                        'diagnosis': diagnosis})

    df2 = pd.DataFrame({'refund': lista_b,
                        'marital': lista_a,
                        'texture': lista_c,
                        'diagnosis': diagnosis})

    df3 = pd.DataFrame({'refund': lista_c,
                        'marital': lista_a,
                        'texture': lista_b,
                        'diagnosis': diagnosis})

    r1 = arbol.mejor_atributo(df1, 0.88129, ['refund', 'marital', 'texture'])
    r2 = arbol.mejor_atributo(df2, 0.88129, ['refund', 'marital', 'texture'])
    r3 = arbol.mejor_atributo(df3, 0.88129, ['refund', 'marital', 'texture'])

    assert(r1 == 'marital')
    assert(r2 == 'refund')
    assert(r3 == 'texture')


def test_get_entropia_raiz():
    arbol = Arbol()
    texture = [1, 0, 0, 1]
    radio = [0, 1, 0, 1]

    diag1 = [1, 0, 1, 0]
    diag2 = [1, 0, 1, 1]
    diag3 = [0, 0, 0, 0]

    df1 = pd.DataFrame({'texture': texture,
                        'radio': radio,
                        'diagnosis': diag1})

    df2 = pd.DataFrame({'texture': texture,
                        'radio': radio,
                        'diagnosis': diag2})

    df3 = pd.DataFrame({'texture': texture,
                        'radio': radio,
                        'diagnosis': diag3})

    entropia1 = arbol.get_entropia_raiz(df1)
    entropia2 = arbol.get_entropia_raiz(df2)
    entropia3 = arbol.get_entropia_raiz(df3)

    assert(entropia1 == 1)
    assert(entropia2 == 0.8112781244591328)
    assert(entropia3 == 0)


def test_entropia():
    arbol = Arbol()

    p1 = 1
    n1 = 3
    e1 = 0.8112781244591328

    p2 = 5
    n2 = 2
    e2 = 0.863120568566631

    p3 = 3
    n3 = 4
    e3 = 0.9852281360342516

    assert(arbol.entropia(p1, n1) == e1)
    assert(arbol.entropia(p2, n2) == e2)
    assert(arbol.entropia(p3, n3) == e3)


def test_ganancia_informacion():
    arbol = Arbol()
    texture = [1, 0, 0, 1, 2]
    radio = [0, 1, 0, 1, 1]
    marital = [0, 1, 0, 1, 2]
    diag = [1, 0, 1, 0, 1]

    df = pd.DataFrame({'texture': texture,
                       'radio': radio,
                       'marital': marital,
                       'diagnosis': diag})

    r1 = arbol.ganancia_informacion([0, 1, 2], df, 'texture', 0.88129)
    r2 = arbol.ganancia_informacion([0, 1], df, 'radio', 0.88129)
    r3 = arbol.ganancia_informacion([0, 1, 2], df, 'marital', 0.88129)

    assert(r1 == 0.08128999999999997)
    assert(r2 == 0.33031249956730635)
    assert(r3 == 0.88129)


def test_contar_positivos():
    arbol = Arbol()
    texture = [1, 0, 0, 1]
    radio = [0, 1, 0, 1]

    diag1 = [1, 0, 1, 0]
    diag2 = [1, 0, 1, 1]
    diag3 = [0, 0, 0, 0]

    df1 = pd.DataFrame({'texture': texture,
                        'radio': radio,
                        'diagnosis': diag1})

    df2 = pd.DataFrame({'texture': texture,
                        'radio': radio,
                        'diagnosis': diag2})

    df3 = pd.DataFrame({'texture': texture,
                        'radio': radio,
                        'diagnosis': diag3})

    contar_positivos1 = arbol.contar_positivos(df1)
    contar_positivos2 = arbol.contar_positivos(df2)
    contar_positivos3 = arbol.contar_positivos(df3)

    assert(contar_positivos1 == 2)
    assert(contar_positivos2 == 3)
    assert(contar_positivos3 == 0)


def test_residuo():
    arbol = Arbol()
    texture = [1, 0, 0, 1, 2]
    radio = [0, 1, 0, 1, 1]
    marital = [0, 1, 0, 1, 2]
    diag = [1, 0, 1, 0, 1]

    df1 = pd.DataFrame({'texture': texture,
                        'radio': radio,
                        'marital': marital,
                        'diagnosis': diag})

    residuo1 = arbol.residuo([1, 0, 2], df1, 'texture')
    residuo2 = arbol.residuo([1, 0], df1, 'radio')
    residuo3 = arbol.residuo([0, 1, 2], df1, 'marital')

    assert(residuo1 == 0.8)
    assert(residuo2 == 0.5509775004326937)
    assert(residuo3 == 0)


def test_obtener_valor_fila():
    arbol = Arbol()
    df = pd.DataFrame({'texture': [1],
                       'radio': [2],
                       'marital': [0],
                       'diagnosis': [3]})

    assert(arbol.obtener_valor_fila(df, 'texture') == 1)
    assert(arbol.obtener_valor_fila(df, 'radio') == 2)
    assert(arbol.obtener_valor_fila(df, 'marital') == 0)
    assert(arbol.obtener_valor_fila(df, 'diagnosis') == 3)


def test_evaluar_fila():
    assert(1 == 1)

def test_evaluar_fila_aux():
    assert(1 == 1)
