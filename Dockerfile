# Usa una imagen base de Python oficial, por ejemplo la versión 3.10
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requisitos e instala las dependencias
# --no-cache-dir desactivar el almacenamiento en caché de los paquetes descargados e instalados.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del proyecto (incluyendo app.py) al directorio de trabajo
COPY . .

# Expone el puerto en el que corre Flask (por defecto 5050)
EXPOSE 5050

# Comando para correr la aplicación
# Usa `python app.py` si modificaste app.run(host='0.0.0.0')
# o usa un comando más robusto si instalaste Gunicorn:
# CMD ["gunicorn", "--bind", "0.0.0.0:5050", "app:app"]
CMD ["python", "app.py"]


# Ejecutar en TU terminal
# docker build -t app-flask-chat-01 .

# el . significa copiar TODO el proyecto desde el directorio actual que es el que tiene:
# __pycache__             chat_routes.py          llm_service.py          templates
# app.py                  Dockerfile              requirements.txt        test.py

# docker run -d -p 5000:5000 --name flask-app-contenedor app-flask-chat-01

# docker logs flask-app-contenedor