# ProSafe_Auto_Insure
Análisis Avanzado de Datos para la Optimización del Seguro de Automóviles: Un Caso de Estudio con ProSafe Auto Insure

## Descripción del proyecto

# Descripción del Proyecto

Este proyecto presenta un análisis avanzado y una segmentación de clientes basado en el conjunto de datos de **ProSafe Auto Insure**, una compañía líder en el sector de seguros de automóviles comprometida con la seguridad, la transparencia y la atención centrada en el cliente.

El objetivo principal es extraer valor del histórico de pólizas y reclamaciones para optimizar la gestión del riesgo, mejorar la tarificación de primas y personalizar la experiencia de los asegurados. El análisis se enfoca especialmente en la **segmentación de clientes según su nivel de siniestralidad**, utilizando técnicas de análisis de datos y aprendizaje automático.

A través de una exploración exhaustiva del dataset —que incluye variables como género, tipo de cobertura, valor asegurado, uso del vehículo, historial de siniestros y otros datos clave— se desarrollan modelos analíticos y visualizaciones interactivas. Estas herramientas permiten identificar patrones de riesgo, caracterizar segmentos de clientes y diseñar estrategias de negocio fundamentadas en datos.

El proyecto incluye:

- **Análisis descriptivo** de los asegurados y los vehículos.
- **Estudio de la siniestralidad** y tipificación de reclamaciones.
- **Segmentación de clientes** en función de la frecuencia y monto de los siniestros.
- **Modelado predictivo** del riesgo de siniestralidad y recomendaciones para la optimización de primas.
- **Visualización de resultados** a través de dashboards en Power BI, facilitando la toma de decisiones basada en datos.

En última instancia, este trabajo busca aportar una visión integral y accionable para que ProSafe Auto Insure fortalezca su posicionamiento como socio confiable, mejore la gestión del riesgo y fomente la seguridad vial de sus asegurados.

## Tecnologías Utilizadas

- **Python**: Lenguaje principal para el procesamiento y análisis de datos.
- **Pandas**: Manipulación, limpieza y análisis de datos tabulares.
- **NumPy**: Operaciones numéricas y de arrays.
- **Scikit-learn**: Implementación de algoritmos de machine learning para segmentación y modelos predictivos.
- **Matplotlib** y **Seaborn**: Visualización de datos y gráficos exploratorios.
- **Power BI**: Creación de dashboards interactivos para la visualización y comunicación de resultados.
- **Jupyter Notebook**: Desarrollo, documentación y presentación de análisis de datos de forma interactiva.
- **Git/GitHub**: Control de versiones y colaboración en el desarrollo del proyecto.
- **data_utils**: Módulo propio del proyecto con funciones desarrolladas específicamente para la limpieza, transformación y análisis de los datos.

# Estructura de los datos del proyecto
Los datos se presentan en dos tablas: 

## Descripción de las Tablas

### `motor_data11-14lats.csv`

Contiene datos de pólizas de seguro para vehículos entre los años 2011 y 2014. Sus columnas principales son:

- **OBJECT_ID:** Identificador único del vehículo/póliza.
- **SEX:** Género del titular de la póliza (codificado).
- **INSR_BEGIN / INSR_END:** Fechas de inicio y fin de la póliza.
- **EFFECTIVE_YR:** Año de vigencia.
- **INSR_TYPE:** Tipo de seguro.
- **INSURED_VALUE:** Valor asegurado.
- **PREMIUM:** Prima pagada por la póliza.
- **PROD_YEAR:** Año de fabricación del vehículo.
- **SEATS_NUM:** Número de asientos.
- **CARRYING_CAPACITY:** Capacidad de carga.
- **TYPE_VEHICLE:** Tipo de vehículo (ejemplo: Pick-up).
- **CCM_TON:** Cilindrada o peso (según contexto).
- **MAKE:** Marca del vehículo.
- **USAGE:** Uso del vehículo (ejemplo: Own Goods).
- **CLAIM_PAID:** Importe pagado en caso de siniestro (puede haber valores nulos).

El número de filas que tiene la tabla es 293.537, y el número de columnas es 15


### `motor_data14-2018.csv`

Tiene la misma estructura que la tabla anterior, pero contiene datos de pólizas para el periodo de 2014 a 2018. Las columnas son idénticas.

El número de filas es de 508.499, y el número de columnas es 15


## Relación entre las Tablas

Ambas tablas presentan información histórica de pólizas de vehículos, con los mismos campos y estructura, pero para periodos de tiempo consecutivos/no superpuestos:

- **motor_data11-14lats.csv:** Cubre de 2011 a 2014.
- **motor_data14-2018.csv:** Cubre de 2014 a 2018.

La **relación** entre ambas es de **continuidad temporal**. Se unen ambas tablas para obtener el historial completo de pólizas y siniestros de los mismos vehículos (por su `OBJECT_ID`) entre 2011 y 2018.  En una tabla unificada se  analizará la evolución de ese vehículo/póliza a lo largo del tiempo.

