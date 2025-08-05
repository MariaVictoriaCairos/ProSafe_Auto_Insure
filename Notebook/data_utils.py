# ——————————————————————————————
# Importaciones de las librerías 
# ——————————————————————————————

import pandas as pd  # Para manipulación de datos tabulares
import numpy as np  # Para operaciones numéricas y manejo de arrays
import datetime       # Para normalizar y manipular fechas
import re             # Para normalización y validación de cadenas de fecha
import math           # Para operaciones matemáticas básicas (p.ej. funciones trigonométricas)

# ——————————————————————————————
# Importaciones para tipado
# ——————————————————————————————

from typing import Union, List  
# Union: para anotar parámetros o retornos que pueden tener varios tipos  
# List: para anotar listas con tipos de elemento específicos

# ——————————————————————————————
# Librerías de terceros: cálculo y análisis de datos
# ——————————————————————————————

import numpy as np    # Cálculo numérico y álgebra de matrices
import pandas as pd   # Manipulación y análisis de estructuras de datos tabulares

from scipy.stats import gaussian_kde  
# gaussian_kde: estimación de densidad kernel univariada/multivariada

# ——————————————————————————————
# Librería de visualización
# ——————————————————————————————

import matplotlib.pyplot as plt  
# plt: interfaz de Matplotlib para crear gráficos (líneas, histogramas, scatter, etc.)





# ------------------------------------------------------
# Función para imputar valores nulos en columnas de un DataFrame por distribución de los datos
# --------------------------------------------------------
def imputar_nulos_por_distribucion(
    df: pd.DataFrame,
    columnas: Union[str, List[str]],
    skew_threshold: float = 0.5
) -> pd.DataFrame:
    """
    Imputa los valores nulos en una o varias columnas del DataFrame `df`
    según la simetría de su distribución:
      - Si la columna es numérica y |skewness| < skew_threshold: se imputa con la mediana.
      - Si la columna es numérica y |skewness| ≥ skew_threshold: se imputa con la moda.
      - Si no es numérica: se imputa siempre con la moda.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame de entrada (modificado in-place).
    columnas : str o list[str]
        Nombre de la columna, o lista de nombres de columnas, a imputar.
    skew_threshold : float, opcional
        Umbral de asimetría para elegir mediana vs. moda (por defecto 0.5).

    Devuelve
    -------
    pd.DataFrame
        El mismo DataFrame con las columnas imputadas.
    """
    if isinstance(columnas, (list, tuple)):
        for col in columnas:
            imputar_nulos_por_distribucion(df, col, skew_threshold)
        return df

    col = columnas

    if df[col].isnull().sum() == 0:
        return df  # Nada que imputar

    modos = df[col].mode()
    moda  = modos[0] if not modos.empty else None

    if pd.api.types.is_numeric_dtype(df[col]):
        skewness = df[col].skew(skipna=True)
        media    = df[col].mean()
        mediana  = df[col].median()

        print(f"Asimetría (skewness) de '{col}': {skewness:.3f}")
        print(f"Media    de '{col}': {media:.3f}")
        print(f"Mediana  de '{col}': {mediana:.3f}")
        print(f"Moda     de '{col}': {moda}")

        if abs(skewness) < skew_threshold:
            print(f"Distribución aproximadamente simétrica (|skew| < {skew_threshold}), imputando con mediana.\n")
            df[col] = df[col].fillna(mediana)
        else:
            print(f"Distribución asimétrica (|skew| ≥ {skew_threshold}), imputando con moda.\n")
            df[col] = df[col].fillna(moda)
    else:
        print(f"Columna '{col}' no numérica, imputando con moda: {moda}\n")
        df[col] = df[col].fillna(moda)

    return df



