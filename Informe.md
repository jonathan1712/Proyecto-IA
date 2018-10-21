# I PROYECTO PROGRAMADO IA

------------------------------------------------ 
Instituto Tecnológico de Costa Rica 	      
Escuela de Ingeniería en Computación       
Curso: Inteligencia Artificial	      
Semestre 2 - 2018		 	      
Proyecto I 			      
Estudiantes: 			      
* Jonathan Martínez Camacho 	      
* Mariana Rojas Semeraro 		      
* Diego Tenorio Solís
Repositorio: https://github.com/jonathan1712/Proyecto-IA.git 		      
------------------------------------------------

------------------------------------------------
# Estrategia de Solución
------------------------------------------------
Para la realización de este proyecto decidimos manejar n clases distintas para así resolver el problema.

## Archivo
Esta clase se encarga principalmente de manejar el set de datos, los diferentes métodos se encargan de obtenerlo del archivo descargado desde el repositorio disponible en kaggle.
### get_data_set(self)
Retorna el atributo que corresponde al set de datos.
### escribir_archivo_csv(self, datos, nombre_archivo)
Esta función se encarga de escribir el archivo con el nombre que indica el parámetro nombre_archivo de extensión .csv los datos también dados como parámetro.
### leer_data_set(self)
Con ayuda de la librería pandas se encarga de leer el archivo de extensión .csv, así como de prepararlo para la ejecución del modelo, esto eliminando la columna id, además de mover la columna diagnóstico al final.
### abrir_archivo(self)
Se le asigna a la variable puntero un archivo de extensión .csv para escribir sobre él algunas estadísticas resultantes al ejecutar algún modelo.
### escribir_linea(self, contenido)
Se escribe sobre la variable puntero perteneciente a la clase, el contenido dado como parámetro.
### cerrar_archivo(self)
Se cierra la variable puntero, que correspondía a un archivo de extensión .csv.

## Normalización
Esta clase es la encargada de la normalización de los datos, por lo cual, es indispensable, tanto para el modelo de redes neuronales como para el modelo de random forest. También se encarga de realizar la clasificación de las columnas, esto en el caso del random forest.
### normalizar(self)
Para cada fila del data_set se aplica la función zscore. Cada valor de cada fila es redondeado a dos decimales antes de ser normalizado.
### zcore(self, columna)
Aplica la función zscore de stats a una columna (lista) recibida como parámetro.
### clasificar_columnas(self)
Toma las columnas ya normalizadas y las clasifica según la cantidad de rangos solicitados. Es importante saber que no clasifica la columna de diagnosis.
### generar_rangos(self, media, minimo, maximo, rangos)
Dado los valores flotantes de media, mínimo, máximo de una columna, genera un cantidad n de rangos, para ello se calcula la distancia del mínimo al máximo y ese es el intervalo de cada rango. Hace distinción entre límite del tipo "<x, >x" y a <= x < b
### clasificar_columna(self, columna, etiquetas)
Clasifica todos los elementos de una columna con base en las etiquetas que se generaron para la misma según el número de rangos solicitados.
### evaluar_acote(self, expresion, num)
Evalúa expresiones en string del tipo 10 - 11, donde implica que 10 <= x < 11, y en caso de ser correcto retorna True o False.
### evaluar_limite(self, tipo, expresion, numero)
Evalúa expresiones en string del tipo numero < x, x < numero, y retorna True o False dependiendo del resultado la evaluación.

## Cross Validation
### definir_modelo(self, argumentos)
Dado el tipo de modelo ingresado como parámetro se crea ya sea un modelo tipo Red Neuronal o Random Forest, con sus respectivos parámetros. Ya definido el modelo, se lee el data set desde el achivo .csv y se normalizan los datos.
### cross_validation(self)
Es la función principal, en primer lugar se encarga de resguardar los datos de las predicciones, y posteriormente con los datos restantes aplica el proceso conocido como K-Fold cross validation. El objetivo de la función es determinar los porcentajes de error de las pruebas, de evaluación y primordialmente de las predicciones
### escribir_archivo_prediccion(self, predicciones)
Agrega una columna extra al dataframe de pandas donde se maneja el resultado de las predicciones, de forma que se puede comparar el valor real con el predicho
### particionar(self, fold, k, n)
Crea un dataframe para datos de entrenamiento y datos de pruebas, de manera que su manejo pueda ser llevado a cabo por el modelo.
### sacar_prediccion(self):
Dado un set de datos se obtiene una parte de este set que corresponde a un set de datos usado para predicciones en el modelo definido en la clase.

## Modelo
### leer_archivo(self, nombre_archivo)
Crea una instancia de un archivo con el nombre que recibe como parámetro, para posteriormente obtener los datos del archivo .csv.
### normalizar(self, tipo_modelo)
Una vez obtenido el valor de un archivo, se normalizan los datos, y si el tipo es random forest, también se aplica la clasificación.