La tabla final con la que se inicia el EDA tiene un número de filas de 802.036, y el número de columnas es 16. la información se almacena en la carpeta `Data` con el nombre `motor_data_2011_2018.csv`
## Estructura de archivos del proyecto
```.
├── Data
│   ├── motor_data_2011_2018_EDA.csv
│   ├── motor_data_2011_2018_pre.csv
│   ├── motor_data_2011_2018_RISK.csv
│   ├── motor_data_2011_2018.csv
│   ├── motor_data_final_para_powerbi.csv
│   ├── motor_data11-14lats.csv
│   ├── motor_data14-2018.csv
│   ├── nuevo_cliente.csv
│   └── resultado_nuevo_cliente.csv
├── Image
│   ├── boxplot1.png
│   ├── codo.png
│   ├── codo2.png
│   ├── correlacion.png
│   ├── distribuciones_var_cat.png
│   ├── distribuciones_var_date.png
│   ├── distribuciones_variables.png
│   ├── k-Means1.png
│   ├── k-Means2.png
│   ├── var_cruzadas_cat_box.png
│   ├── var_cruzadas_cat.png
│   └── var_cruzadas.png
├── Modelos
│   ├── kmeans_model.pkl
│   ├── pca_model.pkl
│   └── preprocessing_pipeline.pkl
├── Notebook
│   ├── __pycache__
│   │   ├── data_utils.cpython-310.pyc
│   │   └── data_utils.cpython-313.pyc
│   ├── 01-EDAMotor_data11-14lats.ipynb
│   ├── 02-Preproceso.ipynb
│   ├── 03-Clustering_K-Means.ipynb
│   ├── 04-Clustering_DBSCAN.ipynb
│   ├── 05-Evaluacion_Nuevo_Cliente_CORREGIDO.py
│   ├── 05-Evaluacion_Nuevo_Cliente.py
│   ├── 06-Generar_Nuevo_Cliente.ipynb
│   ├── data_utils.py
│   └── muestra.ipynb
├── README.md
├── Siniestralidad_Riesgo3.pbix
└── Siniestralidad_Riesgo3.pdf

6 directories, 38 files
```
# Adquisición y exploración inicial de datos
- Se realiza la carga de cada tabla y se realiza la unión utilizando `concat`, apilando los registros uno debajo del otro.
- Se validan los duplicados:  
  - `object_id` es el identificador único de un vehículo, pero un mismo vehículo puede contar con varias pólizas.  
  - **object_id únicos:** 288,763  
  - **Filas totales:** 802,036  
  - **Duplicados exactos:** 145,742  
  Se eliminan los registros duplicados exactos del conjunto de datos.
- Se validan y ajustan los tipos de datos de cada columna. Cambios realizados:  
  - `INSR_BEGIN`: de `object` a formato de fecha  
  - `INSR_END`: de `object` a formato de fecha  
  - `EFFECTIVE_YR`: de `object` a `int`, completando los años con “20” donde sea necesario  
  - `PROD_YEAR`: de `float64` a `int`, ya que los valores son enteros aunque tengan decimales “.0”  
  - `SEATS_NUM`: de `float64` a `int`  
- Se identifican columnas con valores nulos. Las columnas que presentan valores nulos son:  
  - `EFFECTIVE_YR`  
  - `PREMIUM`  
  - `PROD_YEAR`  
  - `SEATS_NUM`  
  - `CARRYING_CAPACITY`  
  - `CCM_TON`  
  - `MAKE`  
  - `CLAIM_PAID`


 ## Análisis estadístico básico de las variables numéricas
 
 las estadísticas básicas de las variables numéricas son: 
 | Campo              | count      | mean           | std             | min    | 25%        | 50% (mediana) | 75%        | max           | moda    |
|--------------------|------------|----------------|-----------------|--------|------------|---------------|------------|---------------|---------|
| SEX                | 656294.0   | 0.6620         | 0.6549          | 0.0    | 0.0        | 1.0           | 1.0        | 2.0           | 1.0     |
| EFFECTIVE_YR       | 655287.0   | 2019.43        | 20.20           | 2000.0 | 2011.0     | 2013.0        | 2016.0     | 2099.0        | 2011.0  |
| INSR_TYPE          | 656294.0   | 1201.73        | 0.4467          | 1201.0 | 1201.0     | 1202.0        | 1202.0     | 1204.0        | 1202.0  |
| INSURED_VALUE      | 656294.0   | 487090.80      | 900957.37       | 0.0    | 0.0        | 165021.67     | 700000.0   | 25000000.0    | 0.0     |
| PREMIUM            | 656274.0   | 7594.31        | 14353.20        | 0.0    | 755.0      | 3412.3        | 9691.02    | 7581230.43    | 347.7   |
| PROD_YEAR          | 656198.0   | 2003.88        | 10.39           | 1950.0 | 1999.0     | 2007.0        | 2012.0     | 2018.0        | 2012.0  |
| SEATS_NUM          | 656132.0   | 5.90           | 10.97           | 0.0    | 2.0        | 4.0           | 4.0        | 199.0         | 4.0     |
| CARRYING_CAPACITY  | 487155.0   | 418.66         | 3640.36         | 0.0    | 0.0        | 5.5           | 15.0       | 1000000.0     | 0.0     |
| CCM_TON            | 656287.0   | 3132.99        | 3360.00         | 0.0    | 280.0      | 2494.0        | 4164.0     | 20000.0       | 0.0     |
| CLAIM_PAID         | 60096.0    | 256677.12      | 1495929.83      | 0.0    | 13503.74   | 34699.92      | 134102.5   | 15244576.49   | 40000.0 |



## Interpretación de las distribuciones de las variables numéricas
![Distribuciones de variables numéricas](../Image/distribuciones_variables.png)

A continuación se interpreta la distribución de las principales variables numéricas del dataset:

## Interpretación de los histogramas y curvas de densidad (KDE) de las variables numéricas

A continuación se describe la distribución de cada variable según sus histogramas y líneas de densidad (KDE):

- **SEX**  
  La variable es prácticamente binaria: dos grandes grupos, uno cerca de 0 (probable femenino) y otro cerca de 1 (probable masculino). Un pequeño grupo en 2 puede ser error o una categoría poco frecuente. La media está cerca de 0.66, reflejando el desequilibrio entre ambos grupos.

- **EFFECTIVE_YR**  
  Predomina el rango 2010-2020. El KDE muestra concentración en años recientes y algunos valores dispersos hacia años futuros, que pueden ser datos erróneos o placeholders. La media está justo por encima de 2019.

- **INSR_TYPE**  
  La mayoría de los registros tienen el mismo valor (1202). El KDE confirma que es una variable prácticamente constante, lo que limita su valor analítico.

- **INSURED_VALUE**  
  Fuerte asimetría hacia la derecha: la mayoría de los valores asegurados son bajos, pero existen outliers extremadamente altos. El KDE resalta la concentración en valores bajos y cola larga hacia la derecha.

- **PREMIUM**  
  Muestra un patrón similar a `INSURED_VALUE`: gran concentración de primas bajas y muy pocos registros con primas elevadas. El KDE ilustra una fuerte asimetría y la existencia de outliers.

