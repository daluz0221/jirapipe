# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos (requirements.txt) al contenedor
COPY requirements.txt /app/

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de tu proyecto al contenedor
COPY . /app/

# Expone el puerto 8000 para que la app sea accesible desde el exterior
EXPOSE 8000

# Define el comando para correr la aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
