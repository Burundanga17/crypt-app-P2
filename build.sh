#!/bin/bash

# ============================================================
#  build.sh — Script de automatización para Crypto Info App
#  Genera el Dockerfile, construye la imagen y ejecuta el
#  contenedor. Compatible con Jenkins (sin flags interactivos).
# ============================================================

IMAGE_NAME="crypto_app"
CONTAINER_NAME="samplerunning"

echo "=============================================="
echo " 🔨 Construyendo la imagen Docker..."
echo "=============================================="
docker build -t $IMAGE_NAME .

echo ""
echo "=============================================="
echo " 🗑️  Eliminando contenedor anterior (si existe)..."
echo "=============================================="
docker rm -f $CONTAINER_NAME 2>/dev/null || true

echo ""
echo "=============================================="
echo " 🚀 Ejecutando el contenedor..."
echo "=============================================="
docker run \
  --name $CONTAINER_NAME \
  -e CRYPTO_ID=${CRYPTO_ID:-bitcoin} \
  -e MONEDA_FIAT=${MONEDA_FIAT:-usd} \
  -e COINGECKO_API_KEY=${COINGECKO_API_KEY:-""} \
  $IMAGE_NAME

echo ""
echo "=============================================="
echo " 📋 Estado del contenedor:"
echo "=============================================="
docker ps -a --filter "name=$CONTAINER_NAME"

