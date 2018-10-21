from archivo import *


def test_get_data_set():
    archivo = Archivo("prueba.csv")
    archivo.leer_data_set()

    radius = [17, 20, 19, 11, 20, 12, 18, 13, 13]
    textur = [10, 17, 21, 20, 14, 15, 19, 20, 21]
    diagno = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    df = pd.DataFrame({'radius_mean': radius,
                       'texture_mean': textur,
                       'diagnosis': diagno})

    assert all(archivo.get_data_set() == df)

def test_escribir_archivo_csv():
    arch1 = Archivo("prueba.csv")
    arch1.leer_data_set()

    arch2 = Archivo("prueba_escritura.csv")
    res = arch2.escribir_archivo_csv(arch1.get_data_set(),arch2.nombre_archivo)
    res1 = arch2.escribir_archivo_csv([], "")
    assert(res is True)
    assert(res1 is False)


def test_leer_data_set():
    archivo1 = Archivo("prueba.csv")
    assert(archivo1.leer_data_set() is True)
    archivo2 = Archivo("nprueba.csv")
    assert(archivo2.leer_data_set() is False)
