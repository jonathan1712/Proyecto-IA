from modelo import *


# No sirve
def test_leer_archivo():
    modelo = Modelo()
    archivo = "test_modelo.csv"
    print(modelo.leer_archivo(archivo))

def test_normalizar():
    modelo = Modelo()
    entrada_dic = {'columna 1': [0.1189,0.08902,0.08758], 'columna 2': [0.3613,0.4601,0.3613], 'resultado': ["a","b","a"]}
    entrada = pd.DataFrame(data=entrada_dic)

    salida_dic = {'columna 1': [1.414214,-0.707107,-0.707107], 'columna 2': [-0.707107,1.414214,-0.707107], 'resultado': ["a","b","a"]}
    salida = pd.DataFrame(data=salida_dic)

    modelo.archivo = entrada
    
    print(salida)
    print(modelo.normalizar())
    print(salida.equals(modelo.normalizar()))
    print(salida==modelo.normalizar())
    #assert(salida.equals(modelo.normalizar()))

def main():
    test_normalizar()

if __name__ == "__main__":
    main()