- **PROD_YEAR**  
  Se observa un aumento progresivo en el número de vehículos fabricados desde 1960, con una concentración notable a partir del año 2000. El KDE muestra que la mayoría de los vehículos asegurados son relativamente recientes. La media ronda el año 2003.

---

> **Observaciones:**  
> La combinación de histogramas y KDE permite identificar tanto la concentración de datos como la presencia de outliers y asimetrías en la distribución de las variables.
 > La presencia de valores atípicos y posibles errores en algunas variables sugiere la necesidad de una limpieza de datos previa a cualquier análisis profundo.

---

## Análisis de las variables categóricas

Las variables categóricas presentan las siguientes estadísticas básicas

| Variable      | count    | unique | top      | freq    |
|---------------|----------|--------|----------|---------|
| TYPE_VEHICLE  | 656294   | 11     | Truck    | 121587  |
| MAKE          | 656289   | 797    | TOYOTA   | 236751  |
| USAGE         | 656294   | 14     | Private  | 175970  |

![Distribuciones de variables numéricas](../Image/distribuciones_var_cat.png)
## Interpretación de los histogramas de variables categóricas

La gráfica presenta la distribución de frecuencia para tres variables categóricas principales del dataset:

- **TYPE_VEHICLE:**  
  La mayoría de los registros corresponden a camiones (*Truck*), automóviles (*Automobile*) y motocicletas (*Motorcycle*). También hay una presencia significativa de *Pick-up* y *Bus*. Otras categorías como *Station Wagons*, *Trailers*, *Special Construction*, *Tanker* y *Trade plates* tienen una frecuencia considerablemente menor.

- **MAKE:**  
  Existe una gran cantidad de marcas diferentes (altísima cardinalidad), lo que provoca que las etiquetas en el eje X sean ilegibles y se solapen. Esto es típico en bases de datos con mucha variedad de fabricantes y sugiere que para análisis visuales o de modelado será necesario agrupar, filtrar o trabajar solo con las marcas más frecuentes.

- **USAGE:**  
  El uso más común de los vehículos asegurados es *Private*, seguido de *Own Goods* y *General Cartage*. Otras categorías como *Fare Paying Passengers* y *Buses* también son relevantes, mientras que el resto de los usos tiene una representación mucho menor (*Special Construction*, *Agricultural Machinery*, *Ambulance*, *Fire Fighting*, etc.).

---

> **Notas:**  
> - En el caso de variables de alta cardinalidad como *MAKE*, es recomendable agrupar o mostrar únicamente las categorías más frecuentes para facilitar la interpretación visual y el análisis posterior.
> - Las variables *TYPE_VEHICLE* y *USAGE* presentan una distribución muy sesgada hacia pocas categorías principales, lo que puede influir en los modelos predictivos y sugiere potencial para reducción de categorías.

## Análisis de las variables tipo fecha
Las estádisticas básicas de las variables tipo fecha son:

| columna     | min_fecha  | max_fecha  | rango_dias | n_nulos | n_unicos |
|-------------|------------|------------|------------|---------|----------|
| INSR_BEGIN  | 2011-07-01 | 2018-06-30 | 2556       | 0       | 2556     |
| INSR_END    | 2011-07-13 | 2019-06-29 | 2908       | 0       | 2834     |

![Distribuciones de variables numéricas](../Image/distribuciones_var_date.png)

## Interpretación de las variables de fecha

- **INSR_BEGIN**  
  El registro más antiguo de inicio de póliza corresponde al **1 de julio de 2011** y el más reciente al **30 de junio de 2018**.  
  El rango total de días abarca **2556 días** (~7 años). No existen valores nulos en esta columna y cada fecha es prácticamente única, lo que indica que el inicio de póliza suele ser específico para cada registro.

- **INSR_END**  
  Las fechas de término de póliza van del **13 de julio de 2011** al **29 de junio de 2019**, con un rango de **2908 días** (~8 años). Tampoco hay valores nulos y la cantidad de fechas únicas es muy alta, lo que muestra también gran especificidad en el registro de fechas de finalización.

**Conclusiones:**

- Las variables de fecha `INSR_BEGIN` y `INSR_END` cubren un periodo de aproximadamente 7 a 8 años, sin valores faltantes, y presentan una alta cantidad de fechas únicas. Esto indica que prácticamente cada póliza tiene fechas de inicio y fin distintas, lo que es ideal para realizar análisis temporales detallados y segmentaciones por cohortes.
- El análisis de la duración de las pólizas muestra que la mayoría son anuales:
    - Promedio de duración: **354.7 días**
    - Moda de duración: **364 días**
    - El **95.54%** de las pólizas tienen una duración entre 360 y 370 días  
  Esto confirma que el producto es típicamente anual, con ligeras variaciones atribuibles a ajustes administrativos o de calendario.

**Impacto en Modelos Predictivos y Calidad de Datos:**

- La alta granularidad de las variables de fecha permite construir variables temporales relevantes (como antigüedad de póliza, cohortes, estacionalidad, etc.), lo que puede mejorar la capacidad predictiva de los modelos.
- Sin embargo, la discrepancia entre `EFFECTIVE_YR` y el año de `INSR_BEGIN` podría introducir inconsistencias en modelos que utilicen información temporal. Es fundamental validar y, en su caso, estandarizar el criterio de llenado de ambas variables para asegurar la coherencia y calidad de los datos.

Por ahora, los valores nulos de `EFFECTIVE_YR` se han completado con el año correspondiente de `INSR_BEGIN`, mientras se clarifica el significado exacto de esta variable. 

  En un caso real, antes de utilizar estas variables en modelado avanzado, se debería revisar con el área de negocio su definición y procedencia para evitar sesgos o errores en las conclusiones.

## Análisis cruzado

Este proyecto tiene como propósito la **segmentación de clientes según su nivel de siniestralidad**, con el fin de identificar patrones y perfiles asociados a un mayor o menor riesgo. Para ello, se define como **variable objetivo** del estudio:

