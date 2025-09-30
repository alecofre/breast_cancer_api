# Este módulo entrena un modelo de clasificación simple y lo guarda para futuros usos.
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib


# Cargar el conjunto de datos de cáncer de mama
data = pd.read_csv('data.csv')
# print(data.iloc[0])  # Imprimir la primera fila para ver su formato
y = data['diagnosis'].map({'M': 1, 'B': 0}).values  # Convertir etiquetas a 0 y 1
X = data.drop(columns=['id', 'diagnosis', 'Unnamed: 32'])
# print(X.shape, y.shape) # Verificar las dimensiones de X e y    
# print(X.iloc[0])  # Imprimir la primera fila de características para ver su formato

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalamiento de características (opcional)
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

print("Datos preparados. Comenzando el entrenamiento del modelo...")

# Entrenar un modelo de clasificación RandomForest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Guardar el modelo entrenado en un archivo usando joblib
joblib.dump(model, 'modelo.pkl')
print("Modelo entrenado y guardado como 'modelo.pkl'")