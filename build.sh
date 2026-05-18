#!/bin/bash

# Nombre de la imagen y contenedor
IMAGE_NAME="crypto_app"
CONTAINER_NAME="crypto_app_container"

echo "🔨 Construyendo la imagen Docker..."
docker build -t $IMAGE_NAME .

echo "🗑️ Eliminando contenedor anterior (si existe)..."
docker rm -f $CONTAINER_NAME 2>/dev/null

echo "🚀 Ejecutando el contenedor..."
docker run --name $CONTAINER_NAME -it $IMAGE_NAME