- **`CLAIM_PAID`**: Importe pagado en caso de siniestro. Esta variable representa el monto asociado a un siniestro declarado. Puede contener valores nulos, lo que indica vehículos o pólizas sin siniestros reportados o sin pagos asociados.

### Consideraciones adicionales:

- **`object_id`**: Identificador único de un vehículo. Un mismo vehículo puede contar con varias pólizas a lo largo del tiempo.
  
- Información general del dataset:
  - **288,763** vehículos únicos (`object_id`).
  - **802,036** registros totales, considerando todas las pólizas.
  - **145,742** duplicados exactos, que deben ser tratados en las etapas de preprocesamiento para asegurar la calidad del análisis.

La variable `CLAIM_PAID` será empleada en análisis cruzados con el resto de variables del dataset, permitiendo comprender los factores que influyen en la siniestralidad y facilitando la toma de decisiones estratégicas.

### Análisis de la matriz de correlación para las variables numéricas

var_cruzadas
Se ha generado un mapa de calor de correlaciones entre las principales variables numéricas, incluidas:

- **`INSURED_VALUE`**: Valor asegurado.
- **`PREMIUM`**: Prima pagada.
- **`PROD_YEAR`**: Año de fabricación.
- **`SEATS_NUM`**: Número de asientos.
- **`CARRYING_CAPACITY`**: Capacidad de carga.
- **`CCM_TON`**: Cilindrada o tonelaje.
- **`CLAIM_PAID`**: Importe pagado en siniestros.


#### Correlaciones relevantes:

![Distribuciones de variables numéricas](../Image/var_cruzadas.png)

- **`INSURED_VALUE` y `PREMIUM`**: Correlación positiva moderada (**0.51**).  
  Los vehículos de mayor valor asegurado tienden a pagar primas más altas, lo cual es coherente con la lógica del mercado asegurador.

- **`INSURED_VALUE` y `CCM_TON`**: Correlación positiva baja (**0.21**).  
  Los vehículos con mayor cilindraje o tonelaje suelen tener un mayor valor asegurado.

- **`PREMIUM` y `CCM_TON`**: Correlación positiva baja (**0.32**).  
  Existe una ligera tendencia a que vehículos más potentes o grandes tengan primas más elevadas.

#### Correlaciones con la variable objetivo `CLAIM_PAID`:

- **`CCM_TON`**: Correlación positiva muy baja (**0.10**).
- **`PREMIUM`**: Correlación positiva muy baja (**0.077**).
- **`INSURED_VALUE`**: Correlación positiva muy baja (**0.06**).

Esto sugiere que no existe una relación lineal fuerte entre estas variables numéricas y el importe pagado en caso de siniestro.

---

### Análisis cruzado variables categóricas

## Interpretación de Variables Categóricas

### 1. `TYPE_VEHICLE` vs `CLAIM_PAID`

- Los tipos de vehículos como **Trucks**, **Special Construction**, y **Trailers and Semitrailers** concentran la mayor cantidad de siniestros de alto importe.
- Otros tipos como **Motorcycles**, **Automobiles** o **Station Wagons** muestran siniestros mayormente de bajo importe, con pocos o ningún caso de siniestros de importe elevado.
- Esto sugiere que vehículos pesados o de uso especializado tienden a estar involucrados en siniestros más costosos, lo cual es coherente debido a su tamaño, peso y uso industrial.

---

### 2. `MAKE` (Marca) vs `CLAIM_PAID`

- Se observa una gran cantidad de marcas, muchas de ellas con una distribución de siniestros baja o nula.
- Algunas marcas específicas concentran siniestros de importe elevado, aunque por la cantidad de categorías y el solapamiento visual es difícil identificar patrones precisos sin un resumen numérico o gráfico más limpio (por ejemplo, usando agregados como promedio o mediana por marca).
- Es recomendable reducir esta variable, al menos visualmente, agrupando marcas con pocos registros en una categoría "Others" para facilitar el análisis.

---

### 3. `USAGE` (Uso) vs `CLAIM_PAID`

- Los usos como **General Carriage**, **Agricultural Any**, y **Fare Paying Passenger** están asociados a siniestros de importe elevado.
- Otros usos, como **Taxi**, **Fire Fighting**, o **Ambulance**, tienden a tener siniestros de bajo importe o directamente no presentan siniestros significativos.
- El patrón sugiere que ciertos usos, como el transporte de carga o pasajeros, están más expuestos a siniestros costosos, mientras que otros, de uso ocasional o especializado, presentan siniestralidad baja o nula.

---

## Conclusiones Generales

✅ El tipo de vehículo, marca y uso están relacionados con el importe pagado en siniestros, aunque la variabilidad interna dentro de cada categoría es alta.
✅ Los siniestros de mayor importe se concentran principalmente en vehículos pesados, de transporte, de carga o agrícolas.
✅ Algunas marcas específicas y usos están asociados a siniestros costosos, mientras que otros apenas presentan siniestralidad significativa.
✅ Las distribuciones muestran la presencia de muchos valores extremos (outliers), lo que sugiere que es necesario tener precaución en el tratamiento de estos valores durante el modelado.


## Análisis de Inconsistencias

# Análisis de Posibles Inconsistencias del Dataset

A partir del análisis exploratorio, los gráficos de dispersión, las correlaciones y las comparativas de variables categóricas, se pueden identificar los siguientes puntos que podrían indicar **inconsistencias, problemas de calidad o aspectos a revisar en el dataset**:

---

## 1. Valores Extremos Anómalos (`CLAIM_PAID`)

- En múltiples gráficos (dispersión, violines y barras), se observan **siniestros con importes extremadamente altos**, que superan los 100 millones en la variable `CLAIM_PAID`.
- Si bien es posible que existan siniestros de alto coste, el valor de algunos siniestros parece **desproporcionado en comparación con el valor asegurado (`INSURED_VALUE`) o la prima (`PREMIUM`)**, lo que puede ser señal de:
  - Errores de captura (ej. unidades incorrectas, ceros de más).
  - Casos excepcionales no representativos que requieren validación o tratamiento como outliers.