# ------------------------------------------------------
# Función para verificar si hay columnas con valores NaN
# -------------------------------------------------------
def verificar_columnas_con_nan(
    df: pd.DataFrame,
    *listas_de_columnas: List[str]
) -> List[str]:
    """
    Verifica en el DataFrame `df` cuáles de las columnas dadas contienen valores NaN.
    Imprime un mensaje con el total de nulos y el porcentaje para cada columna.
    Devuelve la lista de columnas con NaN.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame a verificar.
    *listas_de_columnas : List[str]
        Uno o más listados de nombres de columna a comprobar.

    Devuelve
    -------
    List[str]
        Lista de nombres de columna que tienen al menos un NaN.
    """
    columnas_con_nan: List[str] = []
    total_filas = len(df)

    for lista in listas_de_columnas:
        for col in lista:
            n_nulos = df[col].isnull().sum()
            porcentaje = (n_nulos / total_filas) * 100 if total_filas else 0
            if n_nulos > 0:
                print(f"Columna '{col}' SÍ tiene valores NaN: {n_nulos} ({porcentaje:.2f}%)")
                columnas_con_nan.append(col)
            else:
                print(f"Columna '{col}' NO tiene valores NaN.")
    return columnas_con_nan


# ------------------------------------------------------
# Función para normalizar fechas
# -------------------------------------------------------
# Esta función toma una cadena de texto que representa una fecha en varios formatos
# y la normaliza a un formato estándar 'DD/MM/YYYY'. Si la cadena no es válida, devuelve None.
# La función maneja fechas en español y en inglés, así como diferentes separadores.

MONTH_MAP_ES = {
    # Español largo
    'enero': '01', 'febrero': '02', 'marzo': '03', 'abril': '04',
    'mayo': '05', 'junio': '06', 'julio': '07', 'agosto': '08',
    'septiembre': '09', 'setiembre': '09', 'octubre': '10',
    'noviembre': '11', 'diciembre': '12',
    # Español corto
    'ene': '01', 'feb': '02', 'mar': '03', 'abr': '04', 'may': '05', 'jun': '06', 'jul': '07',
    'ago': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dic': '12',
    # Inglés corto y largo
    'jan': '01', 'january': '01',
    'feb': '02', 'february': '02',
    'mar': '03', 'march': '03',
    'apr': '04', 'april': '04',
    'may': '05',
    'jun': '06', 'june': '06',
    'jul': '07', 'july': '07',
    'aug': '08', 'august': '08',
    'sep': '09', 'september': '09',
    'oct': '10', 'october': '10',
    'nov': '11', 'november': '11',
    'dec': '12', 'december': '12',
    # ...agrega también español si no estaba...
}

def normalize_date(s):
    if s is None or (isinstance(s, float) and pd.isna(s)) or (type(s).__name__ == 'NaTType'):
        return None
    s = str(s).strip().replace('⁄','/').replace('–','-')
    if not s or s.lower() in ('nan', 'nat'):
        return None
    m = re.match(r'^(\d{1,2})[- /]([A-Za-zñÑ]+)[- /](\d{2,4})$', s)
    if m:
        d, mes_txt, y = m.groups()
        mm = MONTH_MAP_ES.get(mes_txt.lower())
        if mm:
            y = '20' + y if len(y) == 2 else y
            return f"{int(d):02d}/{mm}/{y}"
    m = re.match(r'^(\d{1,2})/(\d{1,2})/(\d{2,4})$', s)
    if m:
        d, mo, y = m.groups()
        y = '20' + y if len(y) == 2 else y
        return f"{int(d):02d}/{int(mo):02d}/{y}"
    return None




def convertir_columnas_a_datetime(
    df: pd.DataFrame,
    columnas: Union[str, List[str]]
) -> pd.DataFrame:
    """
    Convierte columna(s) de object a datetime, genera colname_year y colname_month.
    La columna original queda en formato datetime.
    """
    if isinstance(columnas, (list, tuple)):
        for col in columnas:
            convertir_columnas_a_datetime(df, col)
        return df

    col = columnas  # nombre de la columna a procesar

    # Función interna de parseo
    def parse_val(x):
        norm = normalize_date(str(x))
        if norm is None:
            return pd.NaT
        return pd.to_datetime(norm, format='%d/%m/%Y', errors='coerce')

    # Parsing directo de la columna
    df[col] = df[col].apply(parse_val)
    # df[f"{col}_year"] = df[col].dt.year
    # df[f"{col}_month"] = df[col].dt.month

    return df

