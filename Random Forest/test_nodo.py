from nodo import *


def test_etiqueta():
    nodo = Nodo()
    nodo.etiqueta = "1 -> Radio"

    assert(nodo.g_etiqueta() == "1 -> Radio")
    assert(nodo.g_etiqueta() != "1 -> Texture")


def test_enlace():
    nodo = Nodo()
    nodo.enlace = 1

    assert(nodo.g_enlace() == 1)
    assert(nodo.g_enlace() != 0)


def test_nombre():
    nodo = Nodo()
    nodo.nombre = "Radio"

    assert(nodo.g_nombre() == "Radio")
    assert(nodo.g_nombre() != "Texture")


def test_agregar_nodo():
    nodo_padre = Nodo()
    nodo_padre.nombre = "Padre"

    assert(len(nodo_padre.nodos()) == 0)
    assert(len(nodo_padre.nodos()) != 1)

    nodo_hijo = Nodo()
    nodo_hijo.nombre = "Hijo"
    nodo_padre.agregar_nodo(nodo_hijo)

    assert(len(nodo_padre.nodos()) == 1)
    assert(len(nodo_padre.nodos()) != 0)


def test_agregar_hoja():
    nodo_padre = Nodo()
    nodo_padre.nombre = "Padre"

    assert(len(nodo_padre.hojas()) == 0)
    assert(len(nodo_padre.hojas()) != 1)

    nodo_padre.agregar_hoja([True, 1])

    assert(len(nodo_padre.hojas()) == 1)
    assert(len(nodo_padre.hojas()) != 0)


def test_obtener_valor_hoja():
    nodo = Nodo()
    nodo.nombre = "Padre"

    nodo.agregar_hoja([False, 1])

    assert(nodo.obtener_valor_hoja(1) is False)
    assert(nodo.obtener_valor_hoja(0) is not False)


def test_contiene_hoja():
    nodo = Nodo()
    nodo.nombre = "Padre"

    nodo.agregar_hoja([False, 1])

    assert(nodo.obtener_valor_hoja(1) is False)


def test_contiene_nodo():
    nodo_padre = Nodo()
    nodo_padre.nombre = "Padre"

    assert(nodo_padre.contiene_nodo(1) is False)

    nodo_hijo = Nodo()
    nodo_hijo.nombre = "Hijo1"
    nodo_hijo.enlace = 0
    nodo_padre.agregar_nodo(nodo_hijo)

    assert(nodo_padre.contiene_nodo(0) is True)


def test_obtener_nodo_siguiente():
    nodo_padre = Nodo()
    nodo_padre.nombre = "Padre"

    assert(len(nodo_padre.nodos()) == 0)

    nodo_hijo = Nodo()
    nodo_hijo.nombre = "Hijo"
    nodo_hijo.enlace = 1
    nodo_hijo.etiqueta = "1 -> Radio"
    nodo_padre.agregar_nodo(nodo_hijo)

    assert(nodo_padre.obtener_nodo_siguiente(1).g_enlace() == 1)
