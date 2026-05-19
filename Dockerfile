# Imagen base oficial de Python
FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos del proyecto al contenedor
COPY requirements.txt .
COPY crypto_info_3.0.py .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto al ejecutar el contenedor
CMD ["python", "crypto_info_3.0.py", "bitcoin", "clp", "7"]