**Recomendación:** Verificar los registros con los siniestros de importe más alto y contrastarlos con el valor asegurado y el tipo de vehículo.

---

## 2. Inconsistencias entre Tipo de Vehículo y Uso

- Se observan vehículos clasificados como **Motorcycle** o **Automobile** con siniestros muy elevados, lo que no es consistente con su valor asegurado promedio o su naturaleza.
- De forma similar, ciertos usos como **Taxi**, **Ambulance**, o **Fire Fighting**, que en teoría deberían tener siniestralidad controlada, presentan casos aislados de siniestros muy elevados.

**Recomendación:** Revisar los cruces entre `TYPE_VEHICLE`, `USAGE` y los siniestros de alto importe para detectar posibles errores en la asignación de estas categorías.

---

## 3. Distribución Atípica de Fechas

- Las variables relacionadas con fechas (`PROD_YEAR`, `INSR_BEGIN_year`, `INSR_END_year`, etc.) mostraron dispersión poco clara o posibles inconsistencias:
  - Vehículos con años de fabricación inusuales.
  - Fechas de inicio o fin de pólizas que no corresponden a periodos lógicos o cronológicos.

**Recomendación:** Validar rangos de fechas, detectar registros con fechas incoherentes y corregir o excluir según corresponda.

---

## 4. Cantidad Excesiva de Categorías en Variables como `MAKE`

- La variable `MAKE` presenta una cantidad elevada de marcas, algunas con muy pocos registros.
- Esto puede indicar:
  - Errores de tipografía en los nombres de marcas.
  - Codificación inconsistente (mayúsculas, minúsculas, caracteres especiales).
  - Marcas poco frecuentes que deben ser agrupadas.

**Recomendación:** Realizar limpieza de texto, normalización de categorías y, si es necesario, agrupación en categorías como "Otros" para reducir ruido en los análisis y modelos.

---

## 5. Posible Duplicidad de Registros

- Según datos iniciales del dataset:
  - **Filas totales:** 802,036  
  - **Duplicados exactos:** 145,742  
- La alta cantidad de duplicados puede ser:
  - Lógica si un vehículo tiene múltiples pólizas.
  - Problemática si los duplicados son registros idénticos que no deberían repetirse.

**Recomendación:** Revisar si los duplicados corresponden a situaciones válidas (renovaciones de póliza, cambios en la prima, etc.) o si existen duplicados exactos indebidos que deben ser eliminados.

---

# Conclusión General

Aunque el dataset permite realizar análisis iniciales y se observan patrones consistentes, también existen señales claras de posibles inconsistencias que deben ser revisadas antes de profundizar en el modelado predictivo:

✅ Validar valores extremos en siniestros.  
✅ Revisar coherencia entre tipo de vehículo, uso y siniestralidad.  
✅ Depurar y normalizar variables categóricas como `MAKE`.  
✅ Depurar duplicados y validar la consistencia de fechas.  

Abordar estos aspectos es clave para asegurar que los modelos predictivos y segmentaciones resultantes sean robustos y confiables.

Al ejecutar las reglas sobre el dataset se obtienen los siguientes resultados:
- Regla 1 - Registros con siniestros de importe inusualmente alto: 225 encontrados
- Regla 2 - Vehículos pequeños con siniestros inusualmente altos: 3 encontrados
- Regla 3 - Registros con fechas incoherentes: 0 encontrados
Regla 4 - Registros con marcas poco frecuentes o sospechosas: 1507 encontrados

# Preprocesado de Datos

## Gestión de Nulos

El primer paso en el preprocesamiento consiste en gestionar correctamente los valores nulos, asegurando que los datos estén listos para los modelos predictivos.

### 1. Tratamiento de la columna `CLAIM_PAID`

Los valores nulos en la columna `CLAIM_PAID` no se imputan de forma tradicional, ya que en este caso representan pólizas **sin siniestro**. Por lo tanto:

✅ Los valores nulos se completan con `0`, indicando que no hubo siniestro.  
✅ Se crea una nueva columna binaria llamada `HAS_CLAIM` que indica:  
- `1` si hubo siniestro (valor de `CLAIM_PAID` > 0)  
- `0` si no hubo siniestro  

---

### 2. Imputación de Nulos por Distribución

Para el resto de las columnas con valores nulos, se aplica un proceso de imputación según la **distribución de los datos**:

- Si la columna es **numérica** y su asimetría absoluta (`|skewness|`) es menor que un umbral (`skew_threshold`, por defecto `0.5`), se imputa con la **mediana**.  
- Si la columna es **numérica** y `|skewness|` es mayor o igual al umbral, se imputa con la **moda**.  
- Si la columna **no es numérica**, se imputa siempre con la **moda**.  

Este enfoque garantiza que la imputación sea coherente con la distribución de cada variable, evitando distorsiones en el análisis o modelado.

---

Este procedimiento garantiza que los datos quedan listos para su posterior análisis o modelado, respetando su estructura y evitando introducir sesgos artificiales.

## Gestión de Outliers
las variables que se consideran que tienen outliers son: 
Número de outliers por variable:
                   n_outliers
   SEX                         0 ok
EFFECTIVE_YR            87731 ok
INSR_TYPE                 255 ok
INSURED_VALUE           41290 ok
PREMIUM                 58660 ok
PROD_YEAR               12671
SEATS_NUM              126287 ok
CARRYING_CAPACITY      114172 ok
CCM_TON                 40492 ok
CLAIM_PAID              60057 ok

a continuación se presenta el tratamiento que se realiza a cada caso
### Tratamiento de `SEX`
| Valor | Interpretación común |
| ----- | -------------------- |
| **0** | Femenino             |
| **1** | Masculino            |

El valor 2 claramente no pertenece al esquema binario estándar y puede deberse a:

✅ Error de carga o tipado
✅ Codificación extendida (por ejemplo, otro género)

