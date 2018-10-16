from random_forest import *
from Arbol import *
import pandas as pd

def main():
    print("fgdf")

def prueba():
    outlook =   [0,0,1,2,2,2,1,0,0,2,0,1,1,2]
    temp =      [0,0,0,1,2,2,2,1,2,1,1,1,0,1]
    hum =       [0,0,0,0,1,1,1,0,1,1,1,0,1,0]
    windy =     [0,1,0,0,0,1,1,0,0,0,1,1,0,1]
    r =         [0,0,1,1,1,0,1,0,1,1,1,1,1,0] 
    df = pd.DataFrame({'Outlook':outlook,
                       'Temp':temp,
                       'Hum':hum,
                       'Windy':windy,
                       'diagnosis':r})

    random_forest = Random_Forest(10,df)
    random_forest.crear_forest()
    random_forest.print_forest()

    de = pd.DataFrame({'Outlook':[0],
                       'Temp':[2],
                       'Hum':[1],
                       'Windy':[0],
                       'diagnosis':[0]})
    resultado = random_forest.evaluar_fila_forest(de)
    print(resultado)
    


if __name__ == "__main__":
    main()