## Red Neuronal
### learner(self, datos_entrenamiento)
Función de aprendizaje, dado un conjunto de datos de entrenamiento la red neuronal se llama a una función encargada de entrenar a la red neuronal con dicho conjunto.
 ### crear_modelo(self)
 Se configuran las características de la red, esto implica asignar la cantidad de capas y unidades por capa. Se hace un ciclo, donde cada iteración se crea una nueva capa.
### entrenar_modelo(self, datos_entrenamiento)
Una vez creado el modelo, se seleccionan los datos de entrenamiento y son ingresados en la red, de manera que, esta sea capaz, posteriormente de dar resultados óptimos. El primer paso antes de entrenar es compilar el modelo.
### probar_modelo(self, datos_prueba)
Se brindan los datos de prueba y se evalúan sobre el modelo (red neuronal) creado previamente. El retorno de la función es un porcentaje de error de la prueba.
### predecir(self, datos_prediccion)
Dado un conjunto de datos de predicción, estos se aplican al modelo (red neuronal)  y se obtiene su respuesta y la tasa de error de dicha predicción.
### normalizar_datos_prediccion(self, prediccion)
Recibe el arreglo de predicción y lo normaliza a binario.
### crear_set_datos_entrenamiento(self)
Se toma los datos de entrenamiento del modelo para generar un dataframe de pandas, el cual permite manipular los datos con mayor facilidad. Además de separarlos en dos sets de datos; lo que sería equivalente a las entradas y salidas.
### crear_set_datos_prueba(self)
Se toman los datos de prueba del modelo para generar un dataframe de pandas, el cual permite manipular los datos con mayor facilidad. Además de separarlos en dos sets de datos; lo que sería equivalente a las entradas y salidas.


## Random Forest

------------------------------------------------
# Análisis de resultados
En cuanto al análisis de resultados en primer lugar, mostramos el comportamiento de las pruebas unitarias, y las pruebas de cobertura de código:

Pruebas de Pytest

============================= test session starts =============================
platform win32 -- Python 3.6.4, pytest-3.8.2, py-1.7.0, pluggy-0.7.1
rootdir: E:\TEC\2018\II SEMESTRE\Inteligencia Artifical\Proyecto-IAMMM, inifile:
plugins: expect-1.1.0, cov-2.6.0
collected 36 items

test_arbol.py ............                                               [ 33%]
test_archivo.py ...                                                      [ 41%]
test_hoja.py ..                                                          [ 47%]
test_modelo.py ..                                                        [ 52%]
test_nodo.py .........                                                   [ 77%]
test_normalizador.py .....                                               [ 91%]
test_random_forest.py ...                                                [100%]

Pruebas de Coverage

----------- coverage: platform win32, python 3.6.4-final-0 -----------
Name                    Stmts   Miss  Cover
___________________________________________
arbol.py                  131     16    88%
archivo.py                 30      3    90%
hoja.py                     8      0   100%
modelo.py                  17      2    88%
nodo.py                    51      6    88%
normalizador.py            79     13    84%
random_forest.py           86     56    35%
red_neuronal.py            66     50    24%
test_arbol.py             166      0   100%
test_archivo.py            22      0   100%
test_hoja.py               15      0   100%
test_inicializador.py       0      0   100%
test_modelo.py             22      0   100%
test_nodo.py               64      0   100%
test_normalizador.py       41      0   100%
test_random_forest.py      50      0   100%
test_red_neuronal.py        8      5    38%
___________________________________________
TOTAL                     856    151    82%


En segundo lugar, enfocado especificamente en los modelos, respecto al modelo de Random Forest se encuentra que:

	Realizando varias pruebas con un k = 3, y con 5 árboles, el valor de error en la parte de Test es cercano al 0.05%, el valor de error de Validación ronda el 0.02%, y el tercero pero no menos importante el error de predicción es de 0.4%, todo lo anterior implica que el modelo se comporta de manera estable sin cambios abruptos. En números más claros, de cada 171 filas, como máximo solo ocurrían 7 errores.	
	El comportamiento anterior es similiar para cantidades de árboles entre 10 y 15, sin embargo con valores un poco más altos, como 21, la precisión del modelo aumenta y su error disminuye a cerca de 0.03, pero no solo eso, sino que al modificar el valor de k a 10, el error disminuye abismalmente a cerca de 0.2 - 0.18, mostrando que el valor del K-fold es determinante en la precisión del modelo, y esto se debe a que entre mayor número de particiones (k), los errores se redistribuyen de mejor manera.

	En cuanto a Redes Neuronales, es justo hacer el análisis desde las dos funciones de activación, en primer lugar:

	Softmax: esta función ofrece según las corridas realizadas una mejor precisión, posee un comportamiento similar al nivel de precisión de Random Forest, con número de capas = 3, y 5 unidades por cada capa ronda los 0.05% en cuanto al error de predicción, mientras que con 10 capas y 5 unidades este porcentaje ronda los 0.04%, de igual forma, el porcentaje de error en Test y Validación es cercano al  0.02.

	Relu: está función ofrece predicciones menos certeras en comparación a Softmax, sus % suelen ser significativamente diferentes con valores similares, sin embargo, es importante mencionar que esa diferencia significativa se ve opacada con valores de capas más grandes y con mayor número de unidades, pues en estos casos su poder de predicción es bastante similar a Softmax.