Para poder modelar y al no tener información adicional para eliminar los outliers suponiendo que 2 es un error o una variante de masculino. se realiza una imputación de valores proporcionales con el siguiente resultado: 
SEX
1    299845
0    289138
2     67311
Name: count, dtype: int64
Proporción Femenino (0): 49.09%
Proporción Masculino (1): 50.91%
SEX
1    0.50909
0    0.49091
Name: proportion, dtype: float64

### Análisis de Factores que Pueden Influir en Indemnizaciones Elevadas (`CLAIM_PAID`)

Vamos a analizar los factores que podrían influir en que esas indemnizaciones (`CLAIM_PAID`) sean tan elevadas.

#### Variables que pueden influir y que se observan en los datos:

✅ **INSURED_VALUE** *(Valor asegurado)*  
Los vehículos con mayor valor asegurado tienden a generar indemnizaciones más altas.  

**Ejemplos:**  
- IVECO Tanker → 2,363,510.00 asegurado → 105,388.20 de siniestro  
- IVECO Truck → 2,600,000.00 asegurado → 23,840.01 de siniestro  

---

✅ **TYPE_VEHICLE** *(Tipo de vehículo)*  
Vehículos como **Tanker**, **Truck** y **Pick-up**, que suelen ser de uso comercial o transporte pesado, tienden a estar expuestos a daños más costosos.  
Los automóviles privados pueden tener siniestros altos si hay daños severos.  

---

✅ **USAGE** *(Uso del vehículo)*  
- **General Cartage** y **Own Goods** implican transporte de mercancías, lo que suele estar asociado a mayor riesgo y siniestros costosos.  
- **Private** (uso privado) generalmente implica menor exposición, pero no garantiza siniestros bajos, como se ve en el caso del automóvil privado.  

---

✅ **CCM_TON** *(Cilindrada o tonelaje)*  
Vehículos pesados con alta cilindrada o tonelaje suelen tener mayor valor y costos asociados a daños.  

**Ejemplo:**  
- IVECO Tanker y Truck → 12,880.0 CCM_TON  
- TOYOTA Pick-up → 2,494.0 CCM_TON  
- TOYOTA Automóvil → 4,164.0 CCM_TON  

---

✅ **PREMIUM** *(Prima pagada)*  
Vehículos con primas más altas suelen estar asociados a mayor riesgo o mayor valor asegurado, lo que puede reflejarse en siniestros más altos.  

---

#### Conclusión rápida

✔ Sí tiene **cierto sentido** que esos siniestros sean tan altos, dadas las siguientes combinaciones:  

- Vehículos comerciales o de carga pesada (**Tanker**, **Truck**, **Pick-up**)  
- Altos valores asegurados  
- Alto tonelaje  
- Uso comercial (**Own Goods**, **General Cartage**)  

Incluso el automóvil privado (fila 62) tiene una indemnización alta, pero también es un **TOYOTA** con valor asegurado respetable y cilindrada alta.  

**Ejemplo de los datos**
| SEX | INSR_BEGIN | INSR_END   | EFFECTIVE_YR | INSR_TYPE | INSURED_VALUE | PREMIUM  | PROD_YEAR | SEATS_NUM | CARRYING_CAPACITY | TYPE_VEHICLE | CCM_TON | MAKE  | USAGE           | CLAIM_PAID | HAS_CLAIM |
|-----|------------|------------|---------------|------------|----------------|-----------|------------|------------|--------------------|----------------|------------|---------|-----------------|-----------------|--------------|
| 0   | 2013-08-08 | 2014-08-07 | 2008.0       | 1202      | 285451.24     | 4286.90  | 2010.0    | 4.0        | 7.0                | Pick-up       | 2494.0   | TOYOTA | Own Goods       | 19894.43   | 1          |
| 0   | 2012-08-08 | 2013-08-07 | 2008.0       | 1202      | 285451.24     | 4286.65  | 2010.0    | 4.0        | 7.0                | Pick-up       | 2494.0   | TOYOTA | Own Goods       | 26916.44   | 1          |
| 1   | 2011-11-19 | 2012-11-18 | 2011.0       | 1202      | 2363510.00    | 30371.49 | 2010.0    | 2.0        | 18000.0            | Tanker        | 12880.0  | IVECO  | General Cartage | 105388.20  | 1          |
| 0   | 2012-07-08 | 2013-07-07 | 2097.0       | 1201      | 164516.00     | 3413.05  | 1993.0    | 5.0        | 0.0                | Automobile    | 4164.0   | TOYOTA | Private         | 70809.30   | 1          |
| 1   | 2011-10-12 | 2012-10-11 | 2072.0       | 1202      | 2600000.00    | 38728.40 | 2010.0    | 1.0        | 155.9              | Truck         | 12880.0  | IVECO  | General Cartage | 23840.01   | 1          |

### Justificación sobre el Tratamiento de `CLAIM_PAID` Elevados

En este análisis, **los valores elevados de `CLAIM_PAID` no serán tratados como outliers a eliminar ni como errores de registro.**

### ¿Por qué no se consideran outliers?

- Los siniestros elevados tienen **una explicación clara y consistente en las variables asociadas**, como:
  - Alto valor asegurado (`INSURED_VALUE`)
  - Vehículos de gran tonelaje (`CCM_TON`)
  - Uso comercial o de transporte de mercancías (`USAGE`)
  - Tipos de vehículos con mayor exposición y costos potenciales (`TYPE_VEHICLE`)
   Estas variantes asociadas no se consideraran outliers 


- Estos valores extremos **forman parte de la naturaleza del riesgo asegurado**, especialmente en flotas comerciales, camiones pesados y vehículos de carga. Eliminarlos sería perder información clave sobre los casos más costosos y más relevantes para el negocio asegurador.

### ¿Cómo se abordarán los `CLAIM_PAID` elevados?

- Se utilizarán como insumo fundamental para realizar **una segmentación de riesgos mediante técnicas de clustering no supervisado**.
- El clustering permitirá **agrupar automáticamente los registros en clústeres de riesgo**, detectando patrones ocultos y proporcionando explicaciones basadas en las propias características de los datos.
- Este enfoque:
  - No impone supuestos previos sobre los grupos.
  - Identifica segmentos de vehículos con diferentes niveles de riesgo de manera objetiva y basada en datos.
  - Facilita una mejor comprensión y gestión del portafolio asegurado.