# ------------------------------------------------------
# Estadistica personalizada para columnas numericas
# -------------------------------------------------------
def estadisticas_personalizadas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula para cada columna numérica del DataFrame:
      - mean  : media
      - median: mediana
      - std   : desviación estándar
      - min   : valor mínimo
      - 25%   : primer cuartil
      - 50%   : segundo cuartil (mediana)
      - 75%   : tercer cuartil
      - max   : valor máximo

    Devuelve un DataFrame con esas métricas como columnas
    y las variables originales como índice.
    
    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame de entrada.
    Devuelve
    -------
    pd.DataFrame
        DataFrame con las métricas calculadas.
    """
    # 1) Seleccionamos solo columnas numéricas
    num = df.select_dtypes(include='number')
    
    # 2) Calculamos todas las métricas
    stats = pd.DataFrame({
        'mean'  : num.mean(),
        'median': num.median(),
        'moda'  : num.mode().iloc[0] if not num.mode().empty else np.nan,
        'std'   : num.std(ddof=1),
        'min'   : num.min(),
        '25%'   : num.quantile(0.25),
        '50%'   : num.quantile(0.50),
        '75%'   : num.quantile(0.75),
        'max'   : num.max()
    })
    
    # 3) Reordenamos las columnas en el orden deseado,
    #    rellenando con NaN en caso de que alguna métrica falte
    desired_order = ['mean','median','moda','std','min','25%','50%','75%','max']
    stats = stats.reindex(columns=desired_order)
    
    # 4) Redondeamos a 3 decimales
    stats = stats.round(3)
    
    # Identificación de las principales variables nnumericas que serán atributos principales para el conjunto de datos
    # Para identificar cuáles de las variables numéricas son “principales” (es decir, las que más aportan 
    # variabilidad y, por tanto, más información) nos apoyamos en dos medidas claves:
    #       -   Desviación estándar: cuanto mayor, más dispersión tiene la variable.
    #       -   Rango (max − min) o IQR (75 % − 25 %): dan idea de cuán separadas están sus observaciones.
        
    # 1) Creamos rango e IQR
    stats['range'] = stats['max'] - stats['min']
    stats['IQR']   = stats['75%'] - stats['25%']

    # 2) Top 5 por desviación estándar
    top_std   = stats['std'].sort_values(ascending=False).head(5)

    # 3) Top 5 por rango
    top_range = stats['range'].sort_values(ascending=False).head(5)

    print("→ Top 5 variables por DESVIACIÓN ESTÁNDAR:")
    print(top_std)

    print("\n→ Top 5 variables por RANGO:")
    print(top_range)
    
    return stats


# ------------------------------------------------------
# Visualización gráfica de atributos numéricos
# ------------------------------------------------------
# Esta función toma un DataFrame y una lista de nombres de columnas,
# y genera histogramas para cada columna, superponiendo una línea discontinua
# que indica la media de los datos. Los histogramas se organizan en una cuadrícula de 2 filas y 3 columnas.
# Se utiliza la biblioteca matplotlib para crear las visualizaciones.


def plot_hist_with_mean_and_kde(df, atributos, bins=30):
    """
    Grafica histogramas de las columnas de `atributos` de df,
    superpone una línea discontinua indicando la media,
    y dibuja la curva de densidad (KDE) en rojo.
    
    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame que contiene los datos a graficar.
    atributos : list[str]
        Lista de nombres de columnas a graficar.
    bins : int, opcional
        Número de bins para el histograma (por defecto 30).
    """
    # Creamos el grid (2 filas x 3 columnas)
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))
    axes = axes.flatten()
    
    for ax, col in zip(axes, atributos):
        data = df[col].dropna()
        
        # Histograma normalizado
        ax.hist(data, bins=bins, density=True, alpha=0.6, edgecolor='black')
        
        # Línea vertical de la media
        mu = data.mean()
        ax.axvline(mu, linestyle='--', linewidth=2, label=f'Media: {mu:.3f}')
        
        # Curva de densidad (KDE)
        kde = gaussian_kde(data)
        x_vals = np.linspace(data.min(), data.max(), 200)
        ax.plot(x_vals, kde(x_vals), color='red', linewidth=2, label='KDE')
        
        ax.set_title(col)
        ax.set_ylabel('Densidad')
        ax.legend()
    
    # Apagamos subplots sobrantes
    for ax in axes[len(atributos):]:
        ax.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    
# ------------------------------------------------------
# Función para identificar y eliminar outliers
# -------------------------------------------------------       

def listar_outliers_y_boxplot(df, atributos):
    """
    Para cada columna en `atributos`:
     - Detecta outliers con el método IQR (1.5*IQR)
     - Almacena los valores atípicos en un dict
     - Dibuja un boxplot horizontal
    Retorna:
      outliers_dict: {columna: Series de outliers}
      fig: objeto matplotlib.figure.Figure
    """
    outliers_dict = {}
    n = len(atributos)
    
    # Creamos la figura y los ejes
    cols = 4
    rows = (n + cols - 1) // cols  # Redondeo hacia arriba
    if rows == 0:
        rows = 1

    # Creamos un grid de rows x cols
    fig, axes = plt.subplots(rows, cols,
                             figsize=(4 * cols, 4 * rows),
                             squeeze=False)
    axes = axes.flatten()
    
    for ax, col in zip(axes, atributos):
        data = df[col].dropna()
        
        # Cálculo de cuartiles e IQR
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        
        # Máscara de outliers
        mask = (data < lower) | (data > upper)
        outliers = data[mask]
        outliers_dict[col] = outliers
        
        # Boxplot Vertical
        ax.boxplot(data, vert=True, showfliers=True)
        ax.set_title(f'Boxplot de {col}')
        ax.set_xlabel(col)
        
        # anotar número de outliers
        ax.annotate(f"n outliers={len(outliers)}",
                    xy=(0.95, 0.85), xycoords='axes fraction',
                    ha='right', fontsize=9, bbox=dict(boxstyle="round,pad=0.3", 
                                                      fc="white", ec="gray"))
    
    plt.tight_layout()
    return outliers_dict, fig
# ------------------------------------------------------
def robust_scale_duration(df, column):
    """
    Reemplaza en la columna indicada todos los valores por encima del umbral
    de outliers (Q3 + 1.5 * IQR) con la mediana de la columna.
    
    Parámetros:
    - df: pandas.DataFrame
    - column: nombre de la columna a procesar
    
    Devuelve:
    - df modificado in-place con los outliers capados a la mediana.
    """
    # Cálculo de estadísticos
    median = df[column].median()
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    upper_bound = Q3 + 1.5 * IQR

    # Reemplazar outliers por la mediana
    df.loc[df[column] > upper_bound, column] = median
    return df

# ------------------------------------------------------
# función para graficar histogramas de atributos categóricos
# -------------------------------------------------------
# Esta función toma un DataFrame y una lista de nombres de columnas categóricas,
# y genera histogramas (barcharts) para cada columna, organizados en un grid de hasta 4 columnas.
# Se utiliza la biblioteca matplotlib para crear las visualizaciones.
# Se asume que las columnas categóricas son de tipo 'object' o 'category'.
# Se pueden rotar las etiquetas del eje x para mejorar la legibilidad.
# Se pueden ocultar los ejes sobrantes si hay menos columnas que filas*columnas.


import matplotlib.cm as cm

def plot_categorical_histograms(df, columns, cols=4, figsize=None, rotation=45, palette='viridis', fontsize=8):
    """
    Dibuja histogramas (barcharts) de frecuencia para cada atributo categórico en 'columns',
    organizados en un grid de hasta 'cols' columnas, usando la paleta de colores seleccionada.

    Parámetros:
    - df: pandas.DataFrame con los datos.
    - columns: lista de nombres de columnas categóricas a graficar.
    - cols: número de columnas en el grid.
    - figsize: tamaño de la figura (ancho, alto).
    - rotation: ángulo de rotación de las etiquetas del eje x.
    - palette: nombre de la paleta de colores de matplotlib a usar para las barras.
    - fontsize: tamaño de letra para etiquetas y ticks.
    """
    n = len(columns)
    rows = (n + cols - 1) // cols if cols > 0 else 1

    if figsize is None:
        figsize = (4 * cols, 4 * rows)

    # Caso especial: solo una gráfica
    if n == 1:
        fig, ax = plt.subplots(figsize=figsize)
        axes = [ax]
    else:
        fig, axes = plt.subplots(rows, cols, figsize=figsize)
        axes = axes.flatten()

    for ax, col in zip(axes, columns):
        counts = df[col].value_counts(dropna=False)
        num_bars = len(counts)
        cmap = cm.get_cmap(palette, num_bars)
        colors = [cmap(i) for i in range(num_bars)]
        counts.plot(kind='bar', ax=ax, color=colors)
        ax.set_title(f'Histograma de {col}', fontsize=fontsize+2)
        ax.set_xlabel(col, fontsize=fontsize)
        ax.set_ylabel('Frecuencia', fontsize=fontsize)
        ax.tick_params(axis='x', labelsize=fontsize, rotation=rotation)
        ax.tick_params(axis='y', labelsize=fontsize)

    for ax in axes[n:]:
        ax.set_visible(False)

    plt.tight_layout()
    plt.show()

# ------------------------------------------------------
# EDA de variables tipo datetime. funciones para resumen y visualización
# -------------------------------------------------------

def date_column_summary(df, date_cols):
    """
    Calcula estadísticas descriptivas para variables de tipo fecha.
    Parámetros:
    - df: pandas.DataFrame
    - date_cols: lista de nombres de columnas de tipo fecha

    Devuelve:
    - DataFrame resumen con: min, max, rango (días), n_nulos, n_unicos
    """
    summary = []
    for col in date_cols:
        fechas = pd.to_datetime(df[col], errors='coerce')
        min_fecha = fechas.min()
        max_fecha = fechas.max()
        rango_dias = (max_fecha - min_fecha).days if pd.notnull(min_fecha) and pd.notnull(max_fecha) else None
        n_nulos = fechas.isnull().sum()
        n_unicos = fechas.nunique()
        summary.append({
            'columna': col,
            'min_fecha': min_fecha,
            'max_fecha': max_fecha,
            'rango_dias': rango_dias,
            'n_nulos': n_nulos,
            'n_unicos': n_unicos
        })
    return pd.DataFrame(summary)


import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd

def plot_date_distributions_subplots(df, date_cols, freq='Y', figsize=(6, 4), fontsize=10, palette='viridis'):
    """
    Grafica la distribución de variables de fecha en subplots.
    
    Parámetros:
    - df: DataFrame
    - date_cols: lista de nombres de columnas de tipo fecha
    - freq: frecuencia de agrupación ('Y' año, 'M' mes, 'D' día)
    - figsize: tamaño total de la figura (ancho, alto) POR SUBPLOT
    - fontsize: tamaño de letras
    - palette: paleta de colores matplotlib a usar ('viridis', etc.)
    """
    n = len(date_cols)
    fig, axes = plt.subplots(n, 1, figsize=(figsize[0], figsize[1]*n))
    
    # Permite compatibilidad cuando solo hay una columna
    if n == 1:
        axes = [axes]

    for ax, col in zip(axes, date_cols):
        fechas = pd.to_datetime(df[col], errors='coerce').dropna()
        if len(fechas) == 0:
            ax.set_title(f'{col}: Sin fechas válidas', fontsize=fontsize+2)
            continue
        serie = fechas.dt.to_period(freq).value_counts().sort_index()
        num_bars = len(serie)
        cmap = cm.get_cmap(palette, num_bars)
        colors = [cmap(i) for i in range(num_bars)]
        serie.plot(kind='bar', ax=ax, color=colors)
        ax.set_title(f'Distribución temporal de {col}', fontsize=fontsize+2)
        ax.set_xlabel('Fecha', fontsize=fontsize)
        ax.set_ylabel('Frecuencia', fontsize=fontsize)
        ax.tick_params(axis='x', labelsize=fontsize, rotation=45)
        ax.tick_params(axis='y', labelsize=fontsize)
    plt.tight_layout()
    plt.show()

