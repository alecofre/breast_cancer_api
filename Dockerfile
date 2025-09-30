# Imagen base
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY modelo.pkl .
COPY api_flask.py .
COPY requirements.txt .

# Instalar las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto en el que se ejecutará la API
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "api_flask.py"]

# Instrucciones para construir y ejecutar el contenedor:
# 1. Construir la imagen:   docker build -t mlm10_api .
# 2. Ejecutar el contenedor: docker run -d -p 5000:5000 mlm10_api   # -d para modo desatendido, -p para mapear puertos
# 3. Probar la API:        python test_api.py
# 4. Detener el contenedor: docker ps (para obtener el ID) y luego docker stop <container_id>
# 5. (Opcional) Eliminar la imagen: docker rmi mlm10_api
# Nota: Asegúrate de que el puerto 5000 esté libre en tu máquina local antes de ejecutar el contenedor.
# Puedes verificar los contenedores en ejecución con: docker ps
# Si necesitas reconstruir la imagen después de hacer cambios, usa: docker build --no-cache -t mlm10_api .
