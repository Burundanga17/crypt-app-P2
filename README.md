# 📊 Crypto Info App

## 🎯 Narrativa del Proyecto

**Stakeholder:** Inversionista independiente en criptomonedas que necesita consultar métricas clave de activos digitales de forma rápida, sin depender de plataformas web con publicidad o interfaces lentas.

**Problema:**
Los inversionistas pierden tiempo navegando entre múltiples plataformas para obtener datos básicos como precio actual, capitalización de mercado y volumen de trading. No cuentan con una herramienta ligera, ejecutable desde terminal, que entregue esta información de forma inmediata y automatizable.

**Solución:**
`Crypto Info App` consulta la API pública de CoinGecko y entrega por consola un informe completo de la criptomoneda seleccionada: precio actual, máximo/mínimo de 24h, cambio porcentual, capitalización de mercado y volumen total. Todo configurable mediante variables de entorno, sin hardcoding de credenciales, y ejecutable en un contenedor Docker en segundos.

---

## ⚙️ Variables de Entorno

| Variable | Descripción | Valor por defecto |
|---|---|---|
| `CRYPTO_ID` | ID de la criptomoneda (ej: `bitcoin`, `ethereum`) | `bitcoin` |
| `MONEDA_FIAT` | Moneda de referencia (ej: `usd`, `eur`, `clp`) | `usd` |
| `COINGECKO_API_KEY` | Clave de API de CoinGecko (opcional para plan gratuito) | *(vacío)* |

### Configurar variables en Linux/Mac:
```bash
export CRYPTO_ID="ethereum"
export MONEDA_FIAT="clp"
export COINGECKO_API_KEY="tu_clave_aqui"
```

### Configurar variables en Windows (PowerShell):
```powershell
$env:CRYPTO_ID = "ethereum"
$env:MONEDA_FIAT = "clp"
$env:COINGECKO_API_KEY = "tu_clave_aqui"
```

---

## 🐳 Ejecución con Docker

### 1. Construir la imagen:
```bash
docker build -t crypto_app .
```

### 2. Ejecutar el contenedor:
```bash
docker run --name samplerunning \
  -e CRYPTO_ID=bitcoin \
  -e MONEDA_FIAT=usd \
  -e COINGECKO_API_KEY=tu_clave \
  crypto_app
```

### 3. Ver estado del contenedor:
```bash
docker ps -a
```

### 4. Ver logs:
```bash
docker logs samplerunning
```

### 5. Usando el script de automatización:
```bash
chmod +x build.sh
./build.sh
```

---

## 📁 Estructura del Repositorio

```
crypt-app-P2/
├── app.py              # Script principal que consulta la API
├── build.sh            # Script de automatización (build + run)
├── Dockerfile          # Definición de la imagen Docker
├── requirements.txt    # Dependencias Python
├── .gitignore          # Archivos excluidos del repositorio
├── README.md           # Documentación del proyecto
└── evidencias/
    ├── docker/
    │   ├── output.txt          # docker ps -a + logs con datos reales
    │   └── screenshot.png      # Captura de la salida en consola
    └── jenkins/
        ├── stage_view.png              # Stage View de SamplePipeline
        ├── console_output_build.png    # Console Output de BuildAppJob
        ├── credentials.png             # Credenciales GitHub en Jenkins
        └── pipeline_script.txt         # Script inline de SamplePipeline
```

---

## 🔧 Errores Manejados

| Error | Descripción |
|---|---|
| `Timeout` | La API no respondió en el tiempo límite |
| `ConnectionError` | Sin conexión a internet o API caída |
| `HTTP 401` | Clave de API inválida o no autorizada |
| `HTTP 404` | Criptomoneda no encontrada |
| `HTTPError` | Otros errores HTTP inesperados |
| `ValueError` | Respuesta no válida (JSON malformado) |

---

## 🛠️ Pipeline Jenkins

**SamplePipeline** orquesta el flujo completo en dos etapas:

```groovy
node {
  stage('Preparation') {
    catchError(buildResult: 'SUCCESS') {
      sh 'docker stop samplerunning'
      sh 'docker rm samplerunning'
    }
  }
  stage('Build') {
    build 'BuildAppJob'
  }
}
```
