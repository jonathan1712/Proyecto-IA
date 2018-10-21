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
###learner(self, filas)
*Se configura y se crea el modelo de random forest
###probar_modelo(self, filas)
*Dado un conjunto de filas se prueba el modelo  obteniendo como respuesta la tasa de error de dichas pruebas
###get_valor_real(self, filas)
*Obtiene el valor real de una fila, el "y" Retorna True si es 1 (Benigno), y sino False
###crear_bootstrapped(self)
*Crea el bootstrapped del random forest, seleccionando filas al azar del conjunto de entrada
###crear_forest(self)
*Se crea el bootstrapped del random forest y se crean todos los árboles solicitados
###evaluar_fila_forest(self, fila)
*Toma una fila en particular y la evalua en el random forest. Devuelve True si es Benigno y False si es maligno
###predecir(self, fila)
*Toma un conjunto de filas y se las aplica al random forest, devolviendo la predicciones generadas y la tasa de error de las mismas
###crear_fila(self, filas, indice)
*Toma un grupo de datos y los transforma en una fila parapoderlos evaluar posteriormente
###print_forest(self)
*Muestra todos los árboles del random forest

##Arbol
###crear_arbol(self, filas)
*Inicia el proceso recursivo de creación con la raiz
###crear_sub_arbol(self, nodo, filas, entropia, enlace)
*Construye el árbol con base en n filas seleccionadas al azar, sigue el algoritmo describo en el libro, buscando siempre el atributo con mejor ganancia
###generar_columnas(self, cantidad, atributos)
*Genera una lista de tamano n, con números random entre 0 y atributos, esta lista representa las  columnas a evaluar
###columna_unica(self, nodo, dist, nombre)
*En caso de que solo quede una columna, se calcula el resultado  del grupo de datos pertinente
###definir_eleccion(self, positivos, negativos, valor, nodo)
*En caso de que solo quede una columna se extraer las posibles elecciones de la misma
###get_prediccion(self, filas)
*Retorna True si la predicción de un grupo de filas es 1 sino False
###get_nombre_columnas(self, filas, columnas)
*Obtiene el nombre de un conjunto de columnas
###mejor_atributo(self, filas, entropia, columnas)
*Obtiene cuál es el mejor atributo de un lista de posibles mejores atributos
###get_entropia_raiz(self, filas)
*Obtiene la entropía de un conjunto de filas
###entropia(self, p, n)
*Cálculo de la entropia según la fórmula del libro
###ganancia_informacion(self, v_unicos, datos_columnas, col, entropia)
*Retorna la diferencia entre la entropía del nodo padre y el residuo del atributo
###contar_positivos(self, distribucion)
*Cuenta cuantas filas (con un mismo valor de un atributo) tienen como resultado positivo
###residuoself, v_unicos, datos, n_columna)
*Para cada atributo obtiene su residuo, que está dado por  la suma de la entropia * (p/total + n/total) de cada valor diferente.
###ver_arbol(self)
*Imprime el arbol en formato que sea entendible al usuario
###ver_arbol_aux(self, nivel, nodo_raiz
*Función auxiliar de ver árbol
###obtener_valor_fila(self, fila, atributo)
*obtener_valor_fila Dada una fila, obtiene el valor de un atributo
###evaluar_fila(self, fila)
*Inicia el proceso recursivo de evaluación de una función
###evaluar_fila_aux(self, nodo, fila)
*Función donde se evalua a profundidad una fila en el árbol. Retorna True o False

##Hoja
###g_valor(self)
*Retorna el valor de hoja
###g_enlace(self)
*Retorna el valor de enlace de la hoja

##Nodo
###hojas(self)
*Retorna las hojas asociadas al nodo actual
###nodos(self)
*Retorna los nodos asociadas al nodo actual
###g_etiqueta(self)
*Retorna la etiqueta del nodo actual
###g_enlace(self)
*Retorna el enlace del nodo actual
###g_nombre(self)
*Retorna el nombre del atributo propietario del nodo
###agregar_nodo(self, nodo)
*Agrega un nodo a la lista de nodos hijos del actual nodo
###agregar_hoja(self, datos)
*Agregar una hoja a la lista de hojas del nodo actual
###obtener_valor_hoja(self, valor)
*Obtener el valor de una hoja en particular, dado el enlace de la misma
###contiene_hoja(self, valor)
*Verifica si un nodo posee una hoja, dado un enlace particular
###contiene_nodo(self, valor)
*Verifica si un nodo contiene un nodo, dado el nombre de un atributo
###obtener_nodo_siguiente(self, valor)
*Obtener un nodo de la lista de nodos del objeto actual, dado el nombre del atributo

##Inicializador
###obtener_parametros()
*Se encarga de la lectura de parámetros que se le ingresen de la consola y dependiendo de la elección del usuario llama la función para ejecutar el Random Forest o la Red neuronal con sus respectivos parámetros
###random_forest(arboles, umbral_poda, porcentaje_pruebas, prefijo)
*Llama la función random forest con los parámetros ingresados.
###red_neuronal(capas, unidades, funcion, porcentaje_pruebas, prefijo)
*Llama la función red neuronal con los parámetros respectivos

##main
###main()
*Llama a la función cross validation con los parámetros ingresados al inicializador.


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

