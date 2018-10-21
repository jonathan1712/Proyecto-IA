from normalizador import *


def test_zscore():
    normalizador = Normalizador()
    zscore_a = np.array([-1.41421356, -0.70710678, 0, 0.70710678, 1.41421356])

    # media = 2.5, desviación = 0.5
    assert all(normalizador.zcore([2, 3]) == np.array([-1, 1]))

    # media = 3, desviación = 1,41421356
    assert(str(normalizador.zcore([1, 2, 3, 4, 5])) == str(zscore_a))


def test_generar_rangos():
    normalizador = Normalizador()
    rango_a = ['< 2.33', '2.33 - 3.66', '3.66 <']
    rango_b = ['< 7.0', '7.0 <']
    rango_c = ['< 9.33', '9.33 - 14.66', '14.66 <']

    # casos individuales, donde se muestra que efectivamente genera los rangos
    assert(normalizador.generar_rangos(3, 1, 5, 3) == rango_a)
    assert(normalizador.generar_rangos(7, 2, 15, 2) == rango_b)

    # caso con valores erroneos que no producen la salida esperada
    assert(normalizador.generar_rangos(5, 4, 10, 3) != rango_c)
    assert(normalizador.generar_rangos(5, 4, 20, 3) == rango_c)


def test_evaluar_acote():
    normalizador = Normalizador()

    # casos donde un valor si se encuentra entre un rango lim_a <= x < lim_b
    assert(normalizador.evaluar_acote("10.5 - 11", 10.6) is True)
    assert(normalizador.evaluar_acote("0 - 5", 4) is True)

    # casos donde no se encuentra un valor entre un rango lim_a <= x < lim_b
    assert(normalizador.evaluar_acote("1 - 8", 9) is False)
    assert(normalizador.evaluar_acote("4.6 - 20.9", 30) is False)


def test_evaluar_limite():
    normalizador = Normalizador()

    # casos donde un valor si está fuera del límite
    assert(normalizador.evaluar_limite(0, "< 4", 3) is True)
    assert(normalizador.evaluar_limite(0, "< 100", 25.8) is True)

    # casos donde un valor está dentro del límite
    assert(normalizador.evaluar_limite(1, "4 <", 3) is False)
    assert(normalizador.evaluar_limite(1, "100 <", 25.8) is False)


def test_clasificar_columna():
    normalizador = Normalizador()
    pred_a = ['1 - 10', '10 - 12', '12 <', '< 1', '1 - 10', '10 - 12']
    pred_b = ['< 0', '< 0', '0 <', '< 0', '0 <']
    error_p_a = ['12 <', '10 - 12', '12 <', '< 1', '1 - 10', '10 - 12']
    error_p_b = ["< 0", "< 0", "< 0", "< 0", "< 0"]
    etiq_a = ["10 - 12", "< 1", "1 - 10", "12 <"]
    etiq_b = ["< 0", "0 <"]
    col_a = [1, 10.5, 16, 0, 5, 11]
    col_b = [-1, -5, 2, -3, 6]

    # casos donde se clasifican de manera correcta los datos
    assert(normalizador.clasificar_columna(col_a, etiq_a) == pred_a)
    assert(normalizador.clasificar_columna(col_b, etiq_b) == pred_b)

    # caso donde se el valor esperado es incorrecto
    assert(normalizador.clasificar_columna(col_a, etiq_a) != error_p_a)
    assert(normalizador.clasificar_columna(col_b, etiq_b) != error_p_b)
