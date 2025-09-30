# Este módulo crea una API RESTful usando Flask para servir un modelo de clasificación entrenado.
from flask import Flask, request, jsonify
import joblib
import numpy as np

# Inicializar la aplicación Flask
app = Flask(__name__)

# Cargar el modelo entrenado
model = joblib.load('modelo.pkl')
print("Modelo cargado exitosamente.")

# Definir una ruta raíz para verificar que la API está funcionando
@app.route('/')
def index():
    return jsonify({'message': 'API de predicción de cancer en funcionamiento'}),200

# Define una ruta para verificar el estado de la API
@app.route('/health', methods=['GET'])  
def health():
    return jsonify({'status': 'ok'}), 200

# Define una ruta para la predicción
@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos JSON de la solicitud
    data = request.get_json(force=True)
    
    # Extraer las características del JSON
    features = np.array(data['features']).reshape(1, -1)
    # print("Características recibidas para predicción:", features)

    # Verificar que las características tienen la dimensión correcta
    if features.shape[1] != 30:
        return jsonify({'error': 'Se requieren 8 características para la predicción'}), 400
    
    if not np.issubdtype(features.dtype, np.number):
        return jsonify({'error': 'Todas las características deben ser numéricas'}), 400
    
    # Realizar la predicción
    try:
        prediction = model.predict(features)
        # print("Predicción realizada:", prediction)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    # Devolver la predicción como JSON
    return jsonify({'prediction': int(prediction[0])})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)