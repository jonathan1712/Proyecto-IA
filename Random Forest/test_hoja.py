from hoja import *


def test_g_valor():
    hoja = Hoja(False, 1)
    assert(hoja.g_valor() is False)
    assert(hoja.g_valor() is not True)

    hoja = Hoja(True, 1)
    assert(hoja.g_valor() is True)
    assert(hoja.g_valor() is not False)


def test_g_enlace():
    hoja = Hoja(False, 1)
    assert(hoja.g_enlace() == 1)
    assert(hoja.g_enlace() != 0)

    hoja = Hoja(True, 2)
    assert(hoja.g_enlace() == 2)
    assert(hoja.g_enlace() != 1)