### Beneficio del enfoque

Este tratamiento permite **conservar la heterogeneidad real del negocio** y entender cómo ciertos tipos de vehículos, usos y características específicas explican los siniestros más altos, en lugar de excluirlos como anomalías estadísticas.

El objetivo es desarrollar **segmentaciones de riesgo reales y accionables** que representen el comportamiento natural del portafolio y contribuyan a mejorar la toma de decisiones en suscripción y tarificación.

# Segmentación de riesgos mediante técnicas de clustering no supervisado

## Elección de K-Means para Segmentación de Perfiles de Riesgo

## Elección de K-Means para Segmentación de Perfiles de Riesgo

En el presente análisis, se evaluaron distintos enfoques de clustering con el objetivo de identificar perfiles de riesgo diferenciados dentro del conjunto de datos de pólizas de seguro.

Inicialmente, se exploró el uso de algoritmos robustos como **DBSCAN**, que permite detectar agrupaciones basadas en densidades y es particularmente útil para identificar *outliers* de forma automática. Sin embargo, en este caso específico, DBSCAN presentó las siguientes limitaciones:

- Generación excesiva de micro-clústeres no interpretables.
- Alta proporción de registros clasificados como "ruido" o *outliers*, dificultando una segmentación estructurada.
- Sensibilidad elevada a los parámetros `eps` y `min_samples`, lo que dificultó obtener resultados consistentes a nivel global del dataset.

Dado el objetivo del proyecto —clasificar de forma práctica y comprensible los perfiles de riesgo— se optó finalmente por utilizar **K-Means**, debido a sus ventajas:

✔ Permite una segmentación clara y controlada definiendo previamente el número de grupos (K).  
✔ Es eficiente y escalable, adecuado para trabajar con grandes volúmenes de datos como los del presente análisis.  
✔ Los grupos resultantes son de fácil interpretación al analizar sus centroides y características promedio.  
✔ La identificación de perfiles de riesgo se complementa al separar previamente los casos extremos ("Muy Alto" riesgo) mediante análisis estadístico (*Z-score* y percentiles).  

La selección del número óptimo de clústeres se realizó aplicando el **método del codo**, garantizando un balance entre simplicidad y representatividad de los grupos.

### ⚡ Conclusión

**K-Means** proporciona en este contexto una solución robusta, interpretativa y eficiente para la segmentación de perfiles de riesgo, permitiendo a las áreas de negocio comprender y actuar sobre los diferentes grupos identificados.

## Clustering de Perfiles de Riesgo mediante K-Means

Para la segmentación de los perfiles de riesgo se implementó el algoritmo **K-Means**, una técnica de agrupamiento no supervisado que permite identificar grupos de registros con características similares dentro de los datos de pólizas de seguro.

### Selección del Número Óptimo de Clústeres

La elección del número de clústeres (K) es un aspecto clave en la efectividad del modelo. Para ello, se aplicó el **método del codo**, que consiste en graficar la inercia (suma de las distancias cuadráticas de los puntos a su centroide más cercano) en función del número de clústeres.

En el gráfico obtenido, se observa una disminución progresiva de la inercia a medida que aumenta K. Sin embargo, a partir de **K = 4 o 5**, la tasa de disminución comienza a estabilizarse, generando un punto de inflexión o "codo" en la curva.
![selección de numero de cluster](../Image/codo.png)
Este comportamiento indica que, a partir de ese punto, incrementar el número de clústeres aporta beneficios marginales en la compactación de los grupos, por lo que se considera óptimo trabajar con **4 o 5 clústeres** para lograr un balance entre simplicidad y representatividad.



### Ventajas de K-Means en este Contexto

- Permite identificar grupos de riesgo diferenciados dentro del conjunto de pólizas.
- Genera agrupamientos de fácil interpretación mediante el análisis de los centroides.
- Es un método eficiente y escalable, adecuado para los volúmenes de datos utilizados.
- Complementa el análisis previo, donde los casos extremos de "Muy Alto" riesgo se detectaron y clasificaron por separado mediante criterios estadísticos.

### Selección de grupos con K-Means

![gráfica de clusters](../Image/k-Means1.png)
La gráfica representa la proyección de los datos en dos dimensiones mediante **Análisis de Componentes Principales (PCA)**, lo que permite visualizar de forma simplificada la distribución de los registros y la separación de los grupos generados por el algoritmo **K-Means**.

## Observaciones clave:

✅ Se observan **4 clústeres diferenciados**, representados por distintos colores:

- **Clúster 0** (rojo)  
- **Clúster 1** (azul)  
- **Clúster 2** (verde)  
- **Clúster 3** (morado)  

✅ La mayoría de los registros se agrupan en una zona densa, cerca del origen, lo que indica que gran parte de los datos comparten características similares en las dimensiones analizadas.

✅ Existen varios puntos dispersos alejados del núcleo principal, particularmente hacia la derecha y hacia abajo del gráfico. Estos registros corresponden a casos con **características atípicas** dentro del conjunto, posiblemente relacionados con **valores extremos** en variables como `INSURED_VALUE` o `PREMIUM`.

✅ Algunos de estos casos extremos fueron asignados al **clúster 1** (azul), lo que sugiere que este grupo podría estar absorbiendo tanto registros "normales" como ciertos **valores atípicos**.

---

⚠️ **Conclusión técnica**:

- El clustering logró **separar parcialmente los perfiles de riesgo**, con varios grupos diferenciados dentro del núcleo de datos.
- Sin embargo, la presencia de registros muy dispersos indica que algunos **valores extremos** siguen presentes y deben analizarse por separado.
- Los resultados refuerzan la decisión de **identificar previamente los casos de "Muy Alto" riesgo** mediante **Z-score** o **percentiles**, y tratarlos como una categoría aparte antes de aplicar clustering convencional.

