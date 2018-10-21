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
Esta clase se encarga principalmente de manejar el set de datos, los diferentes métodos se encargan de obtenerlo del archivo descargado desde el repositorio.
### get_data_set
Retorna el atributo que corresponde al set de datos.
### escribir_archivo_csv
??
### leer_data_set
Con ayuda de la librería pandas se encarga de leer el archivo de extensión csv, así como de prepararlo para la ejecucución del modelo, esto eliminando la columna id, además de mover la columna diagnóstico al final.
### abrir_archivo
### escribir_linea
### cerrar_archivo

## Normalización
Esta clase es la encargada de la normalización de los datos, por lo cual, es indispensable, tanto para el modelo de redes neuronales como para el modelo de random forest. También se encarga de realizar la clasificación de las columnas, esto en el caso del random forest.
### normalizar
### zscore
### clasificar_columna
### clasificar_columnas
### generar_rangos
### evaluar_acote
### evaluar_limite


## Cross Validation
### definir_modelo
Dado el tipo de modelo ingresado como parámetro se crea ya sea un modelo tipo Red Neuronal o Random Forest, con sus respectivos parámetros. Ya definido el modelo, se lee el data set desde el achivo .csv y se normalizan los datos.
### cross_validation
Este algoritmo se encarga de particionar el set de datos en dos conjuntos en cada iteración de un ciclo, primero entrena el modelo con el primer conjunto que serían los datos de entrenamiento, y luego, probar el modelo con el segundo conjunto que son los datos de prueba.
### escribir_archivo_prediccion
### particionar
### particionar_forest
### particionar_red
### sacar_prediccion_red
### sacar_prediccion_forest

## Modelo

## Red Neuronal

## Random Forest

------------------------------------------------
# Análisis de resultados
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

