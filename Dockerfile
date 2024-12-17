# Dockerfile
FROM python:3.9

# Copia los scripts de Python al contenedor
COPY server.py /app/server.py
COPY client.py /app/client.py

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias necesarias
RUN pip install flask requests

# Comando para ejecutar el servidor por defecto
CMD ["python", "server.py"]