## Clustering con Filtro de Riesgo Normal

Previo al proceso de segmentación, se implementó un preprocesado para identificar y aislar los registros con características extremas o atípicas, utilizando un enfoque estadístico con **Z-Score** y percentiles. Este paso permite reducir la distorsión en el clustering provocada por outliers.

### Proceso aplicado:

- ✔ Se crean categorías de riesgo: `"Normal"` y `"Very High"` (alto riesgo) en función de Z-Score y percentiles.  
- ✔ Se filtran y se conservan únicamente los registros de categoría `"Normal"` para la segmentación.  
- ✔ Se calcula el número óptimo de clústeres mediante el **método del codo**, determinando que **K = 5** es adecuado.  
- ✔ Se entrena un modelo de **K-Means** con los registros filtrados para obtener una segmentación robusta y clara.  

---
![gráfica de clusters](../Image/k-Means2.png)
### 🔎 Interpretación del Gráfico PCA con K-Means (K=5)

- Se observan **5 clústeres diferenciados**, representados mediante colores distintos.  
- La separación entre los grupos es razonablemente clara, destacándose los clústeres extremos, como:  
  - **Clúster 0 (rojo)**  
  - **Clúster 2 (verde)**  
- Existe cierto solapamiento en la zona central, particularmente entre los clústeres **1 (azul)** y **4 (naranja)**, lo cual es esperado en datos reales y se ve amplificado por la reducción dimensional aplicada con PCA.  
- En general, los grupos son compactos y siguen una distribución coherente que sugiere la existencia de patrones subyacentes en los datos.

Una vez analizada la gráfica, se presenta a continuación una tabla con la clasificación asignada a cada clusters: | Color Aproximado | Cluster | Nivel de Riesgo |
| ---------------- | ------- | --------------- |
| Rojo             | 0       | Bajo Riesgo     |
| Azul             | 1       | Medio Riesgo    |
| Verde            | 2       | Alto Riesgo     |
| Morado / Violeta | 3       | Muy Alto Riesgo |
| Naranja          | 4       | Muy Alto Riesgo |


---

### ✅ Conclusión:

Este proceso de filtrado previo y clustering con K-Means permite identificar perfiles de riesgo diferenciados de manera más precisa, evitando el efecto distorsionante de los casos extremos y facilitando una segmentación interpretable para la toma de decisiones en el negocio.


## 📊 Documentación de Dashboards Power BI - Análisis de Riesgo y Siniestralidad

### 📁 Archivos entregados
Debido a la falta de licencia para compartir informes en línea o en entornos web, este proyecto se entrega en dos formatos:
- **Archivo .pbix de Power BI Desktop**
- **Archivo .PDF con visualizaciones de los dashboards**

---

## 🔍 Descripción de los Dashboards

### 1. **Dashboard de Estudio de Siniestralidad**
Este panel permite explorar la siniestralidad del portafolio de seguros mediante múltiples filtros disponibles en una barra superior (tipo de vehículo, marca, sexo, tipo de póliza, entre otros).

#### Componentes:
- Segmentación dinámica por características de las pólizas.
- Indicadores clave como:
  - Total de siniestros (€)
  - Ratio de siniestralidad (%)
  - Siniestro medio (€)
  - Frecuencia de siniestros (%)
  - Beneficios (%) y primas cobradas.
- Visualización de siniestros por tipo de vehículo, sexo y tipo de seguro.
- Evolución histórica (2011–2018) de las principales métricas.

#### 🧑‍💼 Uso:
Selecciona cualquier combinación de filtros para observar cómo varían las métricas de siniestralidad a lo largo del tiempo o entre distintos perfiles de póliza.

---

### 2. **Dashboard de Segmentación de Clientes**
Este panel presenta la segmentación de clientes realizada a través del algoritmo de clustering **K-Means**, clasificándolos por **nivel de riesgo**.

#### Componentes:
- Visualización de clusters en un gráfico de dispersión (PCA).
- Distribución de características de los clientes por nivel de riesgo:
  - Promedio de valor asegurado
  - Promedio de primas
  - Promedio de siniestros
- Proporción de siniestros por **marca del vehículo** y por **uso del vehículo**.

#### 🧑‍💼 Uso:
Interactúa con los filtros para explorar cómo se comportan los distintos clusters de clientes en términos de siniestralidad y prima. Ideal para identificar perfiles de alto riesgo y potenciales oportunidades de optimización.

---

### 3. **Dashboard de Análisis de Riesgo del Nuevo Cliente**
Este panel permite **analizar dinámicamente el riesgo de un nuevo cliente** en tiempo real utilizando un script de Python embebido que aplica K-Means sobre los datos históricos para predecir su nivel de riesgo.

#### Componentes:
- Entrenamiento automático con datos históricos (2011–2018).
- Asignación de nivel de riesgo a un nuevo cliente ingresado.
- Visualización de las principales características asociadas al cluster asignado.
- Comparación del cliente con perfiles existentes.

#### 🧑‍💼 Uso:
1. Ingresar las características del nuevo cliente.
2. Ejecutar el script embebido.
3. Observar en qué cluster de riesgo se clasifica.
4. Analizar visualmente las métricas clave y comparar con clientes similares.

---

### 4. **Tooltip dinámico por Nivel de Riesgo**
Función complementaria mostrada como parte de la visualización de dispersión en los paneles de segmentación. Al pasar el cursor sobre un punto del gráfico:

#### Componentes:
- Muestra información específica del cliente según su clasificación en el cluster.
- Presenta las características top de siniestralidad asociadas al nivel de riesgo.

#### 🧑‍💼 Uso:
Al explorar la gráfica de dispersión, pasa el cursor sobre cualquier punto para obtener detalles contextuales enriquecidos sobre ese cliente/cluster.

---

## 🛠️ Requisitos para Uso
- **Power BI Desktop instalado**.
- Si se desea ejecutar el script de Python:
  - Tener Python instalado y correctamente configurado en Power BI.
  - Librerías necesarias: `pandas`, `sklearn`, entre otras usadas para KMeans.