------------------------------------------------

------------------------------------------------
# Manual de Instalación

### Requisitos básicos:
- Python 3.6.4 (Windows), se recomienda este enlace de descarga: https://www.python.org/ftp/python/3.6.4/python-3.6.4-amd64.exe
- Adicionalmente, ya que al equipo de trabajo se le presentaron problemas con tensorflow y Windows, se recomienda instalar también: https://www.microsoft.com/es-es/download/confirmation.aspx?id=53587&6B49FDFB-8E5B-4B07-BC31-15695C5A2143=1 y, en caso de que ya se encuentre instalado, no hay problema. 
### Instalación de paquetes
- Tensorflow:
	* pip install --upgrade pip
	* pip install --upgrade tensorflow
- Numpy:
	* pip install numpy
- Pandas:
	* pip install pandas
- Scipy:
	* pip install scipy
- Keras: 
	* pip install keras
------------------------------------------------

------------------------------------------------
# Manual de Ejecución
### Requisitos básicos:
- Set de datos para la correcta predicción de los modelos, el mismo se puede obtener de forma gratuita de la siguiente dirección: https://www.kaggle.com/uciml/breast-cancer-wisconsin-data

### Ejecución:
- Red neuronal: lo primero es definir las opciones de configuración para este modelo, las cuales son:
	* -rn o --red-neuronal: identifica el tipo de modelo que se va a crear.
	* -nc o --numero-capas: identifica el número de capas de la red neuronal.
	* -upc o --unidades-por-capa: identifica el número de unidades por capa. Es este caso todas las capas poseen la misma cantidad de unidades.
	* -pp o --porcentaje-pruebas: identifica el porcentaje de filas del conjunto de datos original que deben ser destinado a la predicción.
	* -fa o --funcion-activacion: identifica el tipo de función de activación que se desea utilizar en el modelo. Son válidas las siguientes: "softmax" y "relu".
	* -prer --prefijo-r: identifica el prefijo con el cual se crearan los archivos intermedios (de estadísticas de cross validation).
	Un ejemplo de una llamada válida sería:
	python main.py -rn -nc 3 -upc 2 -pp 0.3 -fa "softmax" -prer "corrida1"

- Random Forest: lo primero es definir las opciones de configuración para este modelo, las cuales son:
	* -rf o --random-forest: identifica el tipo de modelo que se va a crear.
	* -na o --numero-arboles: identifica el número de árboles que se crearán para el Random Forest.
	* -pop o --porcentaje-prueba: identifica el porcentaje de filas del conjunto de datos original que deben ser destinado a la predicción.
	* -up o --umbral-poda: identifica el valor mínimo de un atributo para que no exista poda.
	* -prea --prefijo-a: identifica el prefijo con el cual se crearan los archivos intermedios (de estadísticas de cross validation).
	Un ejemplo de una llamada válida sería:
	python main.py -rf -na 11 -pop 0.3 -up 0.15 -prea "corrida1"

Al final de la ejecución de cada modelo se creará un archivo con el nombre ".csv" que contiene las filas de predicción, con el valor real y el predicho.
------------------------------------------------

------------------------------------------------
# Distribución de notas y trabajo realizado
------------------------------------------------
En cuanto a la distribución del trabajo se divide de la siguiente manera:

- Jonathan Martínez:
	* Encargado de la normalización de los datos.
	* Manejo de los archivos. 
	* Diseño y elaboración del modelo de Random Forest y todas las clases asociadas (Arbol, Hoja, Nodo).
	* Colaboración en la documentación.
	* Desarrollo de pruebas unitarias en lo relacionado con el módulo de Normalización, y Random Forest (Arbol, Hoja, Nodo)

- Mariana Rojas:
	* Investigación e implementación del modelo de Redes Neuronales.
	* Diseño e implementación del módulo de Cross Validation.
	* Diseño e implementación del módulo Modelo, que es el encargado de permitir la herencia.
	* Colaboración en la documentación. 
	* Desarrollo de las pruebas unitarias en lo relacionado con el módulo de Modelo.

- Diego Tenorio:
	* Investigación y colaboración en el módulo de Random Forest.
	* Investigación y colaboración en el módulo de Redes Neuronales.
	* Diseño e implementación del módulo del paso de parámetros al programa.
	* Colaboración en la documentación.

Distribución de la nota:

- Jonathan Martínez 100
- Mariana Roja 95
- Diego Tenorio 80

