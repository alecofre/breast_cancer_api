# breast_cancer_api
Proyecto MLops que conteneriza una api para clasificación de riesgo de cancer de mama

Este proyecto corresponde a la evaluación modular del módulo 10 del curso de Machine Learning. El objetivo principal es publicar una API de un modelo entrenado para obtener predicciones usando Flask y hacerlo a través de un contenedor Docker .

## Requisitos

- Python 3.10
- Bibliotecas principales: `numpy`, `pandas`, `scikit-learn`, `flask` (ver `requirements.txt` para detalles)

## Ejecución

1. Clona este repositorio.
2.1 (opcional) Crea un ambiente virtual
2.2 Instala las dependencias con:
   ```
   pip install -r requirements.txt
   ```
3. Ejecuta los scripts principales según las instrucciones de cada módulo.

## Archivos principales
- *data.csv* : Archivo con los datos Breast Cancer (https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data )
- *train_model.py* : Archivo de comandos para entrenar el modelo y guardarlo
- *modelo.pkl* : Modelo serializado
- *api_flask.py* : Archivo que contiene la api para acceder a las predicciones del modelo
- *test_api.py* : Archivo para testear la api en forma local
- *Dockerfile* : Archivo para generar el contenedor Docker
- *test_docker.bat* : Archivo de comandos para testear la api en el contenedor

## Autor

Alejandro Cofré

## Notas

- Este proyecto es parte de la evaluación del modulo 10 del curso y está orientado a demostrar competencias en el desarrollo de soluciones de machine learning de manera estructurada y reproducible.
