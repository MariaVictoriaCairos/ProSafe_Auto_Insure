
import pandas as pd
import joblib
import os

# Evaluación de un nuevo cliente con K-Means
# Ruta base relativa al propio script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Definir rutas a los modelos
modelo_kmeans_path = os.path.join(BASE_DIR, '..', 'Modelos', 'kmeans_model.pkl')
pipeline_path = os.path.join(BASE_DIR, '..', 'Modelos', 'preprocessing_pipeline.pkl')
pca_path = os.path.join(BASE_DIR, '..', 'Modelos', 'pca_model.pkl')  # Asegúrate de haber guardado el PCA

# Cargar los modelos
kmeans = joblib.load(modelo_kmeans_path)
pipeline = joblib.load(pipeline_path)
pca = joblib.load(pca_path)

# Ruta al archivo del nuevo cliente
nuevo_cliente_path = os.path.join(BASE_DIR, '..', 'Data', 'nuevo_cliente.csv')

# Cargar datos del nuevo cliente
nuevo_cliente = pd.read_csv(nuevo_cliente_path)

# Definir las columnas que espera el modelo
features = ['SEX', 'INSURED_VALUE', 'PREMIUM', 'SEATS_NUM',
            'CARRYING_CAPACITY', 'CCM_TON', 'MAKE', 'USAGE', 'CLAIM_PAID']

# Verificar que el nuevo cliente tiene exactamente esas columnas
faltantes = set(features) - set(nuevo_cliente.columns)
extras = set(nuevo_cliente.columns) - set(features)

if faltantes:
    raise ValueError(f"Faltan las siguientes columnas en el nuevo cliente: {faltantes}")
if extras:
    print(f"Advertencia: El nuevo cliente tiene columnas adicionales que serán ignoradas: {extras}")

# Reordenar y filtrar columnas
nuevo_cliente = nuevo_cliente[features]

# Aseguramos que es de riesgo 'Normal'
nuevo_cliente['RISK_CATEGORY'] = 'Normal'

# Preprocesar los datos
nuevo_cliente_processed = pipeline.transform(nuevo_cliente)

# Asignar cluster
cluster_asignado = kmeans.predict(nuevo_cliente_processed)[0]

# Aplicar PCA
pca_result = pca.transform(nuevo_cliente_processed)

# Crear columnas PCA
nuevo_cliente['PCA1'] = pca_result[:, 0]
nuevo_cliente['PCA2'] = pca_result[:, 1]

# Agregar cluster
nuevo_cliente['Cluster_KMeans'] = cluster_asignado

# Lógica simple de riesgo (ajustar según análisis)
if cluster_asignado in [3, 4]:
    nivel_riesgo = 'Muy Alto'
else:
    nivel_riesgo = 'Normal'

nuevo_cliente['Nivel_Riesgo'] = nivel_riesgo

# Guardar resultado
resultado_path = os.path.join(BASE_DIR, '..', 'Data', 'resultado_nuevo_cliente.csv')
nuevo_cliente.to_csv(resultado_path, index=False)
print(f'Evaluación completada. Resultado guardado en {resultado_path}')