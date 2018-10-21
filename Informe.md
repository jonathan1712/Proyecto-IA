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
- Red neuronal:
- Random Forest:
------------------------------------------------

------------------------------------------------
# Distribución de notas y trabajo realizado
------------------------------------------------
