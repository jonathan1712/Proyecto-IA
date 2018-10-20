from modelo import *


def test_leer_archivo():
    modelo = Modelo()
    nombre_archivo = "prueba.csv"

    radius = [17, 20, 19, 11, 20, 12, 18, 13, 13]
    textur = [10, 17, 21, 20, 14, 15, 19, 20, 21]
    diagno = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    df = pd.DataFrame({'radius_mean': radius,
                       'texture_mean': textur,
                       'diagnosis': diagno})

    assert all(modelo.leer_archivo(nombre_archivo) == df)

def test_normalizar():
    modelo = Modelo()
  
    radius = [0.1189,0.08902,0.08758]
    textur = [0.3613,0.4601,0.3613]
    diagno = [1,0,1]
    df_entrada = pd.DataFrame({'radius_mean': radius,
                       'texture_mean': textur,
                       'diagnosis': diagno})

    modelo.archivo = df_entrada

    radius = [1.414214,-0.707107,-0.707107]
    textur = [-0.707107,1.414214,-0.707107]
    diagno = [1,0,1]
    df_salida = pd.DataFrame({'radius_mean': radius,
                       'texture_mean': textur,
                       'diagnosis': diagno})

    df_salida = df_salida.round(5)
    assert(df_salida.equals(modelo.normalizar(1).round(5)))
